(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["registration"],{"032d":function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("base-layout",{attrs:{buttonName:"Sign up"},on:{startAction:e.signupUser},scopedSlots:e._u([{key:"registrationTexts",fn:function(){return[a("p",{staticClass:"mt-3 mb-3"},[e._v("Already using "+e._s(e.companyDetails.name)+"? "),a("router-link",{attrs:{to:{name:"signin"}}},[e._v("Login here")])],1)]},proxy:!0}])},[e._l(e.fields,(function(t,n){return a("div",{key:t.id,staticClass:"form-group",class:{"mt-2":n>0}},[null!==t.label?a("label",{staticClass:"font-weight-bold",attrs:{for:t.name}},[e._v(" "+e._s(t.label)+" ")]):e._e(),"checkbox"===t.type?a("input",{directives:[{name:"model",rawName:"v-model",value:e.credentials[t.name],expression:"credentials[field.name]"}],staticClass:"form-control",attrs:{name:t.name,id:t.name,placeholder:t.placeholder,autocomplete:t.autocomplete,type:"checkbox"},domProps:{checked:Array.isArray(e.credentials[t.name])?e._i(e.credentials[t.name],null)>-1:e.credentials[t.name]},on:{change:function(a){var n=e.credentials[t.name],s=a.target,o=!!s.checked;if(Array.isArray(n)){var r=null,l=e._i(n,r);s.checked?l<0&&e.$set(e.credentials,t.name,n.concat([r])):l>-1&&e.$set(e.credentials,t.name,n.slice(0,l).concat(n.slice(l+1)))}else e.$set(e.credentials,t.name,o)}}}):"radio"===t.type?a("input",{directives:[{name:"model",rawName:"v-model",value:e.credentials[t.name],expression:"credentials[field.name]"}],staticClass:"form-control",attrs:{name:t.name,id:t.name,placeholder:t.placeholder,autocomplete:t.autocomplete,type:"radio"},domProps:{checked:e._q(e.credentials[t.name],null)},on:{change:function(a){return e.$set(e.credentials,t.name,null)}}}):a("input",{directives:[{name:"model",rawName:"v-model",value:e.credentials[t.name],expression:"credentials[field.name]"}],staticClass:"form-control",attrs:{name:t.name,id:t.name,placeholder:t.placeholder,autocomplete:t.autocomplete,type:t.type},domProps:{value:e.credentials[t.name]},on:{input:function(a){a.target.composing||e.$set(e.credentials,t.name,a.target.value)}}})])})),a("p",[e._v("By using "+e._s(e.companyDetails.name)+" you agree to our "),a("router-link",{staticClass:"font-weight-bold",attrs:{to:{name:"terms_of_use"}}},[e._v("Terms of service")]),e._v(" and our "),a("router-link",{staticClass:"font-weight-bold",attrs:{to:{name:"terms_of_condition"}}},[e._v("Privacy policy")])],1)],2)},s=[],o=a("36b3"),r={name:"Signup",title:function(){return"Signup"},components:{BaseLayout:o["a"]},data:function(){return{fields:[{id:1,name:"email",type:"email",autocomplete:"email",placeholder:"Email",label:"Email"},{id:2,name:"username",type:"text",autocomplete:"username",placeholder:"Username",label:"Username"},{id:3,name:"first_name",type:"text",autocomplete:"given-name",placeholder:"Firstname",label:"Firstname"},{id:4,name:"last_name",type:"text",autocomplete:"family-name",placeholder:"Lastname",label:"Lastname"},{id:5,name:"password1",type:"password",autocomplete:"new-password",placeholder:"Password",label:"Password"},{id:6,name:"password2",type:"password",autocomplete:"new-password",placeholder:"Confirm password",label:null}],credentials:{}}},computed:{isValid:function(){var e=this.credentials,t=e.password1,a=e.password2;return t===a}},methods:{signupUser:function(){this.$store.dispatch("authenticationModule/signUp",this.credentials)}}},l=r,i=a("2877"),c=Object(i["a"])(l,n,s,!1,null,null,null);t["default"]=c.exports},"136d":function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("base-layout",{attrs:{buttonName:"Sign in to your account"},on:{startAuthentication:e.loginUser},scopedSlots:e._u([{key:"registrationTexts",fn:function(){return[a("div",{staticClass:"col-md-12 col-xl-12 text-white"},[a("p",{staticClass:"mt-3"},[e._v("Don't have an account? "),a("router-link",{staticClass:"font-weight-bold text-muted",attrs:{to:{name:"signup"}}},[e._v("Get yours now")])],1),a("p",{staticClass:"mt-3 mb-3"},[e._v("Forgot your password? "),a("router-link",{staticClass:"font-weight-bold text-muted",attrs:{to:{name:"forgot"}}},[e._v("Send yourself a new one")])],1)])]},proxy:!0}])},[a("div",{staticClass:"form-group"},[a("label",{staticClass:"font-weight-bold",attrs:{for:"email"}},[e._v("Email")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.credentials["email"],expression:"credentials['email']"}],staticClass:"form-control",attrs:{type:"email",id:"email",autocomplete:"email",placeholder:"Email"},domProps:{value:e.credentials["email"]},on:{input:function(t){t.target.composing||e.$set(e.credentials,"email",t.target.value)}}})]),a("div",{staticClass:"form-group mt-3"},[a("label",{staticClass:"font-weight-bold",attrs:{for:"email"}},[e._v("Password")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.credentials["password"],expression:"credentials['password']"}],staticClass:"form-control",attrs:{type:"password",id:"password",autocomplete:"current-password",placeholder:"Password"},domProps:{value:e.credentials["password"]},on:{input:function(t){t.target.composing||e.$set(e.credentials,"password",t.target.value)}}})])])},s=[],o=a("5530"),r=a("36b3"),l=a("2f62"),i={name:"Signin",title:function(){return"Signin"},components:{BaseLayout:r["a"]},data:function(){return{credentials:{email:null,username:null,password:null},rememberMe:!1}},methods:Object(o["a"])(Object(o["a"])({},Object(l["b"])("authenticationModule",["login"])),{},{loginUser:function(){var e=this;this.$api.auth.login(this.credentials.email,this.credentials.password).then((function(t){e.login(t),e.$router.push({name:"home"})})).catch((function(e){console.log(e)}))}})},c=i,u=a("2877"),m=Object(u["a"])(c,n,s,!1,null,null,null);t["default"]=m.exports},"36b3":function(e,t,a){"use strict";var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"row justify-content-center"},[a("div",{staticClass:"col-xl-5 col-md-8"},[a("b-card",{staticClass:"mt-5",scopedSlots:e._u([{key:"footer",fn:function(){return[a("button",{staticClass:"btn btn-primary",on:{click:function(t){return e.$emit("startAuthentication")}}},[e._v(" "+e._s(e.buttonName)+" ")])]},proxy:!0}])},[a("transition-group",{attrs:{name:"general-transition"}},e._l(e.messages,(function(t){return a("div",{key:t.id,staticClass:"alert alert-danger",class:t.type,attrs:{role:"alert"}},[e._v(" "+e._s(t.content)+" ")])})),0),e._t("default")],2),e._t("registrationTexts")],2)])},s=[],o={name:"BaseLayout",props:{buttonName:{type:String,default:"Authenticate"}},computed:{messages:function(){return this.$store.getters["getMessagesFor"]("auth")}}},r=o,l=a("2877"),i=Object(l["a"])(r,n,s,!1,null,null,null);t["a"]=i.exports},b789:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("base-layout",{attrs:{buttonName:"Send me a password reset email"},on:{startAction:e.sendRequest},scopedSlots:e._u([{key:"registrationTexts",fn:function(){return[a("p",{staticClass:"mt-3 mb-3"},[e._v("Actually, I remember my password "),a("router-link",{staticClass:"font-weight-bold",attrs:{to:{name:"signin"}}},[e._v("Login here")])],1)]},proxy:!0}])},[a("div",{staticClass:"form-group"},[a("label",{staticClass:"font-weight-bold",attrs:{for:"email"}},[e._v("Email")]),a("input",{directives:[{name:"model",rawName:"v-model",value:e.email,expression:"email"}],staticClass:"form-control",attrs:{type:"email",id:"email",autocomplete:"email",placeholder:"Email"},domProps:{value:e.email},on:{input:function(t){t.target.composing||(e.email=t.target.value)}}})])])},s=[],o=a("36b3"),r=a("2ef0"),l={name:"ForgotPassword",title:function(){return"Forgot password"},components:{BaseLayout:o["a"]},data:function(){return{email:null}},beforeRouteEnter:function(e,t,a){a((function(e){return!!e.$store.getters["authenticationModule/isAuthenticated"]||"profile_passwords"}))},computed:{hasEmail:function(){return Object(r["isNull"])(this.email)}},methods:{sendRequest:function(){this._validateEmail(this.email)?(console.log("Requested email change"),this.$router.push({name:"signin"})):console.error("Email is not valid")}}},i=l,c=a("2877"),u=Object(c["a"])(i,n,s,!1,null,null,null);t["default"]=u.exports}}]);
//# sourceMappingURL=registration.333ae536.js.map