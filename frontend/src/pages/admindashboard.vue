<template>
    <div >
        <NavBar></NavBar>
        <h2>Welcome {{ username }} to admin dashboard</h2>
        <SubjectsComp></SubjectsComp>
        <!-- subjects -->
        
    </div>

</template>
<script>
import NavBar from '../components/NavBar.vue';
import SubjectsComp from '../components/subjects.vue';
export default ({
    name: "LoginComp",
    data() {
        return {
            
            username:"",
            userrole:""
        }
    },
    mounted(){
    },
    components:{
        NavBar,
        SubjectsComp
    }

})

</script>
