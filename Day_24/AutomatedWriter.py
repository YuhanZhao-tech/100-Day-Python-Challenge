class AutomatedWriter():

    def __init__(self) -> None:

        with open("./Input/Names/invited_names.txt", mode='r') as file:
            self._name_list = file.readlines()

        with open("./Input/Letters/starting_letter.txt", mode='r') as file:
            self._structure = file.read()

    def generate_message(self) -> None:
        for names in self._name_list:
            with open("./Output/ReadyToSend/{}".format("To_"+names.strip()), "w") as file:
                file.write(self._structure.replace("[name]", names.strip()))
