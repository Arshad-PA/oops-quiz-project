
class Brain:
    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f'{self.question_number}:{current_question} (TRUE/FALSE)')


