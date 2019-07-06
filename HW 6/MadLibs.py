# This program has multiple functions. It can create a Mad-Lib based on an existent
# input file, which is replacing some words that start with '<' and end with '>' by some
# specific words. Then the program also can print some existent file if the user chooses
# to view the file. The program will keep running until the user calls stop.

# Import the os package such that we can test whether the file exist or not.
import os

# This function can detect whether the input file exists or not. The program will
# keep running until the user use the exist input file. this function returns
# the name of the input file.
def find_input_file():
    input_file = input("Input file name: ")
    while not os.path.isfile(input_file):
        input_file = input("File not found. Try again: ")
    return input_file

# This function can detect any words that starts with < and end with > and change it
# to some specific word. Finally, it will generate an output file and store it in the path.
def create():
    input_file = find_input_file()
    output_file = input("Output file name: ")
    opened_file = open(input_file, 'r')
    opened_output = open(output_file, 'w+')
    for line in opened_file:
        # If the input file has a blank line, then the output file should also has a blank line.
        if line == '\n':
            opened_output.write('\n \n')
        for word in line.split():
            if word.startswith('<') and word.endswith('>'):
                # Choose whether use 'a' or 'an'.
                replaced_word = word.replace('-', ' ')
                if word[1] == 'a' or word[1] == 'e' or word[1] == 'i' \
                or word[1] == 'o' or word[1] == 'u':
                    typed_word = input("Please type an " + replaced_word[1:len(word)-1] + ": ")
                else:
                    typed_word = input("Please type a " + replaced_word[1:len(word)-1] + ": ")
                word = typed_word
            opened_output.write(word + ' ')
    print("Your mad-lib has been created!")
    print()

# This function can view some exist file in the path. By putting the file name as the input,
# the output will generate the details in the input file.
def view():
    input_file = find_input_file()
    print()
    opened_file = open(input_file, 'r')
    print(opened_file.read())
    print()

# The beginning section of the whole program.
print("Welcome to the game of Mad Libs.")
print("I will ask you to provide various words")
print("and phrases to fill in a story.")
print("The result will be written to an output file.")
print()

# Keep running the program until the user want to quit.
while True:
    choice = input("(C)reate mad-libs, (V)iew mad-lib, (Q)uit? ")
    if choice == 'C' or choice == 'c':
        create()
    elif choice == 'V' or choice == 'v':
        view()
    elif choice == 'Q' or choice == 'q':
        break
    else:
        continue
