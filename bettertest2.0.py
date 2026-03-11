import random

score = 0
hp = 3

def check(correct, answer):
    global score
    global hp
    if correct == answer:
        if hp == 3:
            print("wow one try? nice , three points for you")
            score += 3
        elif hp == 2:
            print("umm ok..? , points for you")
            score += 2
        elif hp == 1:
            print("bro")
            score += 1
    else:
        hp -= 1
        print("nope, you lose a life, try again")
        print(f"you have {hp} lives remaining")
        return False


# riddles list
riddles = [
    ("cycle cycle cycle > ", "tricycle"),
    ("stand stand stand i > ", "understand"),
    ("man board > ", "manoverboard"),
    ("you just me > ", "just_between_you_and_me"),
    ("space space space > ", "outerspace")
]

# pick 2 random riddles (no duplicates)
selected = random.sample(riddles, 2)

for question, correct_answer in selected:
    hp = 3
    while hp > 0:
        answer = input(question)
        if check(correct_answer, answer):
            break

print("Final score:", score)
