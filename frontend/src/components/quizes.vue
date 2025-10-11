<template>
    <!-- <div v-if="openform === true">
        <subjectform @formhandler="handleformevent"></subjectform>
    </div> -->
    <div v-if="message" class="alert alert-primary" role="alert">
        {{ message }}
    </div>

    <div class="card ms-5 me-5 mt-5 shadow-lg">
        <div class="card-header d-flex">
            <h3>{{ chapname }} - Quizes</h3>

            <router-link v-if="role === 'admin'" :to="`/admin/${chapname}/create/quiz`" class="btn btn-primary ms-auto"><i
                    class="bi bi-patch-plus"></i>
                Create</router-link>
        </div>
        <div class="card-body">
            <div class="row">

                <div class="col-3  " v-for="quiz in quizes" :key="quiz.id">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">{{ quiz.name }}</h5>
                            <p>Date : {{ quiz.date }}</p>
                            <p>total_marks : {{ quiz.total_marks }}</p>
                            <div>
                                <button v-if="role === 'admin'" class="btn btn-primary" @click="editquiz(quiz)"><i
                                        class="bi bi-pen"></i></button>
                                <button v-if="role === 'admin'" class="btn btn-primary ms-2 " @click="delquiz(sub.id)"><i
                                        class="bi bi-trash"></i></button>
                                <!-- <router-link :to="`/admin/subject/${sub.name}`" class="btn btn-primary ms-2">Go to chapter</router-link> -->
                                <router-link :to="`/student/attemptquiz/${quiz.id}`" class="btn btn-primary " v-if="role === 'student'"
                                    :disabled="quiz.date != formatDate()"> Attempt</router-link>
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
    name: "QuizesComp",
    data() {
        return {
            message: "",
            quizes: [],
            chapname: this.$route.params.chapname,
            role: ''
        }
    },
    async mounted() {
        this.role = localStorage.getItem("role")
        this.fetchquizes()

    },
    methods: {
        formatDate() {
            const date = new Date()
            return date.toISOString().split("T")[0]
        },
        async fetchquizes() {
            const token = localStorage.getItem("token")
            const response = await fetch(`http://127.0.0.1:5000/api/quizes?ch_name=${this.chapname}`, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Authentication-Token': token
                }
            },)
            const data = await response.json()
            if (response.status === 200) {
                this.quizes = data
            }
            else if (response.status === 401) {
                this.$router.push('/login')
            }
        }
    }
})
</script>