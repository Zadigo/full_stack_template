"use strict";(self["webpackChunkvue_templates"]=self["webpackChunkvue_templates"]||[]).push([[6733,9629],{6819:function(e,o,n){n.d(o,{Z:function(){return r}});var t=n(4870),a=n(9307);function r(){const e=(0,t.iH)([]),o=(0,t.iH)({email:null,password:null}),n=(0,t.iH)({username:null,firstname:null,lastname:null,email:null,password1:null,password2:null}),r=(0,t.iH)({email:null}),s=(0,t.iH)({verification_code:null});function i(){return n.value.password1===n.value.password2}async function l(e,n){try{const n=await a.L.post("accounts/login",o.value);try{e(n)}catch(t){console.error(t)}}catch(t){"function"===typeof n?n([t.message,t.response.data]):console.error(t)}}async function c(e,o){try{const o=await a.L.post("accounts/signup",n.value);try{e(o)}catch(t){console.error(t)}}catch(t){o([t.message,t.response.data])}}async function u(e,o){try{await a.L.post("accounts/logout");try{e()}catch(n){console.error(n)}}catch(n){o([n.message,n.response.data])}}async function p(e,o){try{await a.L.post("accounts/verify-account",s.value);try{e()}catch(n){console.error(n)}}catch(n){o([n.message,n.response.data])}}return{verificationCredentials:s,authenticationErrors:e,loginCredentials:o,signupCredentials:n,forgotPasswordCredentials:r,performLogin:l,performSignup:c,performLogout:u,performAccountVerification:p,passwordsValid:i}}},9629:function(e,o,n){n.r(o),n.d(o,{default:function(){return h}});var t=n(3396);const a={class:"row"},r={class:"col-12 my-2"},s={key:0,class:"my-1"},i=(0,t.Uk)("Don't have an account? "),l=(0,t.Uk)("Create one"),c={key:1,class:"my-1"},u=(0,t.Uk)("Already have an account? "),p=(0,t.Uk)("Signin"),d={key:2,class:"my-1"},m=(0,t.Uk)("Forgot your password? "),g=(0,t.Uk)("Reset password");function f(e,o,n,f,w,v){const y=(0,t.up)("router-link");return(0,t.wg)(),(0,t.iD)("div",a,[(0,t._)("div",r,["login_view"===e.$route.name?((0,t.wg)(),(0,t.iD)("p",s,[i,(0,t.Wm)(y,{to:{name:"signup_view"}},{default:(0,t.w5)((()=>[l])),_:1})])):(0,t.kq)("",!0),"signup_view"===e.$route.name?((0,t.wg)(),(0,t.iD)("p",c,[u,(0,t.Wm)(y,{to:{name:"login_view"}},{default:(0,t.w5)((()=>[p])),_:1})])):(0,t.kq)("",!0),"login_view"===e.$route.name?((0,t.wg)(),(0,t.iD)("p",d,[m,(0,t.Wm)(y,{to:{name:"forgot_passoword_view"}},{default:(0,t.w5)((()=>[g])),_:1})])):(0,t.kq)("",!0)])])}var w={name:"ForgotPassword"},v=n(89);const y=(0,v.Z)(w,[["render",f]]);var h=y},6733:function(e,o,n){n.r(o),n.d(o,{default:function(){return v}});var t=n(3396),a=n(9242);const r={class:"card-body"},s={class:"row"},i={class:"col-12"},l={class:"col-12"},c={class:"card-footer"};function u(e,o,n,u,p,d){const m=(0,t.up)("auth-navigation-vue");return(0,t.wg)(),(0,t.iD)(t.HY,null,[(0,t._)("div",r,[(0,t._)("div",s,[(0,t._)("div",i,[(0,t._)("form",{onSubmit:o[2]||(o[2]=(0,a.iM)((()=>{}),["prevent"]))},[(0,t.wy)((0,t._)("input",{"onUpdate:modelValue":o[0]||(o[0]=e=>u.loginCredentials.email=e),type:"email",autocomplete:"email",class:"form-control p-2 my-2"},null,512),[[a.nr,u.loginCredentials.email]]),(0,t.wy)((0,t._)("input",{"onUpdate:modelValue":o[1]||(o[1]=e=>u.loginCredentials.password=e),type:"password",autocomplete:"current-password",class:"form-control p-2 my-2"},null,512),[[a.nr,u.loginCredentials.password]])],32)]),(0,t._)("div",l,[(0,t.Wm)(m)])])]),(0,t._)("div",c,[(0,t._)("button",{type:"button",class:"btn btn-primary",onClick:o[3]||(o[3]=(...e)=>d.completeLogin&&d.completeLogin(...e))}," Login ")])],64)}var p=n(6819),d=n(9629),m=n(2097),g={name:"LoginView",components:{AuthNavigationVue:d["default"]},emits:{submitted:()=>!0},setup(){const e=(0,m.J)(),{loginCredentials:o,performLogin:n}=(0,p.Z)();return{store:e,loginCredentials:o,performLogin:n}},methods:{completeLogin(){this.performLogin((e=>{this.store.loginUser(e.data),this.$session.create("auth",e.data),this.$router.push({name:"home_view"})}),(e=>{console.error(e)}))}}},f=n(89);const w=(0,f.Z)(g,[["render",u]]);var v=w}}]);
//# sourceMappingURL=6733.4921169c.js.map