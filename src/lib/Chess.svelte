<script>
    import { Chessground } from "svelte-chessground";
    import { Chess, SQUARES } from "chess.js";
    import { onMount } from "svelte";

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
    function playOtherSide(chessground, chess) {
        return (orig, dest) => {
            chess.move({ from: orig, to: dest });
            const color = chess.turn() == "w" ? "white" : "black";
            chessground.set({
                turnColor: color,
                movable: {
                    color: color,
                    dests: toDests(chess),
                },
            });
        };
    }

    let fen = "5rk1/1p3ppp/pq3b2/8/8/1P1Q1N2/P4PPP/3R2K1 w - - 2 27";
    let fenSplit = fen.split(" ");
    let computerMove = fenSplit[1];
    // The opponent moves first, so the user is the opposite color
    let orientation = computerMove === "w" ? "black" : "white";
    let movesString = "d3d6 f8d8 d6d8 f6d8";
    let moves = movesString.split(" ");

    const chess = new Chess();
    let chessground;

    let config = {
        fen: fen,
        movable: {
            color: "white",
            free: false,
            dests: toDests(chess),
        },
    };

    onMount(async () => {
        chessground.set({
            orientation: orientation,
            movable: { events: { after: playOtherSide(chessground, chess) } },
        });
        chess.load(fen);
        let origin = moves[0].slice(0, 2);
        let dest = moves[0].slice(2, 4);
        chess.move({ from: origin, to: dest });
        chessground.move(origin, dest);

        const color = chess.turn() == "w" ? "white" : "black";
        chessground.set({
            turnColor: color,
            movable: {
                color: color,
                dests: toDests(chess),
            },
        });
    });
</script>

<Chessground bind:this={chessground} {config} />
