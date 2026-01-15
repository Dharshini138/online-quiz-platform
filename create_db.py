import sqlite3
import time
from tqdm import tqdm  # make sure: pip install tqdm

# --------------------------
# 1. Setup DB and Questions
# --------------------------
conn = sqlite3.connect("quiz.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS questions(
 id INTEGER PRIMARY KEY,
 question TEXT,
 option1 TEXT,
 option2 TEXT,
 option3 TEXT,
 option4 TEXT,
 answer TEXT
)
""")

# Insert 10 questions if table is empty
cur.execute("SELECT COUNT(*) FROM questions")
if cur.fetchone()[0] == 0:
    questions_to_insert = [
        ("What is Python?", "Snake", "Programming Language", "Car", "Game", "Programming Language"),
        ("HTML stands for?", "Hyper Text Markup Language", "High Text Machine Language", "Hyperlinks", "None", "Hyper Text Markup Language"),
        ("Which language is used for web apps?", "Python", "JavaScript", "C++", "Java", "JavaScript"),
        ("Which company developed Java?", "Microsoft", "Oracle", "Google", "IBM", "Oracle"),
        ("CSS is used for?", "Styling web pages", "Creating database", "Backend scripting", "Networking", "Styling web pages"),
        ("Which of the following is a Python web framework?", "Django", "Laravel", "React", "Node.js", "Django"),
        ("What does SQL stand for?", "Structured Query Language", "Simple Query Language", "Sequential Query Logic", "None", "Structured Query Language"),
        ("Which of these is a version control system?", "Git", "Python", "HTML", "Docker", "Git"),
        ("Which is used to store key-value pairs in Python?", "List", "Tuple", "Dictionary", "Set", "Dictionary"),
        ("What is the output of 3 ** 2 in Python?", "6", "9", "8", "5", "9")
    ]
    cur.executemany("INSERT INTO questions VALUES (NULL,?,?,?,?,?,?)", questions_to_insert)
    conn.commit()

cur.execute("SELECT question, option1, option2, option3, option4, answer FROM questions")
questions = cur.fetchall()
conn.close()

# --------------------------
# 2. Quiz Function
# --------------------------
def ask_question(q):
    print("\nQuestion:", q[0])
    print("A)", q[1])
    print("B)", q[2])
    print("C)", q[3])
    print("D)", q[4])
    
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    correct_option = q[5]

    if (answer == "A" and correct_option == q[1]) or \
       (answer == "B" and correct_option == q[2]) or \
       (answer == "C" and correct_option == q[3]) or \
       (answer == "D" and correct_option == q[4]):
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! Correct answer: {correct_option}")
        return False

# --------------------------
# 3. Main Quiz Loop with Single Progress Bar
# --------------------------
print("\nStarting the quiz...")
score = 0
total_questions = len(questions)
seconds_per_question = 30

# One single progress bar for all questions
for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i} of {total_questions}:")
    
    # Show progress bar for 30 seconds per question
    for _ in tqdm(range(seconds_per_question), desc="Time remaining for this question", ncols=70):
        time.sleep(1)
    
    # Ask the question after countdown
    if ask_question(q):
        score += 1

print(f"\nYour final score: {score}/{total_questions}")
