<template>
    <div id="dashboard">
        <p v-if="email">Your email address: {{ email }}</p>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapGetters } from 'vuex';
    import { mapActions } from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'email'
            ])
        },
        methods: {
            ...mapActions([
                'fetchUser'
            ])
        },
        created () {
            this.fetchUser()
        }
    }
</script>

<style scoped>
</style>
