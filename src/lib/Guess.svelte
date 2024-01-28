<script>
    import Tile from "./Tile.svelte";

    export let status;
    export let word;
    export let chessGuess;
    export let chessDone;
    export let chessAnswer;
</script>

<div class="guess">
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
    <div class="tiles">
        <Tile
            letter={chessDone ? chessAnswer[0] : chessGuess[0] || ""}
            status={chessDone ? 2 : status.length === 0 ? -1 : status[5]}
        />
        <Tile
            letter={chessDone ? chessAnswer[1] : chessGuess[1] || ""}
            status={chessDone ? 2 : status.length === 0 ? -1 : status[6]}
        />
        <Tile
            letter={chessDone ? chessAnswer[2] : chessGuess[2] || ""}
            status={chessDone ? 2 : status.length === 0 ? -1 : status[7]}
        />
        <Tile
            letter={chessDone ? chessAnswer[3] : chessGuess[3] || ""}
            status={chessDone ? 2 : status.length === 0 ? -1 : status[8]}
        />
        <Tile
            letter={chessDone ? chessAnswer[4] : chessGuess[4] || ""}
            status={chessDone ? 2 : status.length === 0 ? -1 : status[9]}
        />
    </div>
</div>

<style>
    .guess {
        display: flex;
        gap: 2em;
    }

    .tiles {
        display: flex;
        gap: 0.5em;
    }
</style>
