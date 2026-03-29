questions = (("How many days are there in a week: "),
             ("How many days are in a leap year: "),
             ("What is the capital city of Japan: "),
             ("What is the closest planet to us: "))
options = (("A. 5", "B. 6", "C. 8", "D. 7"),
           ("A. 365", "B. 364", "C. 366", "D. 356"),
           ("A. Nagoya", "B. Fukuoka", "C. Tokyo", "D. Kyoto"),
           ("A. Pluto", "B. Mercury", "C. Venus", "D. Mars"))
answers = (("D"),
           ("C"),
           ("C"),
           ("D"))
guesses = []
score = 0
question_num = 0
for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option, end=" ")
    print()
    guess = input("Enter your guess choose A to D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("------------------------------")
print("           RESULTS            ")
print("------------------------------")
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score = float((score / len(questions)) * 100)
print(f"score: {score:.2f}%")
