class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"User:\n {self.fullname}\n" \
               f"Email:\n {self.email_address}\n"


class Data(User):
    def __init__(self, first_name, last_name, email_address):
        super().__init__(first_name, last_name, email_address)
        self.house = None
        self.car = None

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


def ask_amount(question):
    while True:
        try:
            number = int(input(question + " "))
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print(f"Please enter a positive number (no decimals).")


def housing_details():
    while True:
        try:
            rent_mortgage = ask_amount("How much do you pay for rent / mortgage?")
            service_costs = ask_amount("How much do you pay for service costs?")
            user.house = House(rent_mortgage, service_costs)
            break
        except AttributeError:
            print("Something went wrong. Please try again.")


def run_main_menu():
    print("In run_main_menu")
    options = main_menu_options()
    # validate choice!!
    choice = int(input(options))
    main_menu_choice(choice)


def run_personal_menu():
    print("In run_personal_menu")
    print(user)
    options = personal_submenu_options()
    choice = int(input(options))
    personal_submenu_choice(choice)


def run_house_submenu():
    print("In run_house_submenu")
    print(user.house)
    options = house_submenu_options()
    choice = int(input(options))
    house_submenu_choice(choice)


def house_submenu_choice(choice):
    print("In house_submenu_choice")

    while choice != 9:
        if choice == 1:
            housing_details()
        elif choice == 2:
            user.house = None
        print(user.house)
        options = house_submenu_options()
        choice = int(input(options))


def personal_submenu_choice(choice):
    print("In personal_submenu_choice")

    while choice != 9:
        if choice == 1:
            print("Change first name")
        elif choice == 2:
            print("Change last name")
        elif choice == 3:
            print("Change email address")
        print(user)
        options = personal_submenu_options()
        choice = int(input(options))


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

    menu_options = f"1 - {options['user']}\n" \
                   f"2 - {options['house']}\n" \
                   f"3 - {options['car']}\n" \
                   f"9 - Exit\n" \
                   f"Your choice: "

    return menu_options


def main_menu_choice(choice):
    print("In main_menu_choice")

    while choice != 9:
        if choice == 1:
            run_personal_menu()
        elif choice == 2:
            run_house_submenu()
        elif choice == 3:
            print("Car details")
        options = main_menu_options()
        choice = int(input(options))


def personal_submenu_options():
    submenu_options = f"1 - Change first name\n" \
                      f"2 - Change last name\n" \
                      f"3 - Change email address\n" \
                      f"9 - Back to main menu\n" \
                      f"Your choice: "

    return submenu_options


def house_submenu_options():
    # make this a general submenu with a variable house/car/etc?
    submenu_options = f"1 - Add house\n" \
                   f"9 - Back to main menu\n" \
                   f"Your choice: "

    if user.house:
        submenu_options = f"1 - Change house\n" \
                       f"2 - Delete house\n" \
                       f"9 - Back to main menu\n" \
                       f"Your choice: "

    return submenu_options


if __name__ == '__main__':
    # # test setup
    user = Data("Flora", "Oceania", "flora.oceania@gmail.com")
    # print(user)
    # user.first_name = "Floor"
    # print(user)
    #
    house = House(10, 10)
    # # print(house)
    # house.rent_mortgage = 20
    # # print(house)
    #
    user.house = house
    # user.house.rent_mortgage = 30
    # print(user.house)
    # print(user.car)

    run_main_menu()
