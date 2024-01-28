import { writable } from "svelte/store";

export const chessDone = writable(false);
export const chessMove = writable("");
