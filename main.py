import random
import ctypes
easy_round = {"What year did World War II end?":"1945", 
              "Who painted the Mona Lisa?":"Leonardo da Vinci", 
              "What is the longest river in the world?":"The Nile", 
              "Who was the first person to walk on the moon?":"Neil Armstrong",
              "What is the longest wall in the world?":"The Great Wall of China",
              "Where did Albert Einstein live before moving to the United States?":"Germany"
}
medium_round = {"What was the name of the treaty that ended World War I?":"The Treaty of Versailles",
                "Who was the leader of the Soviet Union during the Cold War?":"Joseph Stalin",
                "What is the name of the period of European history that lasted from the 14th to the 17th century?":"The Renaissance",
                "What was the name of the first successful steam engine?":"The Newcomen Engine",
                "Who wrote 'To Kill a Mockingbird'?":"Harper Lee",
                "What was the code name for the German invasion of the Soviet Union during World War II?":"Operation Barbarossa",
                "What was the name of the Ukrainian nuclear power plant that was the site of a nuclear disaster in April 1986?":"Chernobyl"
}
hard_round = {"What was the name of the secret project that led to the development of the atomic bomb?":"The Manhatten Project", 
              "What was the name of the first successful artificial satellite?":"Sputnik",
              "What is the name of the theory that explains how the universe began?":"The Big Bang Theory",
              "Who was the last tzar of Russia?":"Nicholas II",
              "Who was the first woman to fly solo across the Atlantic Ocean?":"Amelia Earhart",
              "What year did the Berlin Wall fall?":"1989",
              "Who was the first female Prime Minister of the United Kingdom?":"Margaret Thatcher"


}

#record which questions were right and which question were wrong
# questions_answered_right = []
# questions_answered_wrong = []
# random_questions = list(easy_round.keys())
# for random_question in random_questions:
#     user_answer = input(random_question + "")
#     if user_answer == easy_round[random_question]:
#         print("Congrats, you answered correctly!")
#         questions_answered_right.append(random_question)
#     else:
#         print("Incorrect :(")
#         questions_answered_wrong.append(random_question)
# print(f"Nice job! You answered" + questions_answered_right + " questions correctly!")
    
def quiz_round_1():
    questions_answered_right = []
    questions_answered_wrong = []
    random_questions = list(easy_round.keys())
    for random_question in random_questions:
        user_answer = input(random_question + " ")
        if user_answer == easy_round[random_question]:
            print("Congrats, you answered correctly!")
            questions_answered_right.append(random_question)
        else:
            print("Incorrect :(")
            questions_answered_wrong.append(random_question)
    print(f"Nice job! You answered {len(questions_answered_right)} questions correctly!")
    if len(questions_answered_right) >= 3:
        quiz_round_2():
    else:
        quiz_round_1()
    return questions_answered_right, questions_answered_wrong

def quiz_round_2():

quiz_round_1()

