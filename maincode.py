score = 0

def check(correct, answer):
    global score
    if correct == answer:
        print("you got it right!")
        score += 1
    else:
        print("nope")

answer = input("cycle cycle cycle > ")
check("tricycle", answer)

answer = input("stand stand stand i > ")
check("understand", answer)

answer = input("man board > ")
check("manoverboard", answer)

answer = input("you just me > ")
check("just_between_you_and_me", answer)

answer = input("space space space > ")
check("outerspace", answer)

print("Final score:", score)
