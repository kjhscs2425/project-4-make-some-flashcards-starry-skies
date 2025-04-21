import json
import os
import random
import matplotlib.pyplot as plt

def show_flashcard(text, title="Flashcard"):
    plt.ion()  #updates without stopping code
    fig, ax = plt.subplots(figsize=(7, 4)) #figure size 7 by 4 inches, other measurements work too
    ax.text(0.5, 0.5, text, fontsize=18, ha='center', va='center', wrap=True)
    ax.set_axis_off()
    plt.title(title, fontsize=14, pad=20)
    plt.tight_layout()
    plt.show()
    plt.pause(0.01)  

questions_asked = []

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
def load_past_runs(username):
    data = load_data()
    user_data = data.get(username, {}) 
    for run_data in user_data.values():
        for level, stats in run_data.items():
            if level in past_runs and "correct" in stats:
                past_runs[level].append(stats)

def save_data(username, current_run):
    data = load_data()
    if username not in data:
        data[username] = {}
    run = f"run number {len(data[username]) + 1}"
    data[username][run] = current_run
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

def quiz_round(category, username, level=1):
    level_name = f"level_{level}"
    questions_dict = category["questions"]
    remaining_questions = list(questions_dict.keys())
    random.shuffle(remaining_questions)
    #first attempt 
    first_try = {"correct": [], "incorrect": []}
    first_pass = True
    while remaining_questions:
        incorrect_questions = []
        for question in remaining_questions:
            correct_answer = questions_dict[question].lower()
            show_flashcard(question, title=f"Level {level} Flashcard")
            user_answer = input("Your answer: ").lower()
            plt.close()
            if user_answer == correct_answer:
                print("Correct!!!")
                if first_pass:
                    first_try["correct"].append(question)
            else:
                print(f"Incorrect :( The correct answer was: {correct_answer}")
                show_flashcard(f"The correct answer was:\n{correct_answer}", title="Answer")
                incorrect_questions.append(question)
                if first_pass:
                    first_try["incorrect"].append(question)
            questions_asked.append(question)
        if first_pass:
            current_run[level_name]["correct"].extend(first_try["correct"])
            current_run[level_name]["incorrect"].extend(first_try["incorrect"])
            first_pass = False
        print_average(level_name)
        if incorrect_questions:
            print(f"Oops, you made {len(incorrect_questions)} mistakes! Try again before advancing to the next level")
        remaining_questions = incorrect_questions
    save_data(username, current_run)
    print(f"Yay, you passed {level_name}!")
    if category.get("next"):
        quiz_round(category["next"], username, level + 1)

def main():
    username = input("Howdy! What's your name?: ").lower()
    load_past_runs(username)
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
    if input("Welcome to the History Trivia Game! Are you ready to rumble??? (yes/no): ").lower() == "yes":
        quiz_round(categories["history"], username)
    else:
        print("Okay, see you next time!")

main()
