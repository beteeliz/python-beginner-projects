quiz = {
    "question 1": {
    "question": "1. Where did the invention of the electric shower come from?",
    "answer": "Brazil"
    },

    "question 2": {
    "question": "2. Today, how many chemical elements does the periodic table have?",
    "answer": "118"
    },

    "question 3": {
    "question": "3. What is acrophobia a fear of?",
    "answer": "Flying"
    },

    "question 4": {
    "question": "4. How many hearts does an octopus have?",
    "answer": "3"
    },

    "question 5": {
    "question": "5. What country has the most islands?",
    "answer": "Sweden"
    },

    "question 6": {
    "question": "6. What planet is closest to the sun?",
    "answer": "Mercury"
    },   

    "question 7": {
    "question": "7. What is the only continent with land in all four hemispheres?",
    "answer": "Africa"
    },

    "question 8": {
    "question": "8. Where did sushi originate?",
    "answer": "China"
    },

    "question 9": {
    "question": "9. What sporting event has a strict dress code of all-white?",
    "answer": "Wimbledon"
    },

    "question 10": {
    "question": "10. What year was Cinderella released?",
    "answer": "1950"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Write your answer: ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("Your final score is: " + str(score) + " out of 10 questions correctly.")
print("Your percentage is: " + str(score/10 * 100) + "%")