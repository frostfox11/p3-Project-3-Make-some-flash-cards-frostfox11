import json
import random

with open('flashcards.json', 'r') as f:
    flashcards = json.load(f)

flashcards_list = list(flashcards.items())
random.shuffle(flashcards_list)

for prompt, answer in flashcards_list:
    user_response = input(prompt + ": ")
    if user_response == answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is: " + answer)