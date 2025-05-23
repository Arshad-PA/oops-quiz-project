class QuizBrian:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_question(self):

        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_quest(self):
        current_quest = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'{self.question_number}{current_quest.text}(True/False) : ')
        self.check_answer( current_quest.answer,user_answer)

    def check_answer(self, answer, user_input):
        if answer.lower() == user_input.lower():
            print("That's correct answer")
            self.score += 1
        else:
            print("that's Wrong")
        print(f'Correct answer is {answer}')
        print(f"your score is{self.score}/{self.question_number} ")