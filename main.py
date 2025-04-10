import json
import os
import random

questions_asked = []

box_1 = []
box_2 = []
box_3 = []
box_4 = []

past_runs = {
    "level_1": [],
    "level_2": [],
    "level_3": []
}

current_run = {
    "level_1": {"correct": [], "incorrect": []},
    "level_2": {"correct": [], "incorrect": []},
    "level_3": {"correct": [], "incorrect": []}
}

data_file = "quiz_data.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            content = f.read()
            return json.loads(content) if content else {}
    return {}

def load_past_runs():
    data = load_data()
    for run_data in data.values():
        for level, stats in run_data.items():
            if level in past_runs and "correct" in stats:
                past_runs[level].append(stats)

def save_data(past_runs, current_run):
    data = load_data()
    run = f"run number {len(data) + 1}"
    data[run] = current_run
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

def print_average(level_name):
    previous = past_runs.get(level_name, [])
    total_correct = sum(len(run['correct']) for run in previous)
    total_attempted = sum(len(run['correct']) + len(run['incorrect']) for run in previous)
    old_average = (total_correct / total_attempted) if total_attempted else 0
    current = current_run.get(level_name, {})
    current_correct = len(current.get("correct", []))
    current_incorrect = len(current.get("incorrect", []))
    current_attempted = current_correct + current_incorrect
    current_average = (current_correct / current_attempted) if current_attempted else 0
    print(f"Past average = {old_average:.2%}, current average = {current_average:.2%}.")

def quiz_round(questions_dict, level_name, level):
    if level == 1:
        review = box_1
    elif level == 2:
        review = box_2
    elif level == 3:
        review = box_3
    else:
        review = []

    # Combine questions for levels above 1
    if level == 1:
        questions = list(questions_dict.keys())
    else:
        questions = list(questions_dict.keys()) + review

    random.shuffle(questions)

    for question in questions:
        correct_answer = questions_dict.get(question, "").lower()
        user_answer = input(f"{question} ").lower()
        if user_answer == correct_answer:
            print("Congrats, you answered correctly!")
            current_run[level_name]["correct"].append(question)
        else:
            print(f"Incorrect :( The correct answer was: {correct_answer}")
            current_run[level_name]["incorrect"].append(question)
            if level == 1:
                box_1.append(question)
            elif level == 2:
                box_2.append(question)
            elif level == 3:
                box_3.append(question)

        questions_asked.append(question)

    print_average(level_name)

    total = len(current_run[level_name]["correct"]) + len(current_run[level_name]["incorrect"])
    passing = len(current_run[level_name]["correct"]) / total if total else 0

    if total > 0:
        save_data(past_runs, current_run)

    return passing > 0.5

def main():
    load_past_runs()
    categories = {
        "history": {
            "questions": {
                "What year did World War II end?": "1945", 
                "Who painted the Mona Lisa?": "Leonardo da Vinci", 
                "What is the longest river in the world?": "The Nile", 
                "Who was the first person to walk on the moon?": "Neil Armstrong",
                "What is the longest wall in the world?": "The Great Wall of China",
                "Where did Albert Einstein live before moving to the United States?": "Germany",
                "Who wrote the Republic, a vision of a society ruled by a philosopher king?": "Plato",
                "When did WWI officially end?": "Nov 11, 1918"
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
                    "Who were the main combatants in the Peloponnesian War?": "Athens and Sparta"
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
                        "Which war did Operation: Desert Storm kick off in January 1991?": "The Persian Gulf War"
                    },
                    "next": None
                }
            }
        }
    }

    first_decision = input("Hello! Welcome to the Flashcards Game! Do you want to start with history? (yes/no) ").strip().lower()
    
    if first_decision == "yes":
        level = 1
        level_name = f"level_{level}"
        current_category = categories["history"]
        
        while current_category:
            print(f"Starting {level_name}!!!")
            passed = quiz_round(current_category["questions"], level_name, level)
            
            if passed and current_category.get("next"):
                current_category = current_category["next"]
                level += 1
                level_name = f"level_{level}"
            else:
                break
        
        save_data(past_runs, current_run)
    else:
        print("Okay! Maybe next time. Have a great day!")

main()
