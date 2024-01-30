<script>
    import { createEventDispatcher } from "svelte";
    import Key from "./Key.svelte";

    const topRow = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"];
    const middleRow = ["a", "s", "d", "f", "g", "h", "j", "k"];
    const bottomRow = ["Enter", "z", "x", "c", "v", "b", "n", "m", "Backspace"];
</script>

<div class="keyboard">
    <div class="row">
        {#each topRow as key}
            <Key {key} on:key />
        {/each}
    </div>
    <div class="row">
        {#each middleRow as key}
            <Key {key} on:key />
        {/each}
    </div>

    <div class="row">
        {#each bottomRow as key}
            <Key {key} on:key />
        {/each}
    </div>
</div>

<style>
    .row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.25rem;
    }

    .keyboard {
        padding: 2rem;
        position: fixed;
        bottom: 0px;
        left: 0px;
        background-color: var(--main);
        color: var(--text);
        width: 100vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 50;
    }
</style>
