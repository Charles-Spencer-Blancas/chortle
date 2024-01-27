<script>
    import Guess from "./Guess.svelte";
    let guesses = ["", "", "", "", ""];
    let answer = "pigmy";
    let currentActive = 0;
    let gameOver = false;

    let onKeyDown = (e) => {
        let key = e.key;

        // Single alphabet character
        let regex = new RegExp("^[A-Za-z]$");

        if (regex.test(key)) {
            key = key.toUpperCase();
            if (guesses[currentActive].length < 5) {
                guesses[currentActive] = guesses[currentActive] + key;
            }
            return;
        }

        if (key == "Backspace") {
            if (guesses[currentActive].length > 0) {
                guesses[currentActive] = guesses[currentActive].slice(0, -1);
            }
            return;
        }

        if (key == "Enter") {
            submitGuess();
        }
    };

    let submitGuess = () => {
        if (currentActive === 4) {
            gameOver = true;
        }
        currentActive += 1;
    };
</script>

<Guess status={[]} word={guesses[0]} />
<Guess status={[]} word={guesses[1]} />
<Guess status={[]} word={guesses[2]} />
<Guess status={[]} word={guesses[3]} />
<Guess status={[]} word={guesses[4]} />

<svelte:window on:keydown|preventDefault={onKeyDown} />
