from tkinter import *
from tkinter import messagebox
import random

questions = [
    {
        'question': 'What is the capital of India?',
        'options': ['Delhi', 'London', 'Berlin'],
        'answer': 'Delhi'
    },
    {
        'question': 'Which planet is known as the "Red Planet"?',
        'options': ['Jupiter', 'Venus', 'Mars'],
        'answer': 'Mars'
    },
    {
        'question': 'What is the normal temperature of human body?',
        'options': [' 45°C', ' 37°C', ' 28°C'],
        'answer': ' 37°C'
    }
]

score = 0
question_number = 0
current_question = None

def show_question():
    global current_question, question_number, score
    if question_number < 3:
        if not questions:
            play_again = messagebox.askyesno("Game Over", f"Your Total Score: {score}\nDo you want to play again?")
            if play_again:
                score = 0
                question_number = 0
                questions[:] = [q for q in questions_backup]
                show_question()
            else:
                root.destroy()
        else:
            current_question = random.choice(questions)
            question_label.config(text=current_question['question'])

            val1.set(0)
            val2.set(0)
            val3.set(0)

            option1.config(text=current_question['options'][0])
            option2.config(text=current_question['options'][1])
            option3.config(text=current_question['options'][2])

            question_number += 1
            questions.remove(current_question)
    else:
        play_again = messagebox.askyesno("Game Over", f"Your Total Score: {score}\nDo you want to play again?")
        if play_again:
            score = 0
            question_number = 0
            questions[:] = [q for q in questions_backup]
            show_question()
        else:
            root.destroy()

def check_answer():
    global score
    user_answer = ''
    if val1.get():
        user_answer = current_question['options'][0]
    elif val2.get():
        user_answer = current_question['options'][1]
    elif val3.get():
        user_answer = current_question['options'][2]

    if user_answer == current_question['answer']:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text="Incorrect! The correct answer is: " + current_question['answer'], fg="red")

    score_label.config(text="Score: " + str(score))
    show_question()

root = Tk()
root.title("Quiz Game Application")
root.config(bg='skyblue')

question_frame = Frame(root)
question_frame.pack(pady=10)

question_label = Label(question_frame, font=("Arial", 12))
question_label.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option_frame = Frame(root)
option_frame.pack(pady=5)

option1 = Checkbutton(option_frame, variable=val1, text='Option1')
option1.pack(side=LEFT, padx=5)
option2 = Checkbutton(option_frame, variable=val2, text='Option2')
option2.pack(side=LEFT, padx=5)
option3 = Checkbutton(option_frame, variable=val3, text='Option3')
option3.pack(side=LEFT, padx=5)

submit_button = Button(root, command=check_answer, text="Submit", 
                     font=("Arial", 12), bg='lightgreen', fg='black')
submit_button.pack(pady=10)

feedback_label = Label(root, font=("Arial", 12))
feedback_label.pack()

score_label = Label(root, font=("Arial", 12))
score_label.pack()

# Make a backup of the original questions to reset the game later
questions_backup = [q for q in questions]

show_question()

root.mainloop()
