import { writable } from "svelte/store";

export const chessDone = writable(false);
export const chessMove = writable("");
export const showInstructions = writable(true);
export const gameOver = writable(false);
export const gameWon = writable(false);
