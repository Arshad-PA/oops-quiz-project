from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []

for item in question_data:
    quest = item["text"]
    ans = item["answer"]
    new_quest = Question(quest,ans)
    question_bank.append(new_quest)

start_quiz = Brain(question_bank)
start_quiz.next_question()

