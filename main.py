from data import question_data
from question_model import Questions
from quiz_brain import QuizBrian
i = 0
new_question = []
for questions in question_data:
    question = questions['text']
    answer = questions['answer']
    new_q = Questions(question, answer)
    new_question.append(new_q)


brain = QuizBrian(new_question)
while brain.still_question():
    brain.next_quest()
print(f'Game over \n Your Final score is {brain.score}/{brain.question_number} ')