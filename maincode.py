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


while hp > 0:
    answer = input("cycle cycle cycle > ")
    if check("tricycle", answer):
        break
hp = 3

while hp > 0:
    answer = input("stand stand stand i > ")
    if check("understand", answer):
        break
hp = 3

while hp > 0:
    answer = input("man board > ")
    if check("manoverboard", answer):
        break
hp = 3

while hp > 0:
    answer = input("you just me > ")
    if check("just_between_you_and_me", answer):
        break
hp = 3

while hp > 0:
    answer = input("space space space > ")
    if check("outerspace", answer):
        break

print("Final score:", score)
#scrapped due to buggs
#fixed
#inefficient btw
