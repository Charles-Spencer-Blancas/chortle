<script>
    import Modal from "./Modal.svelte";
    export let message;
</script>

<Modal show={message != ""} fromTop="20%">
    {message}
</Modal>
