<template>
    <!-- <div v-if="openform === true">
        <subjectform @formhandler="handleformevent"></subjectform>
    </div> -->
    <div v-if="message" class="alert alert-primary" role="alert">
        {{ message }}
    </div>

    <div class="card ms-5 me-5 mt-5 shadow-lg">
        <div class="card-header d-flex">
            <h3>{{chapname}} - Quizes</h3>

            <router-link to="/admin/create/quiz" class="btn btn-primary ms-auto"><i class="bi bi-patch-plus"></i>
Create</router-link>
        </div>
        <div class="card-body">
            <div class="row">

                <div class="col-3  " v-for="quiz in quizes" :key="quiz.id">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">{{ quiz.name }}</h5>
                            <div>
                                <button class="btn btn-primary" @click="editquiz(quiz)"><i class="bi bi-pen"></i></button>
                                <button class="btn btn-primary ms-2 " @click="delquiz(sub.id)"><i class="bi bi-trash"></i></button> 
                                <!-- <router-link :to="`/admin/subject/${sub.name}`" class="btn btn-primary ms-2">Go to chapter</router-link> -->
                            </div>
                        </div>
                    </div>
                </div>



            </div>

        </div>
    </div>

</template>
<script>
export default({
    name:"QuizesComp" , 
    data(){
        return {
            message:"",
            quizes:[],
            chapname : this.$route.params.chapname
        }
    }
})
</script>