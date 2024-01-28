<script>
    import Tile from "./Tile.svelte";

    export let status;
    export let word;
    export let chessGuess;
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

    <Tile
        letter={chessGuess[0] || ""}
        status={status.length === 0 ? -1 : status[5]}
    />
    <Tile
        letter={chessGuess[1] || ""}
        status={status.length === 0 ? -1 : status[6]}
    />
    <Tile
        letter={chessGuess[2] || ""}
        status={status.length === 0 ? -1 : status[7]}
    />
    <Tile
        letter={chessGuess[3] || ""}
        status={status.length === 0 ? -1 : status[8]}
    />
    <Tile
        letter={chessGuess[4] || ""}
        status={status.length === 0 ? -1 : status[9]}
    />
</div>

<style>
    .tiles {
        display: flex;
        gap: 0.5em;
    }
</style>
