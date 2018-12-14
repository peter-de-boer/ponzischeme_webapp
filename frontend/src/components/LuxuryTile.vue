<template>
    <div class="tile" :class="hiLight(value, points, luxuryTiles[selectedLuxuryTile])">
        ${{value}} {{points}}
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';

    export default {
        props: ['value','points'],
        computed: {
            ...mapGetters([
                'luxuryTiles',
                'selectedLuxuryTile'
            ])    
        },
        methods: {
            hiLight(value,points, sel) {
                if (sel && sel.value==value && sel.points== points) {
                    return "hilight";
                } else {
                    return "nohilight";
                }
            }
        }
    }    
</script>

<style scoped>

.tile {
    border-style: inset;
    border-width: 2px;
    background-color: darkblue;
    font-size: 1.2em;
    font-weight: bold;
    text-align: center;
    text-shadow: -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white;
}

.hilight {
}

.nohilight {
    border-color: transparent;
}

</style>
