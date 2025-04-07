import json
import os
import random
import tkinter as tk

box_1 = {}
box_2 = {}
data_file = "quiz_data.json"

# Load existing quiz data or return an empty dictionary if the file is missing or corrupted
def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
                content = f.read().strip()
                return json.loads(content) if content else {}  # Handle empty file case
    else:
        print("Oh no, there's been an error!!!")
    return {}

# Save the quiz results for a specific run number
def save_data(run_number, performance_by_level):
    data = load_data()  # Load existing data
    data[f"run number {run_number}"] = performance_by_level
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)  # Write data to file with indentation for readability

# Determine the next run number based on previous quiz sessions
def find_number():
    data = load_data()
    run_numbers = [int(key.split(" ")[-1]) for key in data.keys() if key.startswith("run number")]
    return max(run_numbers) + 1 if run_numbers else 1
# Conduct a quiz round based on the given question set
def quiz_round(run_number, level, next_level, first_decision, performance_by_level, level_num=1):
    level_name = f"Level {level_num}"
    correct = []
    incorrect = []
    box_1.update(performance_by_level[correct])
    box_2.update(performance_by_level[incorrect])
    print(level_name)
    # Shuffle questions to make it random
    random_questions = list(level.keys())
    random.shuffle(random_questions)
    for question in random_questions:
        user_answer = input(question + " ").lower()
        if user_answer == level[question].lower():
            print("Congrats, you answered correctly!")
            correct.append(question)

        else:
            print(f"Incorrect :( The correct answer was: {level[question]}")
            incorrect.append(question)
    # Update performance for the current level
    performance_by_level[level_name] = {"correct": correct, "incorrect": incorrect}
    save_data(run_number, performance_by_level)
    stats_summary(level_name, correct, incorrect, performance_by_level)
    print(f"Nice job! You answered {len(correct)} questions correctly")

    # Check if user passed the level
    if len(correct) == 6:
        print("You are advancing to the next level!")
        if next_level:
            quiz_round(run_number, next_level["questions"], next_level.get("next"), first_decision, performance_by_level, level_num + 1)
        else:
            print(f"Congratulations! You completed all levels of {first_decision}!")
            quiz_round(run_number, next_level["questions"], next_level.get("next"), first_decision, performance_by_level, level_num + 1)
            main()
    else:
        print("Oh no! Try getting everything right before continuing")
        # json_string = json.dumps(performance_by_level)
        # print(json_string)
        # quiz_round(run_number, run_number[incorrect], "history", performance_by_level={}, level_num={})
        save_data(run_number, performance_by_level)  # Save data before restarting
        main()

# Stats summary after each level
def stats_summary(level_name, correct, incorrect, performance_by_level):
    total_correct = sum(len(lvl["correct"]) for lvl in performance_by_level.values())
    total_incorrect = sum(len(lvl["incorrect"]) for lvl in performance_by_level.values())
    print(f"Summary for {level_name}: Correct = {len(correct)}, Incorrect = {len(incorrect)}")
    print(f"Stats so far: Total Correct = {total_correct}, Total Incorrect = {total_incorrect}")
    print(incorrect, correct)
# Main function that starts the quiz
def main():
    run_number = find_number()
    categories = {
        "history": {
            "questions": {
                "What year did World War II end?": "1945", 
                "Who painted the Mona Lisa?": "Leonardo da Vinci", 
                "What is the longest river in the world?": "The Nile", 
                "Who was the first person to walk on the moon?": "Neil Armstrong",
                "What is the longest wall in the world?": "The Great Wall of China",
                "Where did Albert Einstein live before moving to the United States?": "Germany",
                "Who wrote the Republic, a vision of a society ruled by a philosopher king?":"Plato",
                "When did WWI officially end?":"Nov 11, 1918"
            },
            "next": {
                "questions": {
                    "What was the name of the treaty that ended World War I?": "The Treaty of Versailles",
                    "Who was the leader of the Soviet Union during the Cold War?": "Joseph Stalin",
                    "What is the name of the period of European history that lasted from the 14th to the 17th century?": "The Renaissance",
                    "What was the name of the first successful steam engine?": "The Newcomen Engine",
                    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
                    "What was the code name for the German invasion of the Soviet Union during World War II?": "Operation Barbarossa",
                    "What was the name of the Ukrainian nuclear power plant that was the site of a nuclear disaster in April 1986?": "Chernobyl",
                    "Who were the main combatants in the Peloponnesian War?":"Athens and Sparta"
                },
                "next": {
                    "questions": {
                        "What was the name of the secret project that led to the development of the atomic bomb?": "The Manhattan Project", 
                        "What was the name of the first successful artificial satellite?": "Sputnik",
                        "What is the name of the theory that explains how the universe began?": "The Big Bang Theory",
                        "Who was the last tsar of Russia?": "Nicholas II",
                        "Who was the first woman to fly solo across the Atlantic Ocean?": "Amelia Earhart",
                        "What year did the Berlin Wall fall?": "1989",
                        "Who was the first female Prime Minister of the United Kingdom?": "Margaret Thatcher",
                        "Which war did Operation: Desert Storm kick off in January 1991?":"The Persian Gulf War"
                        ""
                    },
                            "next": None
                        }
                    }
                }
            }
                        
    

    first_decision = input("Hello! Welcome to the Flashcards Game! Do you want to start with history? (yes/no)").lower()
    if first_decision == "yes":
            quiz_round(run_number, categories["history"]["questions"], categories["history"].get("next"), "history", performance_by_level={})
    else:
         print("Okay! Maybe next time. Have a great day!")
main()


# import pandas as pd
# window = tk.Tk()
# bg_color = "#00000"
# window.title("Flashcards Game!")
# window.config("500x300")
# card_title = .create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
# window.mainloop()

