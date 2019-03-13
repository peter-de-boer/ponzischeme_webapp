<template>
    <div>
        <div v-if="reset_status=='reset_password'" class="reset-form">
          <form @submit.prevent="onSubmit">
            <div class="input" :class="{invalid: change_status=='unequal_password'}">
              <label for="password">Password</label>
              <input
                      type="password"
                      id="password"
                      v-model="password">
            </div>
            <div class="input" :class="{invalid: change_status=='unequal_password'}">
              <label for="confirm-password">Confirm Password</label>
              <input
                      type="password"
                      id="confirm-password"
                      v-model="confirmPassword">
            </div>
            <div class="submit">
              <button type="submit">Submit</button>
            </div>
          </form>
        </div>
        <div v-if="change_status=='failed' || reset_status=='failed'">
            Something went wrong.
        </div>
        <div v-if="change_status=='unequal_password'">The passwords are different.</div>
        <div v-if="change_status=='changed'">Your password is changed. You can login again.</div>
        <div v-if="change_status=='wait'">Please wait...</div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        props: ['token'],
        data() { 
            return {
                password: '',
                confirmPassword: '',
                reset_status: '',
                change_status: ''
            }
        },
        created() {
            var json = {"token": this.token}
            // need to do put instead of get request, else json arg is not working somehow
            axios.post('/user/reset_password', json)
                .then( res => {
                    this.reset_status = res.data.status
                    this.token = res.data.token
                }, error => {
                    console.log(error)
                }); 
        },
        methods: {
            onSubmit () {
                if (this.password != this.confirmPassword) {
                    this.change_status = "unequal_password"
                } else {
                    this.change_status="wait"
                    axios.post('/user/change_password', {
                        password: this.password,
                        returnSecureToken: true,
                        token: this.token
                    })
                    .then(res => {
                        this.change_status = res.data.status
                    })
                    .catch(error => console.log(error))
                }
            }
        }
      }
</script>

<style scoped>
  .reset-form {
    width: 400px;
    margin: 30px auto;
    border: 1px solid #eee;
    padding: 20px;
    box-shadow: 0 2px 3px #ccc;
  }

  .input {
    margin: 10px auto;
  }

  .input label {
    display: block;
    color: #4e4e4e;
    margin-bottom: 6px;
  }

  .input.inline label {
    display: inline;
  }

  .input input {
    font: inherit;
    width: 100%;
    padding: 6px 12px;
    box-sizing: border-box;
    border: 1px solid #ccc;
  }

  .input.inline input {
    width: auto;
  }

  .input input:focus {
    outline: none;
    border: 1px solid #521751;
    background-color: #eee;
  }

  .input select {
    border: 1px solid #ccc;
    font: inherit;
  }

  .input.invalid input {
    border-style: solid;
    border-color: red;
  }

  .input.invalid label {
    color: red;
  }

  .submit button {
    border: 1px solid #521751;
    color: #521751;
    padding: 10px 20px;
    font: inherit;
    cursor: pointer;
  }

  .submit button:hover,
  .submit button:active {
    background-color: #521751;
    color: white;
  }

  .submit button[disabled],
  .submit button[disabled]:hover,
  .submit button[disabled]:active {
    border: 1px solid #ccc;
    background-color: transparent;
    color: #ccc;
    cursor: not-allowed;
  }

</style>
