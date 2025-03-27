
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
# questions_answered_right_history = []
# questions_answered_wrong_history = []
# questions_answered_right_geography = []
# questions_answered_wrong_geography = []
# questions_answered_right_popculture = []
# questions_answered_wrong_popculture = []
# questions_answered_right_records = []
# questions_answered_wrong_records = []
import random
import matplotlib

#history facts
history_easy_round = {"What year did World War II end?":"1945", 
              "Who painted the Mona Lisa?":"Leonardo da Vinci", 
              "What is the longest river in the world?":"The Nile", 
              "Who was the first person to walk on the moon?":"Neil Armstrong",
              "What is the longest wall in the world?":"The Great Wall of China",
              "Where did Albert Einstein live before moving to the United States?":"Germany"
}
history_medium_round = {"What was the name of the treaty that ended World War I?":"The Treaty of Versailles",
                "Who was the leader of the Soviet Union during the Cold War?":"Joseph Stalin",
                "What is the name of the period of European history that lasted from the 14th to the 17th century?":"The Renaissance",
                "What was the name of the first successful steam engine?":"The Newcomen Engine",
                "Who wrote 'To Kill a Mockingbird'?":"Harper Lee",
                "What was the code name for the German invasion of the Soviet Union during World War II?":"Operation Barbarossa",
                "What was the name of the Ukrainian nuclear power plant that was the site of a nuclear disaster in April 1986?":"Chernobyl"
}
history_hard_round = {"What was the name of the secret project that led to the development of the atomic bomb?":"The Manhatten Project", 
              "What was the name of the first successful artificial satellite?":"Sputnik",
              "What is the name of the theory that explains how the universe began?":"The Big Bang Theory",
              "Who was the last tzar of Russia?":"Nicholas II",
              "Who was the first woman to fly solo across the Atlantic Ocean?":"Amelia Earhart",
              "What year did the Berlin Wall fall?":"1989",
              "Who was the first female Prime Minister of the United Kingdom?":"Margaret Thatcher"

}
#geography facts
geography_easy_round = {"hello world", "food"}
geography_medium_round = {"he", "sh"}
geography_hard_round = {"she", "fbe"}
#pop culture facts
popculture_easy_round = {"gr", "rtyh"}
popculture_medium_round = {"wer", "dfg"}
popculture_hard_round = {"cv", "fgh"}
#Guiness world records (make it so that if they guess something close, they still get point)
records_easy_round = {"sdfe", "wertg"}
records_medium_round = {"efrg", "jyhtg"}
records_hard_round = {"yhrt54rwedfthy", "wre4t5y6yjhngbfr"}

questions_answered_right_easy = []
questions_answered_wrong_easy = []

def quiz_round_all(level):
    random_questions = list(level.keys())
    for random_question in random_questions:
        user_answer = input(random_question + " ")
        if user_answer == level[random_question]:
            print("Congrats, you answered correctly!")
            questions_answered_right_easy.append(random_question)
        else:
            print("Incorrect :(")
            questions_answered_wrong_easy.append(random_question)
    print(f"Nice job! You answered {len(questions_answered_right_easy)} questions correctly! You are advancing to round 2")
    if len(questions_answered_right_easy) >= 3:
        next_step = input("Would you like to try geography, pop culture, or world records trivia next?").lower
        if next_step == "geography":
            quiz_round_all(geography_easy_round)
        elif next_step == "pop culture":
            quiz_round_all(popculture_easy_round)
        elif next_step == "records":
            quiz_round_all(records_easy_round)
        else:
            quiz_round_all(history_easy_round)
        return questions_answered_right_easy, questions_answered_wrong_easy
    if len(questions_answered_right_easy) >= 8:
        next_step = input("Would you like to try history, geography, pop culture, or world records trivia next?").lower
        if next_step == "geography":
            quiz_round_all(geography__round)
        elif next_step == "pop culture":
            quiz_round_all(popculture_easy_round)
        elif next_step == "records":
            quiz_round_all(records_easy_round)
        elif next_step == "history":
            quiz_round_all(geography_easy_round)
        else:
            quiz_round_all(history_easy_round)
        return questions_answered_right_easy, questions_answered_wrong_easy

# quiz_round_all_history(easy_round)
def quiz_round_all_geography (level):
    random_questions = list(level.keys())
    for random_question in random_questions:
        user_answer = input(random_question + " ")
        if user_answer == level[random_question]:
            print("Congrats, you answered correctly!")
            questions_answered_right.append(random_question)
        else:
            print("Incorrect :(")
            questions_answered_wrong.append(random_question)
    print(f"Nice job! You answered {len(questions_answered_right)} questions correctly!")
    if len(questions_answered_right) >= 3:
        quiz_round_all(medium_round)
    if len(questions_answered_right >= 7):
        quiz_round_all(hard_round)
    else:
        quiz_round_all(easy_round)
    return questions_answered_right, questions_answered_wrong

