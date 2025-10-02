
import greeting from "./greeting.js"

app = new Vue(
    {
        "el" : "#vue_app",
        template :
        `
        <greeting></greeting>
        `,
        components:{
            greeting
        }
    }
)
