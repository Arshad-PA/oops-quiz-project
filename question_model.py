from data import question_data


class Question:
    def __init__(self, question, answer):
        self.test = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.test} | Answer: {self.answer}"

