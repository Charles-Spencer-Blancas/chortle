<script>
    export let letter;
    export let status;
</script>

<div
    class:green={status === 2}
    class:yellow={status === 1}
    class:gray={status === 0}
>
    {letter}
</div>

<style>
    div {
        width: 2rem;
        height: 2rem;
        border-style: solid;
        font-size: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .green {
        background-color: green;
    }

    .yellow {
        background-color: yellow;
    }

    .gray {
        background-color: gray;
    }
</style>
