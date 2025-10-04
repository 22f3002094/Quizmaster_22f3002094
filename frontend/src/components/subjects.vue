<template>
    <div class="card ms-5 me-5 shadow-lg">
        <div class="card-header d-flex">
            <h3>Subjects</h3>
            <button class="btn btn-primary ms-auto"><i class="bi bi-patch-plus"></i> Create</button>
        </div>
        <div class="card-body">
            <div class="row">

                <div class="col-3  " v-for="sub in subjects" :key="sub.id">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">{{ sub.name }}</h5>
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
            subjects: []

        }
    },
    async mounted() {
        const token = localStorage.getItem("token");
        const response = await fetch("http://127.0.0.1:5000/api/subjects", {
            method: "GET",
            headers: {
                'Content-Type': 'application/json',
                'Authentication-Token': token
            }
        },)
        const data = await response.json()
        if (response.status === 200){
            this.subjects = data
        }
        else if (response.status === 401){
            this.$router.push('/login')
        }
    }
})

</script>
