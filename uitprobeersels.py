menu_error = "Please make a choice from the menu."

options_2 = {
        1: "1 - Change first name\n",
        2: "2 - Change last name\n",
        9: "9 - Back to main menu\n",
    }


def __make_question(options):
    question = ""
    for value in options.values():
        question += value

    question += "Your choice: "

    return question


def ask_choice(option_set):
    question = __make_question(option_set)
    while True:
        try:
            choice = int(input(question))
            if choice not in option_set.keys():
                raise ValueError
            return choice
        except ValueError:
            print(menu_error)


ask_choice(options_2)

