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
                    <div class="form-floating">
                        <input type="text" v-model="quiz.description" class="form-control" id="floatingPassword"
                            placeholder="Password">
                        <label for="floatingPassword">Description</label>
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
                                    <button class="btn btn-primary" @click="openeditquestion(index)"><i class="bi bi-pen"></i></button>
                                    <button class="btn btn-primary" @click="removequestion(index)"><i class="bi bi-trash"></i></button>
                                </div>
                            </div>

                            <div class="d-flex gap-2 text-muted">
                                <p>A: {{ question.A }}</p>
                                <p>B: {{ question.B }}</p>
                                <p>C: {{ question.C }}</p>
                                <p>C: {{ question.D }}</p>

                            </div>
                            <div class="d-flex gap-2">
                                <p>Correct : {{question.correct}}</p>
                            </div>
                        </div>


                    </div>
                    <button @click="openquestionmodal" class="btn btn-primary mt-3" data-bs-toggle="modal"
                        data-bs-target="#questionModal"><i class="bi bi-plus"></i>Add New Question</button>
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
                    <h1 class="modal-title fs-5" id="exampleModalLabel">{{questioneditmode?'Edit Question' :'Create Question'}}</h1>
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


                    <button class="btn btn-primary" @click="questioneditmode ? editquestion() : createquestion()"> {{questioneditmode? 'Edit' :  "Add"}}</button>
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
                description: "",
                questions: [
                    
                ]
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
            questioneditmode:false

        }
    },
    methods: {
        editquestion(){
        
            this.quiz.questions[this.question.index] = {... this.question}
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
            this.questioneditmode=false
        },
        removequestion(index){
            this.quiz.questions.splice(index , 1)
        },
        openeditquestion(index){
            this.question = {... this.quiz.questions[index]}
            this.question.index=index
            this.questioneditmode = true
            this.openquestionmodal()
        },
        closequestionmodel() {

            const modalElement = document.getElementById('questionModal');
            const modal = window.bootstrap.Modal.getInstance(modalElement);
            const backdrop = document.querySelector('.modal-backdrop');
            if (backdrop) {
                backdrop.remove();
            }


            modal.hide();


        },
        openquestionmodal() {
            const questionModal = new window.bootstrap.Modal(document.getElementById('questionModal'))
            questionModal.show()
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

        }
    }
})
</script>