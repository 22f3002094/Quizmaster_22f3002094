<template>
    <div v-if="openform === true">  
        <subjectform @closetheform="closetheform"></subjectform>
    </div>
    <div v-if="errorMessage.text" class="alert alert-primary" role="alert">
        {{ errorMessage.text }}
    </div>

    <div class="card ms-5 me-5 mt-5 shadow-lg">
        <div class="card-header d-flex">
            <h3>Subjects</h3>

            <button class="btn btn-primary ms-auto" @click="opentheform"><i class="bi bi-patch-plus"></i>
                {{ openform ? "Close" : "Create" }}</button>
        </div>
        <div class="card-body">
            <div class="row">

                <div class="col-3  " v-for="sub in subjects" :key="sub.id">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">{{ sub.name }}</h5>
                            <div>
                                <button class="btn btn-primary"><i class="bi bi-pen"></i></button>
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
import subjectform from './subjectform.vue';
export default ({
    name: "SubjectsComp",
    data() {
        return {
            
            openform: false,
            message: "",
            greetmessage : "Hello"

        }
    },
    computed:{
        subjects(){
            return this.$store.getters.allSubjects
        },
        errorMessage(){
            return this.$store.getters.message
        }
    },
    methods: {
        async delsubject(id){
            this.$store.dispatch("deleteSubject" , id)
        },

        opentheform() {
            console.log("button clicked!!")
            this.openform = !this.openform
        },
        closetheform(){
            this.openform=false
        },

        handleformevent(sc, msg) {
            if (sc === 200) {
                this.openform = false
                this.message = msg
            }
            else if (sc == 409) {
                this.openform = false
                this.message = msg
            }
            else if (sc == 500) {
                this.openform = false
                this.message = "Something went wrong, Try again"
            }
            this.fetchsubject()

        },
        
    },
    async mounted() {
        await this.$store.dispatch("fetchSubjects")
    },
    components: {
        subjectform
    }
})

</script>
