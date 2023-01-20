from data import question_data


class Question():

    def __init__(self, question_dict):
        self._question = question_dict['question']
        self._answer = question_dict['correct_answer']

    def __str__(self):
        return self._question

    def check_answer(self, user_input):
        return user_input == self._answer

    def get_correct_answer(self):
        return self._answer
