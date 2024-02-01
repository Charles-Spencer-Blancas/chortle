<script>
    export let show;
    export let fromTop = "50%";
</script>

<div class="card" style:display={show ? "block" : "none"} style:top={fromTop}>
    <slot />
</div>

<style>
    .card {
        position: fixed;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 100;
        background-color: var(--main);
        color: var(--text);
        border-radius: 10px;
    }
</style>
