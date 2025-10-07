<template>
    <div class="card ms-auto me-auto mt-3" style="width:50%">
        <div class="card-body">
            <div class="form-floating mb-3">
                <input type="text" v-model="formdata.name" class="form-control" id="floatingInput">
                <label for="floatingInput">Chapter Name</label>
            </div>
            <div class="form-floating">
                <input type="text" v-model="formdata.description" class="form-control" id="floatingPassword"
                    placeholder="Password">
                <label for="floatingPassword">Description</label>
            </div>
            <button class="btn btn-primary mt-3" @click="submit">Submit</button>

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
            }
        }
    },
    methods: {
        async submit() {
            console.log(this.formdata)
            const token = localStorage.getItem("token")
            try{
                const response = await fetch(`http://127.0.0.1:5000/api/chapters?sub_name=${this.$route.params.subname}`, {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': token
                    },
                    body: JSON.stringify(this.formdata)

                },)
                const data = await response.json()
                console.log(data)

                this.$emit("formhandler", response.status, data.message)
            }
            catch(e){
                this.$emit("formhandler", 500, e.message)
            }


        }
    }

})

</script>
