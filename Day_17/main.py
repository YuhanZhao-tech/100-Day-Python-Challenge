from data import question_data
from Question import Question
from Host import Host

question_list = []
for question in question_data:
    question_list.append(Question(question))

host = Host(question_list)
host.quiz()
