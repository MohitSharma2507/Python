# import random

# question_bank = [
#       {"text": "The ability of one class to acquire methods and attributes of another class is called ___","answer":'A'},
#       {"text": "Which concept allows using the same method name with different implementations?","answer":'B' },
#       {"text": "Which OOP principle hides internal implementation details?", "answer":'D' },
#       {"text": "Which keyword is used to inherit a class in Java?",   "answer":'C'},
#       {"text": "What is it called when a class has multiple methods with same name but different parameters?","answer":'B'      },
#       {"text": "Which concept binds data and methods together into a single unit?","answer":'C'  }
# ]

# options= [
#     ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"]  ,  
#     ["A. Encapsulation", "B. Polymorphism", "C. Inheritance", "D. Abstraction"],
#     ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
#     ["A. this", "B. super", "C. extends", "D. implements"],
#     ["A. Overriding", "B. Overloading", "C. Inheritance", "D. Encapsulation"],
#     ["A. Abstraction", "B. Encapsulation", "C. Polymorphism", "D. Inheritance"]
# ]
# random.shuffle(question_bank)
# print("Welcome to My Quiz Game\n")
# score=0
# for questions_num in range(len(question_bank)):   
 
#    print("************************************************")
#    print(question_bank[questions_num]['text'])
#    for i in options[questions_num]:
#       print(i) 
#    user_ans=input("Enter your answer(A/B/C/D) :").upper() 
#    if user_ans== question_bank[questions_num]['answer']:
#       print('Correct Answer')
#       score+=1
#    else:
#       print("Incorrect Answer")  
#    print(f"Your score is {score}")   

# print(f"You have given {score} correct answer")
# print(f"Your score is {(score/len(question_bank))*100}%")

import random

# 🔹 Question Class
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer


# 🔹 Quiz Class
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_quiz(self):
        print("Welcome to My Quiz Game\n")
        random.shuffle(self.questions)

        for q in self.questions:
            print("************************************************")
            print(q.text)

            for opt in q.options:
                print(opt)

            user_ans = input("Enter your answer (A/B/C/D): ").upper()

            if user_ans == q.answer:
                print("Correct Answer")
                self.score += 1
            else:
                print("Incorrect Answer")

            print(f"Your score is {self.score}\n")

        self.show_result()

    def show_result(self):
        total = len(self.questions)
        print(f"You have given {self.score} correct answers")
        print(f"Your score is {(self.score / total) * 100}%")


# 🔹 Create Question Objects
question_list = [
    Question(
        "The ability of one class to acquire methods and attributes of another class is called ___",
        ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
        "A"
    ),
    Question(
        "Which concept allows using the same method name with different implementations?",
        ["A. Encapsulation", "B. Polymorphism", "C. Inheritance", "D. Abstraction"],
        "B"
    ),
    Question(
        "Which OOP principle hides internal implementation details?",
        ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
        "D"
    ),
    Question(
        "Which keyword is used to inherit a class in Java?",
        ["A. this", "B. super", "C. extends", "D. implements"],
        "C"
    ),
    Question(
        "What is it called when a class has multiple methods with same name but different parameters?",
        ["A. Overriding", "B. Overloading", "C. Inheritance", "D. Encapsulation"],
        "B"
    ),
    Question(
        "Which concept binds data and methods together into a single unit?",
        ["A. Abstraction", "B. Encapsulation", "C. Polymorphism", "D. Inheritance"],
        "B"
    )
]

# 🔹 Create Quiz Object and Start
quiz = QuizGame(question_list)
quiz.start_quiz()