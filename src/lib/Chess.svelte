<script>
    import { Chessground } from "svelte-chessground";
    import { Chess, SQUARES } from "chess.js";
    import { onMount } from "svelte";
    import { chessMove, chessDone } from "../stores";

    export let fen;
    export let movesString;
    let firstChessMoveSubscribe = true;

    const chess = new Chess();
    let chessground;

    let chessMoveValue;
    chessMove.subscribe((value) => {
        console.log("value", value);
        chessMoveValue = value;

        if (!firstChessMoveSubscribe) {
            if (value === "") {
                console.log("Should reset");
                resetChessboard();
            }
        } else {
            firstChessMoveSubscribe = false;
        }
    });

    let chessDoneValue;
    chessDone.subscribe((value) => {
        chessDoneValue = value;

        if (value == true) {
            chessground.set({
                viewOnly: true,
            });
        }
    });

    // Find all legal moves
    function toDests(chess) {
        const dests = new Map();
        SQUARES.forEach((s) => {
            const ms = chess.moves({ square: s, verbose: true });
            if (ms.length)
                dests.set(
                    s,
                    ms.map((m) => m.to),
                );
        });
        return dests;
    }

    // Play a move and toggle whose turn it is
    function moved(chessground, chess) {
        return (orig, dest) => {
            let moved = chess.move({ from: orig, to: dest });
            console.log(moved);
            const color = chess.turn() == "w" ? "white" : "black";
            chessground.set({
                turnColor: color,
                viewOnly: true,
            });

            chessMove.set(moved.from + moved.to);
        };
    }

    //let fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
    // let fen = "5rk1/1p3ppp/pq3b2/8/8/1P1Q1N2/P4PPP/3R2K1 w - - 2 27";
    let fenSplit = fen.split(" ");
    let computerMove = fenSplit[1];
    // The opponent moves first, so the user is the opposite color
    let orientation = computerMove === "w" ? "black" : "white";
    //let movesString = "d3d6 f8d8 d6d8 f6d8";
    let moves = movesString.split(" ");

    function resetChessboard() {
        chessground.set({
            viewOnly: false,
            fen: fen,
            orientation: orientation,
        });
        chess.load(fen);

        let origin = moves[0].slice(0, 2);
        let dest = moves[0].slice(2, 4);

        chess.move({ from: origin, to: dest });
        chessground.move(origin, dest);

        const color = chess.turn() === "w" ? "white" : "black";
        chessground.set({
            turnColor: color,
            movable: {
                color: color,
                dests: toDests(chess),
                free: false,
            },
        });

        chessMove.set("");
    }

    function undo() {
        resetChessboard();
    }

    onMount(async () => {
        chessground.set({
            movable: { events: { after: moved(chessground, chess) } },
        });
        resetChessboard();
    });
</script>

<div class="chess">
    <Chessground bind:this={chessground} />
</div>
<button on:click={undo} disabled={chessDoneValue}>Undo</button>

<style>
</style>
