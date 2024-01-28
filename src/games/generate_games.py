import random

game_filename = "shorter_games.csv"
word_filename = "answerlist.txt"
out_filename = "output.js"

word_file = open(word_filename, "r")
words = word_file.read().split("\n")

game_file = open(game_filename, "r")
games = game_file.read().split("\n")

out_file = open(out_filename, "w")
out_file.write("let games = [")


def get_fen_and_moves(line):
    splitted = line.split(",")
    return splitted[1], splitted[2]


def random_valid_word(letters, words):
    possible = []
    for word in words:
        if letters[0] in word and letters[1] in word:
            possible += [word]

    return random.choice(possible)


for game in games:
    fen, moves_string = get_fen_and_moves(game)
    moves = moves_string.split(" ")
    valid_letters = [moves[1][0], moves[1][2]]

    word = random_valid_word(valid_letters, words)

    out_file.write(str({"fen": fen, "moves": moves_string, "word": word}))
    out_file.write(",\n")

out_file.write("]")
