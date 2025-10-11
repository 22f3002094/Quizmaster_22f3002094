<template>
    <div class="container my-5">
        <div v-if="quiz">
            <div class="text-center">
                <h2>{{ quiz?.name }}</h2>
                <h5>Total Marks : {{ quiz?.total_marks }}</h5>
            </div>

            <div v-for="question, index in quiz.questions" class="card" :key="index">
                <div class="card-body p-3">
                    <div class="d-flex fs-4 ">
                        <h5>Q.{{ index + 1 }} {{ question.statement }}</h5>
                        <p class="text-muted ms-auto "> Marks: {{ question.marks }} </p>

                    </div>

                    <div class="fs-5 p-3">
                        <div class="form-check">
                            <input class="form-check-input" v-model="user_response[index]" value="A" type="radio" name="radioDefault" id="radioDefault1">
                            <label class="form-check-label" for="radioDefault1">
                                {{ question.A }}
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" v-model="user_response[index]" value="B" type="radio" name="radioDefault" id="radioDefault2">
                            <label class="form-check-label" for="radioDefault2">
                                {{ question.B }}
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" v-model="user_response[index]" value="C"  type="radio" name="radioDefault" id="radioDefault3">
                            <label class="form-check-label" for="radioDefault3">
                                {{ question.C }}
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" v-model="user_response[index]" value="D"  type="radio" name="radioDefault" id="radioDefault4">
                            <label class="form-check-label" for="radioDefault4">
                                {{ question.D }}
                            </label>
                        </div>
                    </div>



                </div>

            </div>
            <button class="btn btn-primary mt-5" @click="submitquiz">Submit</button>

        </div>
        <div v-else class="text-center">
            <p>Error fetching quizes</p>
        </div>


    </div>
</template>
<script>
export default ({
    name: "QuizAttempComp",
    data() {
        return {
            quiz: null,
            user_response: []
        }
    },
    async mounted() {
        const token = localStorage.getItem("token")
        const response = await fetch(`http://127.0.0.1:5000/api/quizes?id=${this.$route.params.quizid}`, {
            method: "GET",
            headers: {
                'Content-Type': 'application/json',
                'Authentication-Token': token
            }
        },)
        const data = await response.json()
        if (response.status === 200) {
            this.quiz = data
            const noofquestion = this.quiz.questions.length
            
            for (let i = 0; i < noofquestion; i++) {
                this.user_response.push("")
            }
            
        }
        else if (response.status === 404) {
            this.$router.push("/student/dashboard")
        }
        else if (response.status === 401) {
            this.$router.push('/login')
        }
    },
    methods:{
        submitquiz(){
            console.log(this.user_response)
        }
    }

})
</script>