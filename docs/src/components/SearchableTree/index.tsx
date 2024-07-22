import React, { useEffect, useState } from "react";
import TreeView, { flattenTree, INode, NodeId } from "react-accessible-treeview";
import styles from './SearchableTree.module.css';
import { ClickEvent, ControlledMenu, MenuItem } from "@szhsin/react-menu";
import '@szhsin/react-menu/dist/index.css';
import { Index } from "flexsearch";

type EventCallback = <T, E>(event: React.MouseEvent<T, E> | React.KeyboardEvent<T>|ClickEvent) => void;

const SearchableTreeView: React.FC<{data: any, filter: string, render_context:(args:{element:INode, isBranch:boolean, isExpanded:boolean, level:number, handleExpand:(ClickEvent) => void}) => React.ReactNode, action:(element:INode) => void, action_label:string, poll_action:(element:INode) => boolean}> = ({
	data, 
	filter, 
	render_context=({element, isBranch, handleExpand, isExpanded})=>{
		if (!isBranch) return <span></span>;
		return (
			<MenuItem onClick={handleExpand}>{isExpanded ? "Collapse" : "Expand"}</MenuItem>
		)
	},
	...props
}) => {
	const baked_data = flattenTree(data);
	// const all_ids = new Set(baked_data.map((x) => x.id));
	const idx = new Index({
		tokenize: "forward"
	});
	baked_data.forEach((x) => {
		if (x.name) idx.add(x.id, x.name);
	});
	const root_id = baked_data.find((x) => x.parent === null).id;
	
	const [no_results, setNoResults] = useState(false);
	const [isOpen, setOpen] = useState(false);
	const [anchorPoint, setAnchorPoint] = useState({x: 0, y: 0});
	const [menuContext, setMenuContext] = useState<{element:INode, isBranch:boolean, isExpanded:boolean, level:number, handleExpand:EventCallback}>();
	var update_filters = new Map<NodeId, (included:boolean) => void>();

	const search = function(filter:string) {
		if (!filter) {
			for (const [id, fn] of update_filters) {
				fn(true);
			}
			return;
		}

		const filtered_ids: Set<NodeId> = new Set();
		const include = (id) => {
			if (filtered_ids.has(id)) return;
			baked_data.forEach((item) => {
				if (item.id === id) {
					if (item.parent === null) return;
					filtered_ids.add(item.id);
					if (item.parent) include(item.parent);
				}
			})
		}
		const includeChildren = (id: NodeId) => {
			baked_data.forEach((item) => {
				if (item.parent === id) {
					include(item.id);
					if (item.children.length) {
						includeChildren(item.id);
					}
				}
			});
		};
		
		const matches = idx.search(filter, baked_data.length);
		matches.forEach((match) => {
			include(match);
		});
		filtered_ids.add(root_id);
		for (const [id, fn] of update_filters) {
			fn(filtered_ids.has(id));
		}
		setNoResults(filtered_ids.size < 2);
	}

	useEffect(() => {
		const delayInputTimeoutId = setTimeout(() => search(filter), 100);
		return () => clearTimeout(delayInputTimeoutId);
	}, [filter, 100]);

	return no_results ? (
		<div>No results.</div>
	) : (
		<div>
		<TreeView
			data={baked_data}
			{...props}
			className={styles.tree}
			clickAction="EXCLUSIVE_SELECT"
			defaultExpandedIds={baked_data[0].children}
			nodeRenderer={({
				element,
				isBranch,
				isExpanded,
				getNodeProps,
				level,
				handleExpand,
				dispatch
			}) => {
				if (element.parent != null) {
					update_filters.set(element.id, (included:boolean) => {
						dispatch({
							type: included ? "ENABLE" : "DISABLE",
							id: element.id,
						});
					});
				}
				return (
					<div
					{...getNodeProps({onClick: () => {}})}
					style={{
						"--level-padding": `${40 * (level - 1)}px`,
						width: "100%",
					} as React.CSSProperties}
					onContextMenu={(e) => {
						e.preventDefault();
						setAnchorPoint({x: e.clientX, y: e.clientY});
						setMenuContext({
							element, 
							isBranch,
							isExpanded,
							level,
							handleExpand:(event) => {
								if ('syntheticEvent' in event) {
									handleExpand(event.syntheticEvent as any);
								} else {
									handleExpand(event);
								}
							}
						});
						setOpen(true);
					}}
					>
						{isBranch && <span style={{
							display: "inline-block",
							background: "var(--ifm-breadcrumb-separator) center no-repeat",
							backgroundOrigin: "content-box",
							transform: isExpanded ? "translate(2px, -5px) rotate(90deg)" : "",
							transition: "transform 0.1s",
							transformOrigin: "25% center",
							cursor: "pointer",
							filter: "var(--ifm-breadcrumb-separator-filter)",
							opacity: ".5",
							verticalAlign: "middle",
							boxSizing: "content-box",
							width: "1em",
							height: "1em",
							padding: "0.25em",
							paddingRight: "calc(0.25em + 0.5ch)",
							margin: "-0.25em",
						}}
						onClick={handleExpand}
						>&nbsp;</span>}
						<span className="name">{/[^/:]*$/.exec(element.name)[0]}</span>
					</div>
				)
			}}
		/>
		<ControlledMenu
			anchorPoint={anchorPoint}
			state={isOpen ? "open" : "closed"}
			onClose={() => setOpen(false)}
		>
			{Boolean(menuContext) && render_context(menuContext)}
		</ControlledMenu>
		</div>
	);
}


export default SearchableTreeView;