class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def change_first_name(self, new_first_name):
        self.first_name = new_first_name
        print(f"Your first name has been updated to: {self.first_name}")

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name
        print(f"Your first name has been updated to: {self.last_name}")

    def change_email(self, new_email):
        self.email_address = new_email
        print(f"Your email address has been updated to: {self.email_address}")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"User:\n {self.fullname}\n" \
               f"Email:\n {self.email_address}"


class House:
    def __init__(self, rent_mortgage, service_costs):
        self.rent_mortgage = rent_mortgage
        self.service_costs = service_costs

    @property
    def total_costs(self):
        return self.rent_mortgage + self.service_costs

    def __str__(self):
        return f"Your housing details:\n" \
               f" - rent/mortgage: €{self.rent_mortgage} \n" \
               f" - service costs: €{self.service_costs}\n" \
               f" - total: €{self.total_costs} per month"


class Car:
    def __init__(self, insurance, road_taxes, parking_permit, road_assistance):
        self.insurance = insurance
        self.road_taxes = road_taxes
        self.parking_permit = parking_permit
        self.road_assistance = road_assistance

    @property
    def total_costs(self):
        return self.insurance + self.road_taxes + self.parking_permit + self.road_assistance

    def __str__(self):
        return f"Your car details:\n" \
               f" - insurance: €{self.insurance}\n" \
               f" - road taxes: €{self.road_taxes}\n" \
               f" - parking permit: €{self.parking_permit}\n" \
               f" - road assistance: €{self.road_assistance}\n" \
               f" - total: €{self.total_costs} per month"


class Data:
    def __init__(self, user):
        self.user = user
        self.house = None
        self.car = None

    def housing_details(self):
        if not self.house:
            return "No housing details available."
        return self.house

    def car_details(self):
        if not self.car:
            return "No car details available"
        return self.car

    def __str__(self):
        return f"{self.user}\n"\
               f"{'House: no details available.' if not self.house else self.house}\n" \
               f"{'Car: no details available.' if not self.car else self.car}"


# --- DATA ---
def ask_amount(question):
    """
    Asks the user for input on how much they pay and takes the input.
    :param question: the question that is displayed to the user.
    For example: How much do you pay for rent / mortgage?
    :return: the number (cost) the user entered as an integer.
    """
    while True:
        try:
            number = int(input(question + " "))
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print(f"Please enter a positive number (no decimals).")


def yes_or_no(question):
    """
    Function asks a yes or no question to the user.
    :param question: the question that is displayed to the user.
    :return: Returns True or False
    """
    while True:
        try:
            answer = input(f'{question} (y/n) ').lower()
            if answer == 'y':
                return True
            elif answer == 'n':
                return False
            else:
                raise ValueError
        except ValueError:
            print("Please enter 'y' or 'n'")


# --- ASKING THE USER FOR INPUT ---
menu_error = "Please make a choice from the menu."


def user_details():
    """
    Function asks the user input on first name, last name and email address.
    :return: Returns a user object with the given input.
    """
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email_address = input("What is your email address? ")
    return User(first_name, last_name, email_address)


def housing_details():
    """
    Function asks the user input for housing: rent/mortgage and service costs.
    :return: Returns a house object with the given input.
    """
    rent_mortgage = ask_amount("How much do you pay for rent / mortgage?")
    service_costs = ask_amount("How much do you pay for service costs?")
    return House(rent_mortgage, service_costs)


def cost_parking_permit():
    """
    Function asks the user about having a parking permit and if yes, the costs.
    :return: Returns the cost of the parking permit as an integer.
    """
    if yes_or_no("Do you have a parking permit?"):
        return ask_amount("How much do you pay for your parking permit?")
    return 0


def cost_road_assistance():
    """
    Function asks the user about having a road assistance and if yes, the costs.
    :return: Returns the cost of the road assistance as an integer.
    """
    if yes_or_no("Do you have road assistance?"):
        return ask_amount("How much do you pay for road assistance?")
    return 0


def car_details():
    """
    Function asks the user input for the car: insurance, road taxes, parking permit and road assistance.
    :return: Returns a car object with the given input.
    """
    insurance = ask_amount("How much do you pay for your car insurance?")
    road_taxes = ask_amount("How much do you pay for road taxes?")
    parking_permit = cost_parking_permit()
    road_assistance = cost_road_assistance()
    return Car(insurance, road_taxes, parking_permit, road_assistance)


def __make_question(options):
    """
    Generates a string with menu options that are displayed to the user from the options variable.
    :param options: dictionary with menu options.
    :return: the menu options as a string.
    """
    question = ""
    for value in options.values():
        question += value

    question += "Your choice: "

    return question


def ask_choice(options):
    """
    Displays the menu options to the user and takes the input from the user.
    :param options: dictionary with menu options.
    :return: the choice user made from the menu as an integer.
    """
    question = __make_question(options)
    while True:
        try:
            choice = int(input(question))
            if choice not in options.keys():
                raise ValueError
            return choice
        except ValueError:
            print(menu_error)


# --- PERSONAL SUBMENU ---
def run_personal_submenu():
    """
    This is the starting point of the personal submenu.
    From here you can choose from the personal submenu actions and get redirected to perform them.
    :return: returns nothing.
    """
    print("In run_personal_submenu")
    print(user_data.user)
    options = generate_personal_submenu_options()
    choice = ask_choice(options)
    process_choice_personal_submenu(choice)


