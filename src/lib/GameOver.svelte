<script>
    import Modal from "./Modal.svelte";
    import { gameOver } from "../stores";

    export let word;
    export let move;

    let gameOverValue;
    gameOver.subscribe((value) => {
        gameOverValue = value;
    });
</script>

<Modal show={gameOverValue}>
    <h1>Game Over</h1>
    <h4>The answer was {word} and {move}</h4>
</Modal>
