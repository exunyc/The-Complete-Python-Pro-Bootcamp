class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        text = question.text
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {text} (True/False)?: ")
        self.check_answer(user_input, question.answer)
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def still_has_questions(self):
        if self.question_number != len(self.questions_list):
            return True
        else:
            return False

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"Incorrect, the correct answer is: {correct_answer}.")

    def final_score(self):
        print(f"You've completed the quiz! Final score: {self.score}/{len(self.questions_list)}")