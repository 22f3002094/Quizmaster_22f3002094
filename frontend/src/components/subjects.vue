<template>
    <!-- <div v-if="openform === true">
        <subjectform @formhandler="handleformevent"></subjectform>
    </div> -->
    <div v-if="message" class="alert alert-primary" role="alert">
        {{ message }}
    </div>

    <div class="card ms-5 me-5 mt-5 shadow-lg">
        <div class="card-header d-flex">
            <h3>Subjects</h3>

            <router-link to="create/subject" class="btn btn-primary ms-auto"><i class="bi bi-patch-plus"></i>
Create</router-link>
        </div>
        <div class="card-body">
            <div class="row">

                <div class="col-3  " v-for="sub in subjects" :key="sub.id">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">{{ sub.name }}</h5>
                            <div>
                                <button class="btn btn-primary" @click="editsubject(sub)"><i class="bi bi-pen"></i></button>
                                <button class="btn btn-primary ms-2 " @click="delsubject(sub.id)"><i class="bi bi-trash"></i></button> 
                                <router-link :to="`/admin/subject/${sub.name}`" class="btn btn-primary ms-2">Go to chapter</router-link>
                            </div>
                        </div>
                    </div>
                </div>



            </div>

        </div>
    </div>

</template>
<script>

export default ({
    name: "SubjectsComp",
    data() {
        return {
            subjects: [],
            openform: false,
            message: "",
            greetmessage : "Hello"

        }
    },
    methods: {
        async delsubject(id){
            const token = localStorage.getItem("token")
            try{
                const response = await fetch(`http://127.0.0.1:5000/api/subjects?id=${id}`, {
                    method: "DELETE",
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': token
                    },

                },)
                const data = await response.json()
                if(response.status==200){
                    this.message=data.message
                    this.fetchsubject()
                }
                else{
                    new Error()
                }


            }
            catch(e){
                this.message="something went worng, try again"
            }
        },

        editsubject(subject){
            localStorage.setItem("subject" , JSON.stringify(subject))
            this.$router.push({path:"edit/subject"  })

        },

        
        async fetchsubject() {
            const token = localStorage.getItem("token")
            const response = await fetch("http://127.0.0.1:5000/api/subjects", {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Authentication-Token': token
                }
            },)
            const data = await response.json()
            if (response.status === 200) {
                this.subjects = data
            }
            else if (response.status === 401) {
                this.$router.push('/login')
            }

        }
    },
    async mounted() {
        this.fetchsubject()
    },
    
})

</script>