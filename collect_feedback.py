import json
import random


def collect_feedback():
    responses = load_feedback()
    print("Community Feedback Survey")
    while True:
        name = input("Enter your name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        rating = input("Rate local initiatives (1-5): ")
        concerns = ""
        while not concerns.strip():
            concerns = input("What are your top concerns? (comma-separated): ")
            if not concerns.strip():
                print("Please enter at least one concern.")

        new_feedback = {
            "name": name,
            "rating": int(rating),
            "concerns": [c.strip() for c in concerns.split(',')]
        }
        responses.append(new_feedback)

        print(f"Thank you, {name}, for your feedback! Your concerns have been recorded.")

        while True:
            next_step = input("Choose an option: (1) Main Menu (2) Exit (3) View Past Feedbacks: ")
            if next_step == '1':
                return
            elif next_step == '2':
                exit()
            elif next_step == '3':
                show_past_feedback(responses, new_feedback)
                while True:
                    follow_up = input("Select an option: (1) Main Menu (2) Exit: ")
                    if follow_up == '1':
                        return
                    elif follow_up == '2':
                        exit()
                    else:
                        print("Invalid choice. Please enter 1 or 2.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    save_feedback(responses)
    print("Survey completed. Data saved.")


def load_feedback():
    try:
        with open("feedback.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_feedback(responses):
    with open("feedback.json", "w") as file:
        json.dump(responses, file, indent=4)


def show_past_feedback(responses, new_feedback):
    sample_feedbacks = [
        {"name": "Alice", "rating": 4, "concerns": ["Traffic", "Public Safety"]},
        {"name": "Bob", "rating": 2, "concerns": ["Healthcare", "Education"]},
        {"name": "Charlie", "rating": 5, "concerns": ["Parks", "Clean Energy"]},
        {"name": "David", "rating": 3, "concerns": ["Housing", "Internet Access"]},
        {"name": "Eve", "rating": 1, "concerns": ["Job Opportunities", "Transportation"]}
    ]

    randomized_feedbacks = random.sample(sample_feedbacks, 3)
    randomized_feedbacks.append(new_feedback)
    print("\n--- Past Feedbacks ---")
    for feedback in randomized_feedbacks:
        print(f"Name: {feedback['name']}, Rating: {feedback['rating']}, Concerns: {', '.join(feedback['concerns'])}")
    print("-----------------------\n")


if __name__ == "__main__":
    while True:
        choice = input("Choose an option: (1) Collect Feedback (2) Exit: ")
        if choice == '1':
            collect_feedback()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
