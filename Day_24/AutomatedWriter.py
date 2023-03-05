class AutomatedWriter():

    def __init__(self) -> None:

        with open("./Input/Names/invited_names.txt", mode='r') as file:
            self._name_list = file.readlines()

        with open("./Input/Letters/starting_letter.txt", mode='r') as file:
            self._structure = file.read()

    def generate_message(self) -> None:
        for names in self._name_list:
            stripped_name = names.strip()

            with open("./Output/ReadyToSend/{}".format("To_" + stripped_name), "w") as file:
                file.write(self._structure.replace("[name]", stripped_name))
