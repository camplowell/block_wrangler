import { MenuItem as SzhMenuItem } from "@szhsin/react-menu";

const MenuItem = function({children, ...props}) {
	return (
			<SzhMenuItem {...props}><span className="menu-item-content">{children}</span></SzhMenuItem>
	)
}

export default MenuItem;