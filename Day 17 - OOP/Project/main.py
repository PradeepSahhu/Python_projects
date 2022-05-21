from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]  # In case of other data it is "text"
    question_answer = question["correct_answer"]  # In case of other data it is "answer"
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("Congratulations!!! You've completed the quiz ")
print(f"your total score is {quiz.score}/{quiz.question_number}")



