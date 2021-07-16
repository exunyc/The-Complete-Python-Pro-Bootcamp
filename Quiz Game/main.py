from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for _ in question_data:
    question = _["question"]
    answer = _["correct_answer"]
    question_answer = Question(question, answer)
    question_bank.append(question_answer)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

quiz_brain.final_score()