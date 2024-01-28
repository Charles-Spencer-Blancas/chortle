game_filename = "shorter_games.csv"
word_filename = "answerlist.txt"

word_file = open(word_filename, "r")
words = word_file.read().split("\n")

game_file = open(game_filename, "r")
games = game_file.read().split("\n")


def get_fen_and_moves(line):
    splitted = line.split(",")
    return splitted[1], splitted[2]


fen, moves_string = get_fen_and_moves(games[1])
moves = moves_string.split(" ")
