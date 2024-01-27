<script>
    import Guess from "./Guess.svelte";
    let currentGuess = "";

    let onKeyDown = (e) => {
        let key = e.key;
        let regex = new RegExp("^[A-Za-z]$");

        if (regex.test(key)) {
            console.log(key);
            return;
        }

        if (key == "Backspace") {
            console.log("backspace");
            return;
        }
    };
</script>

<Guess />
<Guess />
<Guess />
<Guess />
<Guess />

<svelte:window on:keydown|preventDefault={onKeyDown} />
