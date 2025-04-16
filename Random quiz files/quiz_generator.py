from settings import *

import json
import os
from random import shuffle, sample


def get_capitals() -> dict:

    with open('capitals.json', 'r') as file:
        content = json.load(file)

    return content['capitals']


def create_quiz_files_directory() -> None:

    try:
        os.mkdir('quiz_files')

    except FileExistsError:
        pass


def main() -> None:

    capitals = get_capitals()

    create_quiz_files_directory()

    for i in range(FILES_TO_CREATE):

        # Create the files
        quiz_file = open(f"quiz_files\\Capitals_questions_{i + 1}.txt", 'w')
        answer_file = open(f"quiz_files\\Capitals_answers_{i + 1}.txt", 'w')

        # Write the header for the quiz file
        quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
        quiz_file.write((" " * 20) + f"State Capitals Quiz (Form {i + 1})\n\n")

        # Shuffle the order of the states
        states = list(capitals.keys())
        shuffle(states)

        # Create the answer options
        for n in range(QUESTIONS_TO_CREATE):

            correct_answer = capitals[states[n]]

            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = sample(wrong_answers, 3)

            answer_options = wrong_answers + [correct_answer]
            shuffle(answer_options)

            # Write the question and the answer options to the quiz file
            quiz_file.write(f"{n + 1}. What is the capital of {states[n]}?\n")
            for x in range(4):
                quiz_file.write(f"    {'ABCD'[x]}.  {answer_options[x]}\n")
            quiz_file.write('\n')

            # Write the answer to the answer file
            answer_file.write(f"{n + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")

        # Close the files
        quiz_file.close()
        answer_file.close()


if __name__ == '__main__':
    main()
