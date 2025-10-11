<template>
    <div>
        <div v-if="message" class="alert alert-primary" role="alert">
            {{ message }}
        </div>
        <div class="container">

            <div class="card ms-auto me-auto mt-3" style="width:50%">

                <div class="card-body p-3">
                    <h4>Quiz Details</h4>

                    <div class="form-floating mb-3">
                        <input type="text" v-model="quiz.name" class="form-control" id="floatingInput">
                        <label for="floatingInput">Quiz Name</label>
                    </div>
                </div>
            </div>
            <div class="card ms-auto me-auto mt-3" style="width:50%">
                <div class="card-body">
                    <h4>Questions</h4>
                    <div v-for="question, index in quiz.questions" :key="question" class="card mb-3">
                        <div class="card-body">
                            <div class="d-flex">
                                <h5>Q.{{ index + 1 }} {{ question.statement }}</h5>
                                <div class="ms-auto d-flex gap-2">
                                    <button class="btn btn-primary" @click="openeditquestion(index)"><i
                                            class="bi bi-pen"></i></button>
                                    <button class="btn btn-primary" @click="removequestion(index)"><i
                                            class="bi bi-trash"></i></button>
                                </div>
                            </div>

                            <div class="d-flex gap-2 text-muted">
                                <p>A: {{ question.A }}</p>
                                <p>B: {{ question.B }}</p>
                                <p>C: {{ question.C }}</p>
                                <p>C: {{ question.D }}</p>

                            </div>
                            <div class="d-flex gap-2">
                                <p>Correct : {{ question.correct }}</p>
                            </div>
                        </div>


                    </div>
                    <button @click="openquestionmodal" class="btn btn-primary mt-3"><i class="bi bi-plus"></i>Add New
                        Question</button>
                </div>

            </div>
            <div class="card  ms-auto me-auto   mt-3" style="width:50%">
                <div class="card-body">
                    <h4>Quiz Date</h4>
                    <div class="form-floating mb-3 ">
                        <input type="date" v-model="quiz.date" class="form-control" id="floatingInput">
                        <label for="floatingInput">Date</label>
                    </div>

                </div>
            </div>

            <div class="d-flex mt-2 mb-3">
                <button class="btn btn-primary mx-auto" @click="createquiz">
                    Create Quiz
                </button>
            </div>

        </div>
    </div>




    <div class="modal fade" id="questionModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">
                        {{ questioneditmode ? 'Edit Question' : 'Create Question' }}</h1>
                    <button type="button" @click="closequestionmodel" class="btn-close"></button>
                </div>
                <div class="modal-body">
                    <div class="form-floating mb-3">
                        <input type="text" v-model="question.statement" class="form-control" id="floatingInput">
                        <label for="floatingInput">Statement</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" v-model="question.A" class="form-control" id="floatingPassword">
                        <label for="floatingPassword">Option 1</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" v-model="question.B" class="form-control" id="floatingPassword">
                        <label for="floatingPassword">Option 2</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" v-model="question.C" class="form-control" id="floatingPassword">
                        <label for="floatingPassword">Option 3</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" v-model="question.D" class="form-control" id="floatingPassword">
                        <label for="floatingPassword">Option 4</label>
                    </div>

                    <div class="form-floating mb-3">
                        <input type="text" v-model="question.correct" class="form-control" id="floatingPassword">
                        <label for="floatingPassword">Correct option</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" v-model="question.marks" class="form-control" id="floatingPassword">
                        <label for="floatingPassword">Marks</label>
                    </div>


                    <button class="btn btn-primary" @click="questioneditmode ? editquestion() : createquestion()">
                        {{ questioneditmode ? 'Edit' : "Add" }}</button>
                </div>

            </div>
        </div>
    </div>

</template>
<script>
export default ({
    name: "FormquizComp",
    data() {
        return {
            message: "",
            quiz: {
                name: "",
            
                questions: [

                ],
                date:""
            },
            chapname: this.$route.params.chapname,
            question: {

                "statement": "",
                "A": "",
                "B": "",
                "C": "",
                "D": "",
                "correct": "",
                "marks": "",
            },
            questioneditmode: false,
            modelInstance: null,


        }
    },
    methods: {
        editquestion() {

            this.quiz.questions[this.question.index] = { ... this.question }
            this.closequestionmodel()
            this.question = {
                "statement": "",
                "A": "",
                "B": "",
                "C": "",
                "D": "",
                "correct": "",
                "marks": "",
            }
            this.questioneditmode = false
        },
        removequestion(index) {
            this.quiz.questions.splice(index, 1)
        },
        openeditquestion(index) {
            this.question = { ... this.quiz.questions[index] }
            this.question.index = index
            this.questioneditmode = true
            this.openquestionmodal()
        },
        closequestionmodel() {

            this.modelInstance.hide()
            const backdrop = document.querySelector('.modal-backdrop');
            if (backdrop) {
                backdrop.remove();
            }


            this.modelInstance.hide();


        },
        openquestionmodal() {
            this.modelInstance = new window.bootstrap.Modal(document.getElementById('questionModal'))
            this.modelInstance.show()
        },
        createquestion() {
            this.quiz.questions.push(this.question)
            this.question = {
                "statement": "",
                "A": "",
                "B": "",
                "C": "",
                "D": "",
                "correct": "",
                "marks": "",
            }
            this.closequestionmodel()

        },
        async createquiz() {
            
            if (!this.quiz.name || !this.quiz.date) {
                this.message = "Please fill out the Quiz Name and Date.";
                return;
            }
            if (this.quiz.questions.length === 0) {
                this.message = "A quiz must have at least one question.";
                return;
            }
            const apiUrl = `http://127.0.0.1:5000/api/quizes?ch_name=${this.chapname}`;

            const payload = {
                quiz_name: this.quiz.name,
                quiz_date: this.quiz.date,
                questions: this.quiz.questions
            };
            try {
                const token = localStorage.getItem("token")
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': token
                    },
                    body: JSON.stringify(payload)
                });

                const responseData = await response.json();

                if (!response.ok) {
                    throw new Error(responseData.message || `An error occurred: ${response.statusText}`);
                }



                this.message = "Quiz created successfully!";


                setTimeout(() => {
                    this.$router.push(`/admin/chapter/${this.chapname}`); 
                }, 2000);

            } catch (error) {
               
                console.error('Failed to create quiz:', error);
                
                this.message = error.message;
            } 
        }
    }
})
</script>