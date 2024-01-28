<script>
    import Chess from "./Chess.svelte";
    import Guess from "./Guess.svelte";
    import { chessMove, chessDone, gameOver } from "../stores";
    import Instructions from "./Instructions.svelte";
    import GameOver from "./GameOver.svelte";

    let wordGuesses = ["", "", "", "", ""];
    let chessGuesses = ["", "", "", "", ""];
    let statuses = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ];
    let chessStatuses = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ];

    let chessDoneValue;
    chessDone.subscribe((value) => {
        chessDoneValue = value;
    });

    let answer = "DREAM";
    let chessAnswer = "f8d8";
    let currentActive = 0;

    let gameOverValue;
    gameOver.subscribe((value) => {
        gameOverValue = value;
    });

    let chessMoveValue;
    chessMove.subscribe((value) => {
        chessMoveValue = value;
        chessGuesses[currentActive] = value;
    });

    let onKeyDown = (e) => {
        let key = e.key;

        // Single alphabet character
        let regex = new RegExp("^[A-Za-z]$");

        if (regex.test(key)) {
            key = key.toUpperCase();
            if (wordGuesses[currentActive].length < 5) {
                wordGuesses[currentActive] = wordGuesses[currentActive] + key;
            }
            return;
        }

        if (key == "Backspace") {
            if (wordGuesses[currentActive].length > 0) {
                wordGuesses[currentActive] = wordGuesses[currentActive].slice(
                    0,
                    -1,
                );
            }
            return;
        }

        if (key == "Enter") {
            if (
                wordGuesses[currentActive].length === 5 &&
                chessMoveValue != ""
            ) {
                submitGuess();
            }
        }
    };

    let compareWithAnswer = (guess, chessGuess) => {
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

        if (chessDoneValue) {
            chessGuess = chessAnswer;
        }

        for (let i = 0; i < chessGuess.length; i++) {
            if (chessGuess[i] === chessAnswer[i]) {
                out[i + 5] = 2;
                continue;
            }

            if (chessAnswer.includes(chessGuess[i])) {
                out[i + 5] = 1;
                continue;
            }

            out[i + 5] = 0;
        }

        for (let i = currentActive; i < chessGuess.length; i++) {
            if (out[i + 5] !== 2) {
                return out;
            }
        }

        chessDone.set(true);

        return out;
    };

    let checkWin = (comparison) => {
        for (let i = 0; i < comparison.length; i++) {
            if (comparison[i] !== 2) {
                return false;
            }
        }

        return true;
    };

    let submitGuess = () => {
        let comparison = compareWithAnswer(
            wordGuesses[currentActive],
            chessMoveValue,
        );

        statuses[currentActive] = comparison.slice(0, 5);
        chessStatuses[currentActive] = comparison.slice(5);

        if (checkWin(comparison)) {
            gameOver.set(true);
            return;
        }

        if (currentActive === 4) {
            gameOver.set(true);
            return;
        }

        currentActive += 1;

        if (chessDoneValue) {
            chessGuesses[currentActive] = chessAnswer;
            chessStatuses[currentActive] = [2, 2, 2, 2];
        } else {
            chessMove.set("");
        }
    };
</script>

<Instructions />
<GameOver word={answer} move={chessAnswer} {statuses} {chessStatuses} />
<Chess />
<div class="guesses">
    <Guess
        status={statuses[0]}
        chessStatus={chessStatuses[0]}
        word={wordGuesses[0]}
        chessGuess={chessGuesses[0]}
    />
    <Guess
        status={statuses[1]}
        chessStatus={chessStatuses[1]}
        word={wordGuesses[1]}
        chessGuess={chessGuesses[1]}
    />
    <Guess
        status={statuses[2]}
        chessStatus={chessStatuses[2]}
        word={wordGuesses[2]}
        chessGuess={chessGuesses[2]}
    />
    <Guess
        status={statuses[3]}
        chessStatus={chessStatuses[3]}
        word={wordGuesses[3]}
        chessGuess={chessGuesses[3]}
    />
    <Guess
        status={statuses[4]}
        chessStatus={chessStatuses[4]}
        word={wordGuesses[4]}
        chessGuess={chessGuesses[4]}
    />
</div>
<svelte:window on:keydown={onKeyDown} />

<style>
    .guesses {
        display: flex;
        flex-direction: column;
        gap: 0.5em;
    }
</style>
