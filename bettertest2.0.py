import random

score = 0
hp = 3

def check(correct, answer):
    global score
    global hp
    if correct == answer:
        print("you got it right!")
        score += 1
        return True
    else:
        hp -= 1
        print("nope, you lose a life, try again")
        print(f"you have {hp} lives remaining")
        return False


riddles = [
    ("cycle cycle cycle > ", "tricycle"),
    ("stand stand stand i > ", "understand"),
    ("man board > ", "manoverboard"),
    ("you just me > ", "just_between_you_and_me"),
    ("space space space > ", "outerspace")
]

selected = random.sample(riddles, 2)

for question, correct_answer in selected:
    hp = 3
    while hp > 0:
        answer = input(question)
        if check(correct_answer, answer):
            break

print("Final score:", score)
