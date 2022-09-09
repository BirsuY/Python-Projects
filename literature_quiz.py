#birsuyilmaz
quiz = {
    "question 1": {
        "question": "Elizabeth Bennet is the protagonist of which Jane Austen novel?",
        "answer": "Pride and Prejudice"
    },
    "question 2": {
        "question": "Virginia Woolf is famous for pinoeering the use of stream of ______ with her narration.",
        "answer": "Consciousness"
    },
    "question 3": {
        "question": "Which two cities are the settings for Charles Dickens' 'A Tale of Two Cities'?",
        "answer": "Paris and London"
    },
    "question 4": {
        "question": "Which country banned 'Alice in Wonderland?'",
        "answer": "China"
    },
    "question 5": {
        "question": "What villain's name does Tom Riddle's name rearragne to?",
        "answer": "Voldemort"
    },
    "question 6": {
        "question": "Which one of Jojo Moyes many books was made into a film starring Emilia Clarke as Lou Clark caring for a quadriplegic man?",
        "answer": "Me Before You"
    },
    "question 7": {
        "question": " Who wrote the books The Handmaid's Tale are based on?",
        "answer": "Margaret Atwood"
    },
    "question 8": {
        "question": "T/F: Originally plays of Shakespeare only included men in their productions.",
        "answer": "T"
    },
    "question 9": {
        "question": "T/F: Charles Dickens believed that sleeping south would improve his writing",
        "answer": "F"
    },
    "question 10": {
        "question": "T/F: Mary Shelley has inspiration for Frankenstein from a daydream.",
        "answer": "F"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")
    
    if answer.lower() == value['answer'].lower():
        score += 10
        print("Correct Answer !!! Keep the good work !!!")
        print(f"Your score is {score}")
    else:
        print("Wrong Answer. Try studying harder.")
        print(f"The answer is {value['answer']}")
        print(f"Your score is {score}")
        
print(f"Congratulations!! You finished the quiz.\nYour final score is {score} out of 100.")
#birsuyilmaz