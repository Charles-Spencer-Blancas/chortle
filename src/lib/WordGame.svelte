<script>
    import Chess from "./Chess.svelte";
    import Guess from "./Guess.svelte";

    /* THIS IS THE WORDLE PART */
    let guesses = ["", "", "", "", ""];
    let statuses = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ];
    let answer = "PIGMY";
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
            if (guesses[currentActive].length === 5) {
                submitGuess();
            }
        }
    };

    let compareWithAnswer = (guess) => {
        let out = [];
        for (let i = 0; i < guess.length; i++) {
            if (guess[i] === answer[i]) {
                out[i] = 2;
                continue;
            }

            if (answer.includes(guess[i])) {
                out[i] = 1;
                continue;
            }

            out[i] = 0;
        }

        return out;
    };

    let submitGuess = () => {
        statuses[currentActive] = compareWithAnswer(guesses[currentActive]);
        if (currentActive === 4) {
            gameOver = true;
        }
        currentActive += 1;
    };
</script>

<Chess />
<div class="guesses">
    <Guess status={statuses[0]} word={guesses[0]} />
    <Guess status={statuses[1]} word={guesses[1]} />
    <Guess status={statuses[2]} word={guesses[2]} />
    <Guess status={statuses[3]} word={guesses[3]} />
    <Guess status={statuses[4]} word={guesses[4]} />
</div>
<svelte:window on:keydown={onKeyDown} />

<style>
    .guesses {
        display: flex;
        flex-direction: column;
        gap: 0.5em;
    }
</style>
