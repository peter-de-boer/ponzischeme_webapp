<template>
    <div id="log" ref="myid" class="log"> 
        <!--
            for flex-direction: column-reverse; need an additional div to get the scroll 
            down to bottom feature working 
            https://stackoverflow.com/questions/18614301/keep-overflow-div-scrolled-to-bottom-unless-user-scrolls-up
            
            but it appears the column-reverse does not work on all browsers (e.g firefox)
            so additional div is removed
            instead scrollTop=scrollHeight is used
            but that somehow does not work as is, seems to be related with rendering process 
            only with a sufficient timeout it works
        -->
            <h2> Log </h2>
            <!-- the log contains html code (e.g. for coloring the tile names) -->
            <div v-for="line in log" v-html="replaceTags(line)">  </div>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex';
    export default {
        data() {
            return {
                tags: { 
                    "<transporttag>":  "style='background-color:#5F7F9D; color:white'",
                    "<graintag>":      "style='background-color:#E1C908; color:black'",
                    "<mediatag>":      "style='background-color:#50A492; color:white'",
                    "<realestatetag>": "style='background-color:#A70909; color:white'"
                }
            }
        },
        mounted() {
            this.scrollToEnd()
        },
        computed: {
            ...mapGetters([
                'log',
                'gameStateLoaded'
            ])
        },
        methods: {
            scrollToEnd() {
              var self = this
              setTimeout(function() {
                var container = self.$refs["myid"];
                container.scrollTop = container.scrollHeight;
              },200)
            },
            replaceTags(line) {
                var newline = line;
                for (var key in this.tags) {
                    newline = newline.replace(key,this.tags[key])
                }
                return newline
            }
        }
    }    
</script>

<style scoped>

.log {
    border-style: solid;
    height: 350px;
    overflow: auto;
    /*
    display: flex;
    flex-direction: column-reverse;
    */
}

</style>
