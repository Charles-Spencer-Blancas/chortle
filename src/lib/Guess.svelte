<script>
    import Tile from "./Tile.svelte";

    export let status;
    export let word;
</script>

<div class="tiles">
    <Tile
        letter={word[0] || ""}
        status={status.length === 0 ? -1 : status[0]}
    />
    <Tile
        letter={word[1] || ""}
        status={status.length === 0 ? -1 : status[1]}
    />
    <Tile
        letter={word[2] || ""}
        status={status.length === 0 ? -1 : status[2]}
    />
    <Tile
        letter={word[3] || ""}
        status={status.length === 0 ? -1 : status[3]}
    />
    <Tile
        letter={word[4] || ""}
        status={status.length === 0 ? -1 : status[4]}
    />
</div>

<style>
    .tiles {
        display: flex;
        gap: 0.5em;
    }
</style>