def generate_personal_submenu_options():
    """
    Function generates the menu options that will be displayed to the user.
    Since the menu options aren't changing based upon the user data at the moment, it could also be a variable.
    :return: Returns the generated menu options as a string.
    """
    options = {
        1: "1 - Change first name\n",
        2: "2 - Change last name\n",
        3: "3 - Change email address\n",
        9: "9 - Back to main menu\n",
    }

    return options


def process_choice_personal_submenu(choice):
    """
    Function redirects the user based on the choice made from the personal submenu options.
    :param choice: the choice (integer) the user made form the personal submenu.
    :return: returns nothing.
    """
    print("In personal_submenu_choice")

    while choice != 9:
        if choice == 1:
            new_first_name = input("What is your first name? ")
            user_data.user.change_first_name(new_first_name)
        elif choice == 2:
            new_last_name = input("What is your last name? ")
            user_data.user.change_last_name(new_last_name)
        elif choice == 3:
            new_email = input("What is your email address? ")
            user_data.user.change_email(new_email)
        else:
            print(menu_error)
        print(user_data.user)
        options = generate_personal_submenu_options()
        choice = ask_choice(options)


# --- GENERAL SUBMENU OPTIONS ---
def generate_submenu_options(utility):
    """
    Function generates the submenu options based on the chosen utility (f.e. "house" or "car").
    :param utility: string containing the origin of the costs.
    :return: returns the submenu options as a string.
    """
    if utility == "house":
        utility_present = user_data.house
    else:
        utility_present = user_data.car

    options = {
        1: f"1 - Add {utility}\n",
        9: f"9 - Back to main menu\n"
    }

    if utility_present:
        options = {
            1: f"1 - Change {utility}\n",
            2: f"2 - Delete {utility}\n",
            9: f"9 - Back to main menu\n"
        }

    return options


# --- HOUSE SUBMENU ---
def run_house_submenu(utility):
    """
    This is the starting point of the house submenu.
    From here you can choose from the house submenu and get redirected to your choice.
    :return: returns nothing.
    """
    print("In run_house_submenu")
    print(user_data.housing_details())
    options = generate_submenu_options(utility)
    choice = ask_choice(options)
    process_choice_house_submenu(choice)


def process_choice_house_submenu(choice):
    """
    Function redirects the user based on the choice made from the house submenu options.
    :param choice: the choice (integer) the user made form the house submenu.
    :return: returns nothing.
    """
    print("In house_submenu_choice")

    while choice != 9:
        if choice == 1:
            house = housing_details()
            user_data.house = house
        elif choice == 2:
            user_data.house = None
        else:
            print(menu_error)
        print(user_data.housing_details())
        options = generate_submenu_options("house")
        choice = ask_choice(options)


# --- CAR SUBMENU ---
def run_car_submenu(utility):
    """
    This is the starting point of the car submenu.
    From here you can choose from the car submenu and get redirected to your choice.
    :return: returns nothing.
    """
    print("In run_car_submenu")
    print(user_data.car_details())
    options = generate_submenu_options(utility)
    choice = ask_choice(options)
    process_choice_car_submenu(choice)


def process_choice_car_submenu(choice):
    """
    Function redirects the user based on the choice made from the car submenu options.
    :param choice: the choice (integer) the user made form the car submenu.
    :return: returns nothing.
    """
    print("In process_choice_car_submenu")

    while choice != 9:
        if choice == 1:
            car = car_details()
            user_data.car = car
        elif choice == 2:
            user_data.car = None
        else:
            print(menu_error)
        print(user_data.car_details())
        options = generate_submenu_options("car")
        choice = ask_choice(options)


# ----- MAIN MENU -----
def run_main_menu():
    """
    This is the starting point of the application. The function runs the main menu.
    From here you can go into the submenu's.
    From the submenu's you can return to the main menu.
    :return: returns nothing.
    """
    print("In run_main_menu")
    options = generate_main_menu_options()
    choice = ask_choice(options)
    process_choice_main_menu(choice)


def generate_main_menu_options():
    """
    Function generates the menu options that will be displayed to the user based on existing user data.
    :return: Returns the generated menu options as a string.
    """
    print("In main_menu_options")
    options = {
        "user": "View/Change/Delete Personal details",
        "house": "Register housing details",
        "car": "Register car details",
    }

    if user_data.house:
        options["house"] = "View/Change/Delete housing details"

    if user_data.car:
        options["car"] = "View/Change/Delete car details"

    menu_options = {
        1: f"1 - {options['user']}\n",
        2: f"2 - {options['house']}\n",
        3: f"3 - {options['car']}\n",
        9: f"9 - Exit\n"
    }

    return menu_options


def process_choice_main_menu(choice):
    """
    Function redirects the user based on the choice made from the menu options.
    :param choice: the choice (integer) the user made form the menu.
    :return: returns nothing
    """
    print("In main_menu_choice")

    while choice != 9:
        if choice == 1:
            print("run_personal_submenu()")
            run_personal_submenu()
        elif choice == 2:
            print("run_house_submenu(utility)")
            utility = "house"
            run_house_submenu(utility)
        elif choice == 3:
            print("run_car_submenu(utility)")
            utility = "car"
            run_car_submenu(utility)
        else:
            print(menu_error)
        options = generate_main_menu_options()
        choice = ask_choice(options)


if __name__ == '__main__':
    # user = user_details()
    # user_data = Data(user)
    # house = housing_details()
    # user_data.house = house
    # car = car_details()
    # user_data.car = car
    # print(user_data)

    user = User("Flora", "Oceania", "flora.oceania@gmail.com")
    user_data = Data(user)
    run_main_menu()