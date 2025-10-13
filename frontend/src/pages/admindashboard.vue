<template>
    <div>
        <NavBar></NavBar>
        <!-- subjects -->
        <router-view></router-view>
        <button class="btn btn-warning" :disabled="isTrying" @click="export_csv">
            <div v-if="isTrying" class="spinner-border" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            Download
        </button>


    </div>

</template>
<script>
import NavBar from '../components/NavBar.vue';
export default ({
    name: "LoginComp",
    data() {
        return {

            username: "",
            userrole: "",
            isTrying: false
        }
    },
    mounted() {
    },
    components: {
        NavBar,
    },
    methods: {
        
        async export_csv() {
            const token = localStorage.getItem("token")
            const response = await fetch(`http://127.0.0.1:5000/api/admin_export_csv`, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Authentication-Token': token
                }
            },)
            const data = await response.json()
            if (response.status === 200) {
                if (data.task_id) {
                    let tid = data.task_id;
                    this.isTrying = true
                    let interval = setInterval(() => {
                        fetch(`http://127.0.0.1:5000/api/check_admin_export_csv?taskid=${tid}`, {
                            headers: {
                                "Authentication-Token": token
                            }
                        })
                            .then(response => {
                                if (response.status === 200) {
                                    clearInterval(interval);
                                    this.isTrying = false
                                    window.location.href = `http://127.0.0.1:5000/api/check_admin_export_csv?taskid=${tid}`;
                                } else {
                                    console.log("Task not ready yet, retrying...");
                                }
                            })
                            .catch(error => {
                                console.error("Error checking task status:", error);
                                clearInterval(interval);
                            });
                    }, 2000);
                }
            }
            else if (response.status === 401) {
                this.$router.push('/login')
            }
        }
    }

})

</script>

