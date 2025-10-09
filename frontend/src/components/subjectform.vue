<template>
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
            this.$store.dispatch("createSubject" ,this.formdata)
            this.$emit("closetheform")
        }
    }

})

</script>
