from questions import quiz

while True:

    playing = str(input("Do you want to play a game? (y/n)"))

    if playing == "n":
        break

    score = 0

    for question in quiz:
        print(f"{quiz[question]['question']}")
        answer = str(input("Enter answer: "))
        check = check_answer(answer, question)
        if check:
            score +=1