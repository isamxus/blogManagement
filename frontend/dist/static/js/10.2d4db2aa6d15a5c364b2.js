webpackJsonp([10],{D0pu:function(t,e){},vU1N:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=s("aA9S"),o=s.n(r),a=s("C7Kb"),n=s("rVsN"),i=s.n(n),l={userUpdate:function(t){return axios.post(REQUEST_URL.userUpdate,REQUEST_URL.handleParams(t)).then(function(t){return i.a.resolve(t.data.PostContent)})},userChangePassword:function(t){return axios.post(REQUEST_URL.userChangePassword,REQUEST_URL.handleParams(t)).then(function(t){return i.a.resolve(t.data.PostContent)})}},d={data:function(){return{breadcrumbs:[{title:this.$route.meta.title}],settingForm:o()({user_id:"",UserName:"",UserHeadImg:"",PassWord:"",NewPassWord:"",RetypePassWord:"",Edit:!1,uploadStatus:null,uploadList:[]},t),settingFormRules:{PassWord:[{required:!0,message:"请输入原密码"}],NewPassWord:[{required:!0,message:"请输入新密码"}],RetypePassWord:[{required:!0,message:"请再次输入新密码"}]},imageUrl:"",popModal:!1,uploadUrl:REQUEST_URL.userImageUpload};var t},components:{SubNavigationFrame:a.a},computed:{},mounted:function(){this.setInfoHandler()},methods:{setInfoHandler:function(){var t=this.$store.state.UserInfo;t||this.$router.push({name:"Index"}),this.imageUrl=t.UserHeadImg?""+REQUEST_URL.staticDownload+t.UserHeadImg:"",this.settingForm.UserName=t.UserName,this.settingForm.user_id=t.user_id,this.settingForm.UserHeadImg=t.UserHeadImg},handleBeforeUploadNum:function(t,e){return t?t.$props.maxSize&&e.size/1024>t.$props.maxSize?(this.handleError({Msg:"文件体积过大，无法上传",State:-1},e,this.settingForm.uploadList),!1):(this.settingForm.uploadStatus=this.$Message.loading({content:"正在上传文档，请稍等...",duration:0}),void(this.settingForm.uploadList.length&&this.$refs.uploadFileRef.clearFiles())):(this.handleError({Msg:"无法获取上传组件",State:-1},e,this.settingForm.uploadList),!1)},handleSuccess:function(t,e,s){if(1!=t.State)return this.handleError(t,e,s),s.splice(s.length-1,1);if(this.settingForm.uploadStatus(),this.settingForm.uploadStatus=null,1!=t.State)return this.handleError(t,e,s),s.splice(s.length-1,1);var r=this.settingForm;r.UserHeadImg=e.response.PostContent.Address,this.imageUrl=""+REQUEST_URL.staticDownload+r.UserHeadImg},handleFormatError:function(t,e){this.settingForm.uploadStatus(),this.settingForm.uploadStatus=null,this.$Message.warning("文件格式错误，请重新上传")},handleError:function(t,e,s){this.settingForm.uploadStatus(),this.settingForm.uploadStatus=null,this.$Message.warning(t&&t.Msg||"文件上传失败")},handleMaxSize:function(t){this.settingForm.uploadStatus(),this.settingForm.uploadStatus=null,this.$Message.warning("超出文件大小限制，文档不能超过 15M")},submitDataHandler:function(){var t=this;if(this.settingForm.Edit)return this.$Message.warning("请点击完成修改");l.userUpdate({PostContent:{user_id:this.settingForm.user_id,UserName:this.settingForm.UserName,UserHeadImg:this.settingForm.UserHeadImg}}).then(function(e){t.$Message.success("成功修改信息")}).catch(function(e){t.$Message.error(e)})},changePasswordHandler:function(){var t=this;return this.settingForm.PassWord?this.settingForm.NewPassWord?this.settingForm.RetypePassWord?this.settingForm.RetypePassWord!=this.settingForm.NewPassWord?this.$Message.warning("两次输入密码不一致"):void l.userChangePassword({PostContent:{user_id:this.settingForm.user_id,UserName:this.settingForm.UserName,PassWord:this.settingForm.PassWord,NewPassWord:this.settingForm.NewPassWord}}).then(function(e){t.$Message.success("成功修改密码"),t.popModal=!1}).catch(function(e){t.$Message.error(e)}):this.$Message.warning("请再次输入新密码"):this.$Message.warning("请输入新密码"):this.$Message.warning("请输入原密码")}}},u={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("SubNavigationFrame",{attrs:{title:t.$route.meta.title,breadcrumb:t.breadcrumbs}},[s("div",{staticClass:"user_setting_container",attrs:{slot:"content"},slot:"content"},[s("Row",[s("div",{style:{textAlign:"right"}},[s("Button",{attrs:{type:"primary"},on:{click:function(e){t.popModal=!0}}},[t._v("修改密码")]),t._v(" "),s("Button",{on:{click:function(e){return t.$router.push({name:"Index"})}}},[t._v("返回主页")])],1)]),t._v(" "),s("Row",[s("Col",{style:{textAlign:"center",marginBottom:".7rem"},attrs:{span:"8",offset:"8"}},[s("Avatar",{directives:[{name:"show",rawName:"v-show",value:!t.imageUrl,expression:"!imageUrl"}],attrs:{icon:"ios-person",size:"100"}}),t._v(" "),s("Avatar",{directives:[{name:"show",rawName:"v-show",value:t.imageUrl,expression:"imageUrl"}],attrs:{src:t.imageUrl,size:"100"}})],1),t._v(" "),s("Col",{attrs:{span:"6",offset:"9"}},[s("Upload",{ref:"uploadFileRef",style:{display:"inline-block",width:"100%"},attrs:{action:t.uploadUrl,format:["jpg","png","jpeg"],"max-size":1e5,"before-upload":function(e){return t.handleBeforeUploadNum(t.$refs.uploadFileRef,e)},"on-success":t.handleSuccess,"on-format-error":t.handleFormatError,"on-error":t.handleError,"on-exceeded-size":t.handleMaxSize,"show-upload-list":!1}},[s("Button",{attrs:{long:""}},[t._v("更换头像")])],1)],1)],1),t._v(" "),s("Row",[s("Col",{style:{display:"flex",justifyContent:"center",marginTop:"1.4rem"},attrs:{span:"24"}},[s("Form",{ref:"settingForm",attrs:{"label-width":100,model:t.settingForm,rules:t.settingFormRules}},[s("FormItem",{staticClass:"sub-page-input-container min-input-container",attrs:{label:"用户名：",prop:"UserName"}},[s("Input",{attrs:{readonly:!t.settingForm.Edit,placeholder:"请输入用户名"},model:{value:t.settingForm.UserName,callback:function(e){t.$set(t.settingForm,"UserName",e)},expression:"settingForm.UserName"}}),t._v(" "),s("Icon",{attrs:{type:"ios-create-outline"}}),s("span",{directives:[{name:"show",rawName:"v-show",value:!t.settingForm.Edit,expression:"!settingForm.Edit"}],style:{color:"#2b85e4",cursor:"pointer"},on:{click:function(e){t.settingForm.Edit=!0}}},[t._v("修改")]),s("span",{directives:[{name:"show",rawName:"v-show",value:t.settingForm.Edit,expression:"settingForm.Edit"}],style:{color:"#2b85e4",cursor:"pointer"},on:{click:function(e){t.settingForm.Edit=!1}}},[t._v("完成")])],1)],1)],1),t._v(" "),s("Col",{attrs:{span:"6",offset:"9"}},[s("Button",{attrs:{type:"primary",long:""},on:{click:t.submitDataHandler}},[t._v("确认修改")])],1)],1),t._v(" "),s("Modal",{attrs:{title:"修改密码",width:"400"},on:{"on-visible-change":function(e){return t.$refs.createForm.resetFields()}},model:{value:t.popModal,callback:function(e){t.popModal=e},expression:"popModal"}},[s("Form",{ref:"createForm",attrs:{"label-width":150,model:t.settingForm,rules:t.settingFormRules}},[s("FormItem",{attrs:{label:"原密码：",prop:"PassWord"}},[s("Input",{attrs:{placeholder:"请输入原密码"},model:{value:t.settingForm.PassWord,callback:function(e){t.$set(t.settingForm,"PassWord",e)},expression:"settingForm.PassWord"}})],1),t._v(" "),s("FormItem",{attrs:{label:"新密码：",prop:"NewPassWord"}},[s("Input",{attrs:{placeholder:"请输入新密码"},model:{value:t.settingForm.NewPassWord,callback:function(e){t.$set(t.settingForm,"NewPassWord",e)},expression:"settingForm.NewPassWord"}})],1),t._v(" "),s("FormItem",{attrs:{label:"再次输入新密码：",prop:"RetypePassWord"}},[s("Input",{attrs:{placeholder:"请再次输入新密码"},model:{value:t.settingForm.RetypePassWord,callback:function(e){t.$set(t.settingForm,"RetypePassWord",e)},expression:"settingForm.RetypePassWord"}})],1)],1),t._v(" "),s("div",{attrs:{slot:"footer"},slot:"footer"},[s("Button",{attrs:{type:"primary"},on:{click:t.changePasswordHandler}},[t._v("确定")]),t._v(" "),s("Button",{on:{click:function(e){t.popModal=!1}}},[t._v("取消")])],1)],1)],1)])},staticRenderFns:[]};var m=s("C7Lr")(d,u,!1,function(t){s("D0pu")},null,null);e.default=m.exports}});
//# sourceMappingURL=10.2d4db2aa6d15a5c364b2.js.map