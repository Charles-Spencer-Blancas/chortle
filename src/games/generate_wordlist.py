word_filename = "wordlist.txt"
out_filename = "possibilities.js"

word_file = open(word_filename, "r")
words = word_file.read().split("\n")

out_file = open(out_filename, "w")
out_file.write("export const possibilities =")
out_file.write(str(words))
out_file.write(";")
