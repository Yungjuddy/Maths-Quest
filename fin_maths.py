import random
import time

def generate_question():
    """Generate a math question with random operands and operator."""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*', '/'])
    question = f"What is {a} {op} {b}?"
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    elif op == '/':
        answer = a / b
    return question, answer

def get_gender():
    """Get the user's gender."""
    while True:
        gender = input("Are you a boy or a girl? ")
        if gender.lower() in ('boy', 'girl'):
            return gender.lower()
        else:
            print("Invalid input. Please enter 'boy' or 'girl'.")

def appraise_answer(is_correct, gender):
    """Give an appraisal for the user's answer."""
    if is_correct:
        if gender == 'boy':
            return random.choice(['Good job, you got it right!', 'Well done, keep it up!', 'Excellent!', 'Great work!'])
        else:
            return random.choice(['Good girl, you got it right!', 'Well done, keep it up!', 'Excellent!', 'Great work!'])
    else:
        return random.choice(['Wrong answer. The correct answer is ___.', 'Better luck next time!', 'You can do better!', 'Try again!'])

def run_math_app():
    """Run the math app."""
    name = input("What is your name? ")
    gender = get_gender()
    num_questions = int(input("How many questions do you want to answer? "))
    questions = [generate_question() for _ in range(num_questions)]
    random.shuffle(questions)
    score = 0
    start_time = time.time()
    for question, answer in questions:
        user_answer = input(question)
        try:
            user_answer = float(user_answer)
            is_correct = user_answer == answer
            print(appraise_answer(is_correct, gender), f"The correct answer is {answer}.")
            if is_correct:
                score += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
    end_time = time.time()
    print(f"Final score: {score}/{num_questions}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    run_math_app()
