<script>
    import svelteLogo from "./assets/svelte.svg";
    import WordGame from "./lib/WordGame.svelte";
    import viteLogo from "/vite.svg";
</script>

<main>
    <div>Chortle</div>
    <WordGame />
</main>

<style>
    .logo {
        height: 6em;
        padding: 1.5em;
        will-change: filter;
        transition: filter 300ms;
    }
    .logo:hover {
        filter: drop-shadow(0 0 2em #646cffaa);
    }
    .logo.svelte:hover {
        filter: drop-shadow(0 0 2em #ff3e00aa);
    }
    .read-the-docs {
        color: #888;
    }
</style>
