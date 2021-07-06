#from typing_extensions import TypeVarTuple
from questions import quiz
#Hyvä, omat kirjastot, vastauksia ja kysymyksiä ei näy koodissa.
score = 0

def check_answer(player_answer, question):
    if player_answer.lower() == quiz[question]['answer']:
        print("Your answer was correct!")
        return True
    print("Your answer was incorrect!")
    return False 
#hyvä, vastaus muutettu pieniksi kirjaimiksi.

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
    
    print(f"You reached the end. Your score is {score} out of {len(quiz)}")

    if score == len(quiz):
        print("You got everything correct, extra question!")
        final = input("Is it ok to put pineapple on a pizza? (yes/no): ")
        if final.lower() == "no":
            print("That is the correct answer. You win!")
        else:
            print("Go away!")
            break
#hyvin toteutettu, laadukas ohjelma. Tähän on helppo lisätä kysymyksiä ja ohjelma huomioi sen.