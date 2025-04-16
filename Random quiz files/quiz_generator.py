from settings import *

import json
import os
from random import shuffle, sample


def get_capitals() -> json:

    with open('capitals.json', 'r') as file:
        content = json.load(file)

    return content['capitals']


def main() -> None:

    capitals = get_capitals()

    for i in range(FILES_TO_CREATE):

        # Create the files
        try: os.mkdir('quiz_files')
        except FileExistsError: pass

        quiz_file = open(f"quiz_files\\Capitals_questions_{i + 1}.txt", 'w')
        answer_file = open(f"quiz_files\\Capitals_answers_{i + 1}.txt", 'w')


if __name__ == '__main__':
    main()
