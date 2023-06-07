# Maths-Quest
A customizable math quiz game that allows users to set the number of questions to answer


import random
import pygame
import tkinter as tk
from tkinter import messagebox, simpledialog


class MathQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Quiz App")
        self.geometry("400x300")

        # widgets
        self.num_questions_label = tk.Label(self, text="Number of Questions:")
        self.num_questions_entry = tk.Entry(self)
        self.start_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)

        # layout
        self.num_questions_label.pack(pady=10)
        self.num_questions_entry.pack()
        self.start_button.pack(pady=20)

    def bring_question(self):
        a = random.randrange(1, 11)
        b = random.randrange(1, 11)
        signs = ["*", "/", "+", "-"]
        sign = random.choice(signs)
        question = str(a) + " " + sign + " " + str(b) + " = "
        answer = eval(f"{str(a)} {sign} {str(b)}")
        return question, answer

    def start_quiz(self):
        try:
            num_questions = int(self.num_questions_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        questions = []
        for i in range(num_questions):
            question, answer = self.bring_question()
            questions.append((question, answer))

        score = 0
        for question, answer in random.sample(questions, k=num_questions):
            user_answer = simpledialog.askstring("Question", question)
            try:
                user_answer = int(user_answer)
            except ValueError:
                try:
                    user_answer = float(user_answer)
                except ValueError:
                    user_answer = None
            if user_answer == answer:
                messagebox.showinfo("Correct!", "Great job!")
                score += 1
            else:
                messagebox.showerror("Incorrect", f"Sorry, the answer was {answer} try better.")

        messagebox.showinfo("Quiz Complete", f"Your final score is {score}/{num_questions}.")

if __name__ == "__main__":
    app = MathQuizApp()
    app.mainloop()
