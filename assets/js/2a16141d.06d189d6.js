"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[625],{4578:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>i,contentTitle:()=>a,default:()=>d,frontMatter:()=>r,metadata:()=>l,toc:()=>c});var s=n(4848),o=n(8453);const r={slug:"alpha-blog-post",title:"First alpha release!",authors:["lowell"],tags:["announcement"]},a=void 0,l={permalink:"/block_wrangler/blog/alpha-blog-post",source:"@site/blog/2024-07-11-alpha-blog-post.mdx",title:"First alpha release!",description:"Welcome to the first alpha release of Block Wrangler!",date:"2024-07-11T00:00:00.000Z",tags:[{inline:!1,label:"Announcement",permalink:"/block_wrangler/blog/tags/announcements",description:"Big news or changes in direction"}],readingTime:1.44,hasTruncateMarker:!1,authors:[{name:"Lowell Camp",title:"Maintainer of Block Wrangler",url:"https://github.com/camplowell",imageURL:"https://github.com/camplowell.png",key:"lowell"}],frontMatter:{slug:"alpha-blog-post",title:"First alpha release!",authors:["lowell"],tags:["announcement"]},unlisted:!1},i={authorsImageUrls:[void 0]},c=[{value:"What&#39;s next?",id:"whats-next",level:2}];function h(e){const t={a:"a",code:"code",em:"em",h2:"h2",li:"li",p:"p",ul:"ul",...(0,o.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(t.p,{children:"Welcome to the first alpha release of Block Wrangler!"}),"\n",(0,s.jsxs)(t.p,{children:["The few of you who followed the ",(0,s.jsx)(t.a,{href:"https://github.com/camplowell/block_properties",children:"previous repository"})," might be wondering why I started over like this."]}),"\n",(0,s.jsx)(t.p,{children:"There are a few reasons for this:"}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsxs)(t.li,{children:["I discovered that ",(0,s.jsx)(t.code,{children:"block.properties"})," requires block IDs to be mutually exclusive, and the previous system wasn't capable of ensuring that.","\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsx)(t.li,{children:"In fact, changing the old system to be capable of this would have required a full rewrite anyways, so I decided to start over."}),"\n"]}),"\n"]}),"\n",(0,s.jsxs)(t.li,{children:["The old system required me to write and maintain a custom code interpreter, which isn't ideal for a project whose goal is ",(0,s.jsx)(t.em,{children:"not"})," to create a new programming language."]}),"\n"]}),"\n",(0,s.jsx)(t.p,{children:"All that to say, I started over, and I'm pretty happy with the results."}),"\n",(0,s.jsx)(t.p,{children:"In addition to rectifying those pain points, I also managed to squeeze out a few more features:"}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsxs)(t.li,{children:["I added the optional ",(0,s.jsx)(t.code,{children:"fuzzy_tags"})," feature, which allows the library to tell you if you misspelled a tag, or if it's a tag that doesn't exist."]}),"\n",(0,s.jsxs)(t.li,{children:["It's now possible to import block types and tags from mods and new versions of the game using the ",(0,s.jsx)(t.a,{href:"https://wiki.vg/Data_Generators",children:"data generator"}),"."]}),"\n",(0,s.jsxs)(t.li,{children:["Tags can now do things like include all blocks that have a certain property, or whose name matches a certain pattern.","\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsx)(t.li,{children:"...as long as you've registered the blocks before you define the tag."}),"\n"]}),"\n"]}),"\n",(0,s.jsx)(t.li,{children:"better progress bars!"}),"\n"]}),"\n",(0,s.jsx)(t.h2,{id:"whats-next",children:"What's next?"}),"\n",(0,s.jsx)(t.p,{children:"I have a few ideas on my wishlist for future releases:"}),"\n",(0,s.jsxs)(t.ul,{children:["\n",(0,s.jsx)(t.li,{children:"Improve the documentation for the project, of course"}),"\n",(0,s.jsx)(t.li,{children:"Add one or more project templates to help shaderpack developers get started with Block Wrangler"}),"\n",(0,s.jsx)(t.li,{children:"Add more preset tags for features that are commonly used in shaderpacks"}),"\n",(0,s.jsxs)(t.li,{children:["Numerical flags support (",(0,s.jsx)(t.code,{children:"int emission_brightness(int block_id)"}),")"]}),"\n"]})]})}function d(e={}){const{wrapper:t}={...(0,o.R)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(h,{...e})}):h(e)}},8453:(e,t,n)=>{n.d(t,{R:()=>a,x:()=>l});var s=n(6540);const o={},r=s.createContext(o);function a(e){const t=s.useContext(r);return s.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function l(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(o):e.components||o:a(e.components),s.createElement(r.Provider,{value:t},e.children)}}}]);