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

    def personal_details(self):
        return f"User:\n {self.fullname}\n"\
               f"Email:\n {self.email_address}\n"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"User:\n {self.fullname}\n" \
               f"Email:\n {self.email_address}"


class Data(User):
    def __init__(self, first_name, last_name, email_address):
        super().__init__(first_name, last_name, email_address)
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
        return super(Data, self).__str__() + \
               f"{'House: no details available.' if not self.house else self.house}\n" \
               f"{'Car: no details available.' if not self.car else self.car}"


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
               f" - total: {self.total_costs} per month"


# (global) variables
menu_error = "Please make a choice from the menu."


# to do:
# find out why I don't have to pass the variables to the functions (like menu_error)
# include the car


# --- CHECKING DATA ---
def __make_question(options):
    question = ""
    for value in options.values():
        question += value

    question += "Your choice: "

    return question


def ask_amount(question):
    while True:
        try:
            number = int(input(question + " "))
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print(f"Please enter a positive number (no decimals).")


def ask_choice(options):
    question = __make_question(options)
    while True:
        try:
            choice = int(input(question))
            if choice not in options.keys():
                raise ValueError
            return choice
        except ValueError:
            print(menu_error)


# --- ASKING DETAILS FROM USER ---
def housing_details():
    while True:
        try:
            rent_mortgage = ask_amount("How much do you pay for rent / mortgage?")
            service_costs = ask_amount("How much do you pay for service costs?")
            user.house = House(rent_mortgage, service_costs)
            break
        except AttributeError:
            print("Something went wrong. Please try again.")


# -- MAIN MENU ---
def run_main_menu():
    print("In run_main_menu")
    options = main_menu_options()
    choice = ask_choice(options)
    main_menu_choice(choice)


def main_menu_options():
    print("In main_menu_options")
    options = {
        "user": "View/Change/Delete Personal details",
        "house": "Register housing details",
        "car": "Register car details",
    }

    if user.house:
        options["house"] = "View/Change/Delete housing details"

    if user.car:
        options["car"] = "View/Change/Delete car details"

    menu_options = {
        1: f"1 - {options['user']}\n",
        2: f"2 - {options['house']}\n",
        3: f"3 - {options['car']}\n",
        9: f"9 - Exit\n"
    }

    return menu_options


def main_menu_choice(choice):
    print("In main_menu_choice")

    while choice != 9:
        if choice == 1:
            run_personal_submenu()
        elif choice == 2:
            utility = "house"
            run_house_submenu(utility)
        elif choice == 3:
            print("Car details")
            utility = "car"
            run_car_submenu(utility)
        else:
            print(menu_error)
        options = main_menu_options()
        choice = ask_choice(options)


# --- GENERAL SUBMENU ---
def submenu_options(utility):
    if utility == "house":
        utility_present = user.house
    else:
        utility_present = user.car

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


# --- PERSONAL SUBMENU ---
def run_personal_submenu():
    print("In run_personal_submenu")
    print(user.personal_details())
    options = personal_submenu_options()
    choice = ask_choice(options)
    personal_submenu_choice(choice)


def personal_submenu_options():
    options = {
        1: "1 - Change first name\n",
        2: "2 - Change last name\n",
        3: "3 - Change email address\n",
        9: "9 - Back to main menu\n",
    }

    return options


def personal_submenu_choice(choice):
    print("In personal_submenu_choice")

    while choice != 9:
        if choice == 1:
            print("Change first name")
            new_first_name = input("What is your first name? ")
            user.change_first_name(new_first_name)
        elif choice == 2:
            print("Change last name")
            new_last_name = input("What is your last name? ")
            user.change_last_name(new_last_name)
        elif choice == 3:
            print("Change email address")
            new_email = input("What is your email address? ")
            user.change_email(new_email)
        else:
            print(menu_error)
        print(user.personal_details())
        options = personal_submenu_options()
        choice = ask_choice(options)


# --- HOUSE SUBMENU ---
def run_house_submenu(utility):
    print("In run_house_submenu")
    print(user.housing_details())
    options = submenu_options(utility)
    choice = ask_choice(options)
    house_submenu_choice(choice)


def house_submenu_choice(choice):
    print("In house_submenu_choice")

    while choice != 9:
        if choice == 1:
            housing_details()
        elif choice == 2:
            user.house = None
        else:
            print(menu_error)
        print(user.housing_details())
        options = submenu_options("house")
        choice = ask_choice(options)


# --- CAR SUBMENU ---
def run_car_submenu(utility):
    print("In run_car_submenu")
    print(user.car_details())
    options = submenu_options(utility)
    choice = ask_choice(options)
    car_submenu_choice(choice)


def car_submenu_choice(choice):
    print("In car_submenu_choice")

    while choice != 9:
        if choice == 1:
            print("Change car")
        elif choice == 2:
            print("Delete car")
            user.car = None
        else:
            print(menu_error)
        print(user.car_details())
        options = submenu_options("car")
        choice = ask_choice(options)


if __name__ == '__main__':
    # # test setup
    user = Data("Flora", "Oceania", "flora.oceania@gmail.com")
    # print(user)
    # user.first_name = "Floor"
    # print(user)
    #
    house = House(10, 10)
    car = Car(40, 40, 10, 0)
    # # print(house)
    # house.rent_mortgage = 20
    # # print(house)
    #
    user.house = house
    user.car = car
    # user.house.rent_mortgage = 30
    # print(user.house)
    # print(user.car)

    run_main_menu()
