import json
import os
from random import choices
from ascii_art import vs

dirname = os.path.dirname(__file__)
file = open(os.path.join(dirname, "Dummy_data.json"))
data = json.load(file)["ctRoot"]

def random_select():
    """Randomly select 2 users from data and put them into list"""
    return choices(data, k=2)
    
def print_versus(compare_list):
    print(f"Compare A: {compare_list[0]['name']}, {compare_list[0]['description']}")
    print(vs)
    print(f"Against B: {compare_list[1]['name']}, {compare_list[1]['description']}")
    user_input = input("Who has more followers? 'A' or 'B'?: ")
    return user_input

def index_of_winner(compare_list):
    """return the index of the person who has the higher amount of followers"""
    def myFunc(user):
        return user["followers"]
    return compare_list.index(max(compare_list, key=myFunc))

def check_answer(compare_list, answer):
    """return true if the player answered the correct index"""
    return index_of_winner(compare_list) == answer

if __name__ == '__main__':
    print(print_versus(random_select()))
#print(index_of_winner(random_select()))