
class Host():

    _correct_num = 0

    def __init__(self, quiz_list):
        self._questions = quiz_list

    def quiz(self):
        for i in range(len(self._questions)):
            question_num = i + 1
            question = self._questions[i]
            print(f"Q{question_num}: {question}")
            user_answer = input("True or False?: ")

            if question.check_answer(user_answer):
                self._correct_num += 1
                print(
                    "Correct! Current score: {}/{}".format(self._correct_num, question_num))

            else:
                print("Incorrect! The correct answer is {}, Current score: {}/{}"
                      .format(question.get_correct_answer(), self._correct_num, question_num))

        print(
            f"You have answered all questions. Your total score is {self._correct_num}/{len(self._questions)}")
