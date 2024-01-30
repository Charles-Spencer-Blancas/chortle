<script>
    export let show;
</script>

<div class="card" style:display={show ? "block" : "none"}>
    <slot />
</div>

<style>
    .card {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 100;
        background-color: var(--main);
        color: var(--text);
        border-radius: 10px;
    }
</style>
