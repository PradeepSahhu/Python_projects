class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # Default value of the question number.
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)  # It will return either true or false.

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text}? (True/False)")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1

        else:
            print("you got it wrong")
        print(f"your Current score is {self.score}/{self.question_number}")
        print(f"Correct answer is: {correct_answer}")
        print("\n")





