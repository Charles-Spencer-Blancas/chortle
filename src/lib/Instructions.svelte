<script>
    import Modal from "./Modal.svelte";
    import { showInstructions } from "../stores";

    let showInstructionsValue;
    showInstructions.subscribe((value) => {
        showInstructionsValue = value;
    });

    let closeInstructions = () => {
        showInstructions.set(false);
    };
</script>

<Modal show={showInstructionsValue}>
    <h1>Instructions</h1>
    <h4>Guess the word and find the best chess move in 5 moves</h4>

    <ol>
        <li>Green means the symbol is in the right place</li>
        <li>Yellow means the symbol is in another spot</li>
        <li>Gray means the symbol is not there</li>
        <li>At least one letter in the best move is in the word</li>
    </ol>

    <button on:click={closeInstructions}>Understood</button>
</Modal>
