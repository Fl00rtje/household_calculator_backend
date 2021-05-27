class User:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.house = None

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, value):
        if value:
            self.__house = value
        else:
            self.__house = None

    @house.deleter
    def house(self):
        self.__house = None

    def house_present(self):
        if not self.house:
            return False
        else:
            return True

    def view_house(self):
        if not self.house:
            print("No housing details available.")
        else:
            print(self.house)

    def __str__(self):
        return f"User:\n {self.first_name} {self.last_name}\n" \
               f"Email:\n {self.email_address}\n" \
               f"Housing details registered:\n {'No' if not self.house else 'Yes'}"


class House:
    def __init__(self, rent_mortgage, service_costs):
        self.rent_mortgage = rent_mortgage
        self.service_costs = service_costs
        self.total_costs = self.total_costs()

    @property
    def rent_mortgage(self):
        return self.__rent_mortgage

    @rent_mortgage.setter
    def rent_mortgage(self, amount):
        self.__rent_mortgage = amount

    # @rent_mortgage.deleter
    # def rent_mortgage(self):
    #     self.__rent_mortgage = None

    def total_costs(self):
        return self.rent_mortgage + self.service_costs

    def __str__(self):
        return f"Housing costs: €{self.total_costs} per month. \n" \
               f" - rent/mortgage: €{self.rent_mortgage} \n" \
               f" - service costs: €{self.service_costs}"


def ask_amount(question):
    while True:
        try:
            number = int(input(question + " "))
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print(f"Please enter a positive number (no decimals).")


def user_details():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email_address = input("What is your email address? ")
    return User(first_name, last_name, email_address)


def housing_details():
    while True:
        try:
            rent_mortgage = ask_amount("How much do you pay for rent / mortgage?")
            service_costs = ask_amount("How much do you pay for service costs?")
            user.house = House(rent_mortgage, service_costs)
            break
        except AttributeError:
            print("Something went wrong. Please try again.")


def menu():
    add_change = "Add house"
    if user.house_present():
        add_change = "Change house"

    choices = f"0 - Personal Details\n" \
              f"1 - {add_change}\n" \
              f"2 - View House\n" \
              f"3 - Delete House\n" \
              f"9 - Exit\n" \
              "Your choice: "

    return choices


if __name__ == '__main__':
    # test setup
    user = User("Flora", "Oceania", "flora.oceania@gmail.com")
    print(user)

    # interface setup
    print("Welcome to Flora's household calculator!")
    print("Please make a choice from the menu:")
    # user = user_details()
    # print(user)
    menu_options = menu()
    choice = int(input(menu_options))

    while choice != 9:
        if choice == 0:
            print(user)
        elif choice == 1:
            housing_details()
            print(user)
        elif choice == 2:
            user.view_house()
        elif choice == 3:
            if user.house:
                del user.house
            else:
                print("No housing details to delete.")
            print(user)
        menu_options = menu()
        choice = int(input(menu_options))
