<template>
    <div >
        <NavBar></NavBar>
        <!-- subjects -->
        <router-view></router-view>
        
    </div>

</template>
<script>
import NavBar from '../components/NavBar.vue';
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
    }

})

</script>
