import { createRouter,createWebHistory } from "vue-router";
//import components here that are to be routed
import login from './components/LoginComp.vue';
import HomeComp from './components/HomeComp.vue';
import RegisterComp from './components/RegisterComp.vue';
import AdminDashboard from './pages/admindashboard.vue';
import StudentDashboard from './pages/studentdashboard.vue';
import Subjects from "./components/subjects.vue";
import Chapters from "./components/chapters.vue";
import Subjectform from "./components/subjectform.vue";
import Quizes from "./components/quizes.vue";
import Formquiz from "./components/formquiz.vue";
import QuizAttemp from "./components/quizAttemp.vue";
const routes = [
    {path:"/", component: HomeComp},
    {path:"/login", component: login},
    {path:"/register", component: RegisterComp},
    {path:"/admin", component:AdminDashboard,
        children : [
            {path :"dashboard" ,  component: Subjects },
            {path :"subject/:subname" , component : Chapters},
            {path: "create/subject" , component : Subjectform },
            {path: "edit/subject" , component : Subjectform },
            {path: "chapter/:chapname" , component: Quizes},
            {path: ":chapname/create/quiz" , component : Formquiz },

        ]
        
    },
    {path:"/student", component:StudentDashboard,
        children:[
            {path:'dashboard' , component:Subjects},
            {path :"subject/:subname" , component : Chapters},
            {path: "chapter/:chapname" , component: Quizes},
            {path:"attemptquiz/:quizid" , component:QuizAttemp}
        ]
    }
]


const router= createRouter({
    history: createWebHistory(),

    routes
})

export default router;