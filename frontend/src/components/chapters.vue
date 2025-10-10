<template>
    <div v-if="openform === true">
        <chapterform @formhandler="handleformevent"></chapterform>
    </div>
    <div v-if="message" class="alert alert-primary" role="alert">
        {{ message }}
    </div>

    <div class="card ms-5 me-5 mt-5 shadow-lg">
        <div class="card-header d-flex">
            <h3>{{subname}} - Chapters</h3>

            <button class="btn btn-primary ms-auto" @click="opentheform"><i class="bi bi-patch-plus"></i>
                {{ openform ? "Close" : "Create" }}</button>
        </div>
        <div class="card-body">
            <div class="row">

                <div class="col-3  " v-for="chap in chapters" :key="chap.id">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">{{ chap.name }}</h5>
                            <div>
                                <button class="btn btn-primary"><i class="bi bi-pen"></i></button>
                                <button class="btn btn-primary ms-2" @click="delchapter(chap.id)"><i class="bi bi-trash"></i></button> 
                                <router-link :to="`/admin/chapter/${chap.name}`" class="btn btn-primary ms-2">Go to Quizzes</router-link>
                            </div>
                        </div>
                    </div>
                </div>



            </div>

        </div>
    </div>

</template>
<script>
import chapterform from './chapterform.vue';
export default ({
    name: "ChaptersComp",
    data() {
        return {
            chapters: [],
            openform: false,
            message: "",
            subname:""

        }
    },
    methods: {
        async delchapter(id){
            const token = localStorage.getItem("token")
            try{
                const response = await fetch(`http://127.0.0.1:5000/api/chapters?ch_id=${id}`, {
                    method: "DELETE",
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': token
                    },

                },)
                const data = await response.json()
                if(response.status==200){
                    this.message=data.message
                    this.fetchchapter()
                }
                else{
                    new Error()
                }


            }
            catch(e){
                this.message="something went worng, try again"
            }
        },

        opentheform() {
            console.log("button clicked!!")
            this.openform = !this.openform
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
            this.fetchchapter()

        },
        async fetchchapter() {
            const token = localStorage.getItem("token")
            const response = await fetch(`http://127.0.0.1:5000/api/chapters?sub_name=${this.subname}`, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Authentication-Token': token
                }
            },)
            const data = await response.json()
            if (response.status === 200) {
                this.chapters = data
                console.log(this.chapters)
            }
            else if (response.status === 401) {
                this.$router.push('/login')
            }

        }
    },
    async mounted() {
        this.subname = this.$route.params.subname
        this.fetchchapter()
    },
    components: {
        chapterform
    }
})

</script>
