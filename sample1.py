import random
score = 0
turn = 0
answers = []

questionsAndAnswers = [("ten", "10"),
                       ("twenty", "20"),
                       ("thirty", "30"),
                       ("forty", "40"),
                       ("fifty", "50"),
                       ("sixty", "60"),
                       ("seventy", "70"),
                       ("eighty", "80"),
                       ("ninty", "90"),
                       ("one hundred", "100")]

while turn < 3: 
    turn += 1
    r = random.randint(0, 9)
    question, correct_answer = questionsAndAnswers[r]
    i = 0
    answers = []
    answers.append(correct_answer)
    while i < 3:
        # we can use random.sample instead
        r2 = random.randint(0, len(questionsAndAnswers) - 1)
        rq, ra = questionsAndAnswers[r2]
        if ra not in answers:
            answers.append(ra)
            i += 1
    random.shuffle(answers)
    print(question)
    for answer in answers:
        print("\t" + answer)                           #Print these line by line
    userInput = input("select one: ")
    #turn += 1
    if userInput == correct_answer:
        print("congratulations\n\n")
        score = score + 1
    else:
        print("sorry, sucker!\n\n")
    # create a while loop to catch for invalid answers
print("Your score is:  " + str(score))
print("game over")
