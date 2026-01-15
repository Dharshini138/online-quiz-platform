import sqlite3
import time
from tqdm import tqdm  # pip install tqdm

# Connect to DB and fetch questions
conn = sqlite3.connect("quiz.db")
cur = conn.cursor()
cur.execute("SELECT question, option1, option2, option3, option4, answer FROM questions")
questions = cur.fetchall()
conn.close()

# Function to ask a question with a 30-second progress bar
def ask_question(q):
    print("\nQuestion:", q[0])
    print("A)", q[1])
    print("B)", q[2])
    print("C)", q[3])
    print("D)", q[4])
    
    # Start 30-second countdown with progress bar
    print("\nYou have 30 seconds to answer...")
    for i in tqdm(range(30), desc="Time", ncols=70):
        time.sleep(1)
    
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    correct_option = q[5]
    if answer == "A" and correct_option == q[1]:
        print("✅ Correct!")
        return True
    elif answer == "B" and correct_option == q[2]:
        print("✅ Correct!")
        return True
    elif answer == "C" and correct_option == q[3]:
        print("✅ Correct!")
        return True
    elif answer == "D" and correct_option == q[4]:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! Correct answer: {correct_option}")
        return False

# Main Quiz Loop
score = 0
for q in questions:
    if ask_question(q):
        score += 1

print(f"\nYour final score: {score}/{len(questions)}")
