import React, { useEffect, useState } from "react";
import TreeView, { flattenTree, INode, NodeId } from "react-accessible-treeview";
import * as ContextMenu from "@radix-ui/react-context-menu";
import styles from './SearchableTree.module.css';

const SearchableTreeView: React.FC<{data: any, filter: string, action:(element:INode) => void, action_label:string, poll_action:(element:INode) => boolean}> = ({data, filter, action=(x)=>{}, action_label="Copy", poll_action=(x)=>true, ...props}) => {
	const baked_data = flattenTree(data);
	// const all_ids = new Set(baked_data.map((x) => x.id));
	const [no_results, setNoResults] = useState(false);
	var update_filters = new Map<NodeId, (included:boolean) => void>();

	useEffect(() => {
		if (!filter) {
			for (const [id, fn] of update_filters) {
				fn(true);
			}
			return;
		}
		const filtered_ids: Set<NodeId> = new Set();
		var filtered_root = null;
		const touch = (item:INode) => {
			if (filtered_ids.has(item.id)) return;
			filtered_ids.add(item.id);
		}
		const includeAncestors = (id) => {
			baked_data.forEach((item) => {
				if (item.id === id) {
					if (item.parent === null) return;
					touch(item);
					if (item.parent) includeAncestors(item.parent);
				}
			})
		}
		const includeChildren = (id: NodeId) => {
		baked_data.forEach((item) => {
			if (item.parent === id) {
				touch(item);
				if (item.children.length) {
					includeChildren(item.id);
				}
			}
		});
		};
		const filter_stem = /[^/:]*$/.exec(filter)[0];
		baked_data.forEach((item) => {
			if (item.parent === null) {
				filtered_root = {...item};
				return;
			}
			if (item.name.includes(filter)) { // TODO: more complex search function here
				touch(item);
				const item_stem = /[^/:]*$/.exec(item.name)[0]
				if (
					item_stem.includes(filter_stem) && // Reasonably searching for this exact tag (vs one of its parents)
					item.children.length > 0
				) {
					includeChildren(item.id);
				}

				if (item.parent) {
					includeAncestors(item.parent); // Don't leave hanging nodes!
				}
			}
		});
		filtered_ids.add(filtered_root.id);
		for (const [id, fn] of update_filters) {
			fn(filtered_ids.has(id));
		}
		setNoResults(filtered_ids.size < 2);
	}, [filter]);

	return no_results ? (
		<div>No results.</div>
	) : (
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
				isDisabled,
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
					<ContextMenu.Root>
						<ContextMenu.Trigger 
						{...getNodeProps({onClick: () => {}})}
						style={{
							"--level-padding": `${40 * (level - 1)}px`,
							width: "100%",
						} as React.CSSProperties}
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
						</ContextMenu.Trigger>
						<ContextMenu.Portal>
							<ContextMenu.Content className="ContextMenuContent">
								{isBranch && (
									<ContextMenu.Item className="ContextMenuItem" onClick={handleExpand}>{isExpanded ? "Collapse" : "Expand"}</ContextMenu.Item>
								)}
								{poll_action(element) && (
									<ContextMenu.Item className="ContextMenuItem" onClick={() => action(element)}>{action_label}</ContextMenu.Item>
								)}
							</ContextMenu.Content>
						</ContextMenu.Portal>
					</ContextMenu.Root>
				)
			}}
		/>
	);
}


export default SearchableTreeView;