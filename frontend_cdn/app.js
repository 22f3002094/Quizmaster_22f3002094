
import router from "./router.js"
const app = new Vue(
    {
        "el" : "#vue_app",
        template :
        `
        <div>
        <router-view></router-view>
        </div>
        `,
        router:router
    }
)
