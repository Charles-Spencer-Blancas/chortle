<script>
    import Tile from "./Tile.svelte";

    export let status;
    export let chessStatus;
    export let word;
    export let chessGuess;
</script>

<div class="guess">
    <div class="tiles">
        <Tile letter={word[0] || ""} status={status[0]} />
        <Tile letter={word[1] || ""} status={status[1]} />
        <Tile letter={word[2] || ""} status={status[2]} />
        <Tile letter={word[3] || ""} status={status[3]} />
        <Tile letter={word[4] || ""} status={status[4]} />
    </div>
    <div class="tiles">
        <Tile letter={chessGuess[0] || ""} status={chessStatus[0]} />
        <Tile letter={chessGuess[1] || ""} status={chessStatus[1]} />
        <Tile letter={chessGuess[2] || ""} status={chessStatus[2]} />
        <Tile letter={chessGuess[3] || ""} status={chessStatus[3]} />
    </div>
</div>

<style>
    .guess {
        display: flex;
        gap: 0.5rem;
    }

    .tiles {
        display: flex;
        gap: 0.15rem;
    }
</style>
