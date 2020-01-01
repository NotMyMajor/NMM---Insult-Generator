# Import proper libraries.
import os
import random
from random import randrange
import sys
import time

# Set file location and define vowels and menu options.
FILE_LOCATION_INSULTS = os.path.join(os.path.dirname(__file__), "../data/InsultWords.txt")
vowels = ["a", "e", "i", "o", "u"]
fast_slow_options = ["fast", "slow", "f", "s"]

# Import and format file.
def import_file():

    with open(FILE_LOCATION_INSULTS, "r") as fp:
        words = [line.strip().lower() for line in fp.readlines()]

    return words

# Makes the program print the strings slowly instead of super quickly.
def text_printer(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0.0" + str(randrange(3, 4, 3))
        seconds = float(seconds)
        time.sleep(seconds)

# Generates the actual insults based on the three available formats and randomly selected words.
def generate_insult(all_the_words, max_num, fast_slow_b):
    first_insult = all_the_words[random.randint(0, max_num)]
    second_insult = all_the_words[random.randint(0, max_num)]
    third_insult = all_the_words[random.randint(0, max_num)]

    if first_insult[0] in vowels:
        article_one = "an"
    else:
        article_one = "a"

    if third_insult[0] in vowels:
        article_two = "an"
    else:
        article_two = "a"

    choose = random.randint(1,3)
    if fast_slow_b == "slow" or fast_slow_b == "s":
        if choose == 1:
            text1 = "You {} {}. Go suck {} {}.\n".format(first_insult, second_insult, article_two, third_insult)
            text_printer(text1)
        elif choose == 2:
            text2 = "I am {} {} {}. My life is a pile of {}.\n".format(article_one, first_insult, second_insult, third_insult)
            text_printer(text2)
        elif choose == 3:
            third_insult = third_insult + "s"
            text3 = "Mankind is {} {} {}. They are all just {}.\n".format(article_one, first_insult, second_insult, third_insult)
            text_printer(text3)

    else:
        if choose == 1:
            print("You {} {}. Go suck {} {}.\n".format(first_insult, second_insult, article_two, third_insult))
        elif choose == 2:
            print("I am {} {} {}. My life is a pile of {}.\n".format(article_one, first_insult, second_insult, third_insult))
        elif choose == 3:
            third_insult = third_insult + "s"
            print("Mankind is {} {} {}. They are all just {}.\n".format(article_one, first_insult, second_insult, third_insult))

# Checks to make sure that the input from the user is an actual number.
def is_it_a_number_dumbass(number_1):
    y_n = False
    while not y_n:
        try:
            number_1 = int(number_1)
            y_n = True
            return number_1
        except:
            print("That's not a whole number.")
            number_1 = input("How many insults would you like?\n")

# Checks to make sure user input is one of the options.
def fast_slow_checker(fast_slow_a):
    t_f = False
    while not t_f:
        if fast_slow_a not in fast_slow_options:
            print("That's not an option.")
            fast_slow_a = input("Would you like them printed fast or slow?\n").lower()
        else:
            t_f = True
            return fast_slow_a

# Does the thing.
def main():
    all_the_words = import_file()
    max_num = int(len(all_the_words)) - 1
    repeat_times = input("How many insults would you like?\n")
    fast_slow = input("Would you like them printed fast or slow?\n").lower()
    fast_slow = fast_slow_checker(fast_slow)
    if repeat_times == "inf" or repeat_times == "infinity" or repeat_times == "infinite":
        while True:
            generate_insult(all_the_words, max_num, fast_slow)
    else:
        repeat_times = is_it_a_number_dumbass(repeat_times)
        for i in range(repeat_times):
            generate_insult(all_the_words, max_num, fast_slow)

if __name__ == "__main__":
    main()
