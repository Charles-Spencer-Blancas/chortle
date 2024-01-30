<script>
    import { createEventDispatcher } from "svelte";

    export let key;

    const dispatch = createEventDispatcher();

    function sendKeyToKeyboard() {
        dispatch("key", {
            key,
        });
    }
</script>

<div class="key" on:click={sendKeyToKeyboard}>{key}</div>

<style>
    .key {
        border: solid;
        border-width: 1px;
        min-width: 1rem;
        padding: 0.25rem;
        margin-bottom: 0.5rem;
    }
</style>
