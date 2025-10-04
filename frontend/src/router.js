import { createRouter,createWebHistory } from "vue-router";
//import components here that are to be routed
import login from './components/LoginComp.vue';
import HomeComp from './components/HomeComp.vue';
import RegisterComp from './components/RegisterComp.vue';
import AdminDashboard from './pages/admindashboard.vue';
import StudentDashboard from './pages/studentdashboard.vue';

const routes = [
    {path:"/", component: HomeComp},
    {path:"/login", component: login},
    {path:"/register", component: RegisterComp},
    {path:"/admin/dashboard", component:AdminDashboard},
    {path:"/student/dashboard", component:StudentDashboard}
]


const router= createRouter({
    history: createWebHistory(),

    routes
})

export default router;