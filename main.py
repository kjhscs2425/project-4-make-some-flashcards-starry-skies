import json
import os
import random

data_file = "quiz_data.json"

# Load existing quiz data or return an empty dictionary if the file is missing or corrupted
def load_data():
    if os.path.exists(data_file):
        try:
            with open(data_file, "r") as f:
                content = f.read().strip()
                return json.loads(content) if content else {}  # Handle empty file case
        except json.JSONDecodeError:
            print("Error: quiz_data.json is corrupted. Resetting file.")
            return {}  # Return an empty dictionary instead of failing
    return {}

# Save the quiz results for a specific run number
def save_data(run_number, correct, incorrect):
    data = load_data()  # Load existing data
    data[f"run number {run_number}"] = {
        "questions_answered_right": correct,
        "questions_answered_wrong": incorrect
    }
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)  # Write data to file with indentation for readability

# Determine the next run number based on previous quiz sessions
def find_number():
    data = load_data()
    run_numbers = [int(key.split(" ")[-1]) for key in data.keys() if key.startswith("run number")]
    return max(run_numbers) + 1 if run_numbers else 1

# Conduct a quiz round based on the given question set
def quiz_round(run_number, level, next_level, first_decision):
    correct_answers = []
    incorrect_answers = []
    
    random_questions = list(level.keys())
    random.shuffle(random_questions)  # Randomize question order

    for question in random_questions:
        user_answer = input(question + " ").strip().lower()
        if user_answer == level[question].lower():
            print("Congrats, you answered correctly!")
            correct_answers.append(question)
        else:
            print(f"Incorrect :( The correct answer was: {level[question]}")
            incorrect_answers.append(question)

    print(f"\nNice job! You answered {len(correct_answers)} questions correctly!")

    save_data(run_number, correct_answers, incorrect_answers)

    # If the user gets at least half correct, they advance to the next level
    if len(correct_answers) >= len(random_questions) // 2:
        print("\nYou are advancing to the next level!")
        if next_level:
            quiz_round(run_number, next_level["questions"], next_level.get("next"), first_decision)
        else:
            print(f"🎉 Congratulations! You completed all three levels of {first_decision}! 🎉")
            play_again()
    else:
        print("\nGame over! Try again to improve your score.")
        play_again()

# Ask the user if they want to play again
def play_again():
    restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if restart == "yes":
        main()
    else:
        print("Thanks for playing! See you next time. 👋")

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
                "Where did Albert Einstein live before moving to the United States?": "Germany"
            },
            "next": {
                "questions": {
                    "What was the name of the treaty that ended World War I?": "The Treaty of Versailles",
                    "Who was the leader of the Soviet Union during the Cold War?": "Joseph Stalin",
                    "What is the name of the period of European history that lasted from the 14th to the 17th century?": "The Renaissance",
                    "What was the name of the first successful steam engine?": "The Newcomen Engine",
                    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
                    "What was the code name for the German invasion of the Soviet Union during World War II?": "Operation Barbarossa",
                    "What was the name of the Ukrainian nuclear power plant that was the site of a nuclear disaster in April 1986?": "Chernobyl"
                },
                "next": {
                    "questions": {
                        "What was the name of the secret project that led to the development of the atomic bomb?": "The Manhattan Project", 
                        "What was the name of the first successful artificial satellite?": "Sputnik",
                        "What is the name of the theory that explains how the universe began?": "The Big Bang Theory",
                        "Who was the last tsar of Russia?": "Nicholas II",
                        "Who was the first woman to fly solo across the Atlantic Ocean?": "Amelia Earhart",
                        "What year did the Berlin Wall fall?": "1989",
                        "Who was the first female Prime Minister of the United Kingdom?": "Margaret Thatcher"
                    },
                    "next": None
                }
            }
        }
    }

    first_decision = input("\nHello! Welcome to the Flashcards Game! Do you want to start with history trivia? (yes/no): ").strip().lower()
    
    if first_decision == "yes":
        quiz_round(run_number, categories["history"]["questions"], categories["history"].get("next"), "history")
    else:
        print("\nOkay! Maybe next time. Have a great day! 👋")

# Start the quiz program
if __name__ == "__main__":
    main()
