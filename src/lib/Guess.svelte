<script>
    import Tile from "./Tile.svelte";

    export let status;
    export let word;
</script>

<div class="tiles">
    <Tile letter={word[0] || ""} />
    <Tile letter={word[1] || ""} />
    <Tile letter={word[2] || ""} />
    <Tile letter={word[3] || ""} />
    <Tile letter={word[4] || ""} />
</div>

<style>
    .tiles {
        display: flex;
    }
</style>
