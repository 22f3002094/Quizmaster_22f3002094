<template>
    <div v-if="message" class="alert alert-primary" role="alert">
        {{ message }}
    </div>

    <div class="card ms-auto me-auto mt-3" style="width:50%">
        <div class="card-body">
            <div class="form-floating mb-3">
                <input type="text" v-model="formdata.name" class="form-control" id="floatingInput">
                <label for="floatingInput">Subject Name</label>
            </div>
            <div class="form-floating">
                <input type="text" v-model="formdata.description" class="form-control" id="floatingPassword"
                    placeholder="Password">
                <label for="floatingPassword">Description</label>
            </div>
            <button class="btn btn-primary mt-3" @click="iseditMode ? edit() : submit()">{{ iseditMode ? 'Edit' : 'Create'
                }}</button>

        </div>
    </div>

</template>
<script>
export default ({
    name: "LoginComp",
    data() {
        return {
            formdata: {
                name: "",
                description: ""
            },
            message: "",
            iseditMode: false
        }
    },
    methods: {
        async submit() {
            console.log(this.formdata)
            const token = localStorage.getItem("token")
            try {
                const response = await fetch("http://127.0.0.1:5000/api/subjects", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': token
                    },
                    body: JSON.stringify(this.formdata)

                },)
                const data = await response.json()
                console.log(data)

                if (response.status === 200) {

                    this.$router.push("/admin/dashboard")

                }
                else if (response.status == 409) {

                    this.message = data.message
                }
                else if (response.status == 500) {

                    this.message = "Something went wrong, Try again"
                }
            }
            catch (e) {
                this.message = e.message
            }


        },
        async edit() {
            console.log(this.formdata)
            const token = localStorage.getItem("token")
            try {
                const response = await fetch(`http://127.0.0.1:5000/api/subjects?id=${this.formdata.id}`, {
                    method: "PUT",
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': token
                    },
                    body: JSON.stringify(this.formdata)

                },)
                const data = await response.json()
                console.log(data)

                if (response.status === 200) {
                    localStorage.removeItem("subject")

                    this.$router.push("/admin/dashboard")

                }
                else if (response.status == 409) {

                    this.message = data.message
                }
                else if (response.status == 404) {

                    this.$router.push("/admin/dashboard")
                }
            }
            catch (e) {
                this.message = e.message
            }

        }

    },
    mounted() {
        this.formdata = { ...JSON.parse(localStorage.getItem("subject")) }
        if (this.formdata.name) {
            this.iseditMode = true
        }
        console.log(this.formdata)



    },
    unmounted(){
        localStorage.removeItem("subject")
    }

})

</script>