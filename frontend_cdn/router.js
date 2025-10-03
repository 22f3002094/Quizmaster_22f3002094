import login from './login.js';

const routes = [
    {path:"/login", component: login}
]
const router = new VueRouter({
    routes
})
export default router