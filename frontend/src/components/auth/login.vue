<template>
  <div id="login">
    <div class="login-form">
      <form @submit.prevent="onSubmit">
        <div class="input">
          <label for="username">Username</label>
          <input
                  type="text"
                  id="username"
                  autocomplete="username"
                  v-model="username">
        </div>
        <div class="input">
          <label for="password">Password</label>
          <input
                  type="password"
                  id="password"
                  autocomplete="current-password"
                  v-model="password">
        </div>
        <div v-if="authFailed" style="color:red">
            Wrong username and/or password!
        </div>
        <div class="submit">
          <button type="submit">Submit</button>
        </div>
        <router-link :to="{name: 'request_reset_password'}">Forgot Password?</router-link>
        <br>
        <router-link :to="{name: 'request_confirm_email'}">Still need to confirm your email-address?</router-link>
      </form>
    </div>
  </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';

    export default {
        data () {
            return {
                username: '',
                password: ''
            }
        },
        computed: {
            ...mapGetters([
                'authFailed'
            ])
        },
        beforeDestroy() {
            this.clearFailedStatus()
        },
        methods: {
            ...mapActions([
                'login',
                'clearFailedStatus'
            ]),
          onSubmit () {
              const formData = {
                  username: this.username,
                  password: this.password,
              }
            this.login(formData)
      }
    }
  }
</script>

<style scoped>
  .login-form {
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

  .input input {
    font: inherit;
    width: 100%;
    padding: 6px 12px;
    box-sizing: border-box;
    border: 1px solid #ccc;
  }

  .input input:focus {
    outline: none;
    border: 1px solid #521751;
    background-color: #eee;
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
