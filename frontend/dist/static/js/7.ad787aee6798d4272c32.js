webpackJsonp([7],{b11J:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=n("rVsN"),r=n.n(o),a={commentGetPageList:function(e){return axios.post(REQUEST_URL.commentGetPageList,REQUEST_URL.handleParams(e)).then(function(e){return r.a.resolve(e.data.PostContent)})},commentDelete:function(e){return axios.post(REQUEST_URL.commentDelete,REQUEST_URL.handleParams(e)).then(function(e){return r.a.resolve(e.data.PostContent)})}},i={name:"commentManagement",data:function(){return{breadcrumbs:[{title:this.$route.query.paramsName}],columns:[{title:"序号",type:"index",width:120},{title:"评论者",key:"commentAuthor",width:120},{title:"评论内容",key:"commentContent",width:400},{title:"所属文章",key:"parentArticleTitle",width:200},{title:"创建时间",key:"CreateTime",width:220,render:this.TimeRender},{title:"操作",align:"center",render:this.toolColumnRender}],commentListData:[],PageCount:0,PageNumber:1,PageSize:10}},components:{SubNavigationFrame:n("C7Kb").a},mounted:function(){this.$store.commit("showAdminMenu",!0),this.getCommentListHandler()},methods:{TimeRender:function(e,t){return e("span",{domProps:{innerText:new Date(t.row.CreateTime).Format("yyyy-MM-dd hh:mm")}})},getCommentListHandler:function(){var e=this;a.commentGetPageList({PostContent:{_OrderBy:"-CreateTime",PageSize:this.PageSize,PageNumber:this.PageNumber}}).then(function(t){e.commentListData=t.Items.map(function(e){return e.CreateTime=new Date(e.CreateTime).Format("yyyy-MM-dd hh:mm"),e}),e.PageCount=t.TotalItems}).catch(function(t){e.$Message.error(t)})},toolColumnRender:function(e,t){var n=this;return e("div",[e("Button",{props:{type:"text"},domProps:{innerText:"删除"},on:{click:function(e){n.deleteCommentHandler(t.row.comment_id),e.stopPropagation()}}})])},deleteCommentHandler:function(e){var t=this;if(!e)return this.$Message.warning("参数ID为空，无法删除！！！");this.$Modal.confirm({title:"操作确认",icon:"warning",content:"是否删除此评论",okText:"确定",showCancel:!0,loading:!0,onOk:function(){a.commentDelete({PostContent:{comment_id:e}}).then(function(e){t.$Message.success("成功删除评论！！！"),t.$Modal.remove(),t.getCommentListHandler()}).catch(function(e){t.$Modal.remove(),t.$Message.error(e)})}})}}},m={render:function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("SubNavigationFrame",{attrs:{title:e.$route.query.paramsName,breadcrumb:e.breadcrumbs}},[n("div",{style:{textAlign:"right",marginTop:"-2.5rem"},attrs:{slot:"navigation"},slot:"navigation"},[n("Button",{on:{click:function(t){return e.$router.push({name:"Index"})}}},[e._v("返回主站")]),e._v(" "),n("Button",{on:{click:function(t){return e.$router.go(-1)}}},[e._v("返回")])],1),e._v(" "),n("div",{staticClass:"sub-page-container",style:{"margin-top":".5rem","padding-top":"1rem"},attrs:{slot:"content"},slot:"content"},[n("div",{style:{overflow:"auto"}},[n("Table",{style:{minWidth:"1400px"},attrs:{columns:e.columns,data:e.commentListData}})],1),e._v(" "),n("Page",{style:{paddingTop:"1rem",textAlign:"center"},attrs:{total:e.PageCount,current:e.PageNumber,"page-size":e.PageSize,placement:"top","show-elevator":"","show-total":"","show-sizer":""},on:{"on-change":function(t){e.PageNumber=t,e.getAricleListHandler()},"on-page-size-change":function(t){e.PageSize=t,e.getAricleListHandler()}}})],1)])},staticRenderFns:[]};var s=n("C7Lr")(i,m,!1,function(e){n("im9A")},null,null);t.default=s.exports},im9A:function(e,t){}});
//# sourceMappingURL=7.ad787aee6798d4272c32.js.map