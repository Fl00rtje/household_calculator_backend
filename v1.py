class User:
    # NO_CAR = f"{self.first_name} {self.last_name} doesn't have a car."

    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.house = "No housing details registered."
        self.car = "unknown"

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, value):
        if value:
            self.__house = value
        else:
            self.__house = "No housing details registered."

    @house.deleter
    def house(self):
        self.__house = "No housing details registered."

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, value):
        if value:
            self.__car = value
        else:
            self.__car = f"{self.first_name} {self.last_name} doesn't have a car."

    @car.deleter
    def car(self):
        self.__car = f"{self.first_name} {self.last_name} doesn't have a car."

    def __str__(self):
        return f"User:\n {self.first_name} {self.last_name} \n Email: {self.email_address} \n " \
               f"Car details: {self.car} \n Housing details: {self.house}"


class House:
    def __init__(self, monthly_pay, service_costs):
        self.monthly_pay = monthly_pay
        self.service_costs = service_costs
        self.total_costs = self.total_costs()

    def total_costs(self):
        return self.monthly_pay + self.service_costs

    def __str__(self):
        return f"€{self.total_costs} per month. \n" \
               f" - rent/mortgage: €{self.monthly_pay} \n" \
               f" - service costs: €{self.service_costs}\n"


class Car:
    def __init__(self, insurance, road_taxes, parking_permit, road_assistance):
        self.insurance = insurance
        self.road_taxes = road_taxes
        self.parking_permit = parking_permit
        self.road_assistance = road_assistance
        self.total_costs = self.total_costs()

    def total_costs(self):
        return self.insurance + self.road_taxes + self.parking_permit + self.road_assistance

    def __str__(self):
        return f"€{self.total_costs} per month. \n" \
               f" - insurance: €{self.insurance}\n" \
               f" - road taxes: €{self.road_taxes}\n" \
               f" - parking permit: €{self.parking_permit}\n" \
               f" - road assistance: €{self.road_assistance}\n"


def yes_or_no(question):
    while True:
        answer = input(f'{question} (y/n) ').lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Please enter y or n")


def ask_amount(question):
    while True:
        try:
            answer = int(input(question + " "))
            return answer
        except ValueError:
            print("Please enter a number (no decimals)")


def user_details():
    print("We are going to start with registering your details:")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email_address = input("What is your email address? ")
    return User(first_name, last_name, email_address)


def housing_details():
    print("Let's add your costs related to housing:")
    monthly_costs = ask_amount("How much do you pay for rent / mortgage?")
    service_costs = ask_amount("How much do you pay for service costs?")
    user.house = House(monthly_costs, service_costs)


def cost_parking_permit():
    if yes_or_no("Do you have a parking permit?"):
        return ask_amount("How much do you pay for your parking permit?")
    return 0


def cost_road_assistance():
    if yes_or_no("Do you have road assistance?"):
        return ask_amount("How much do you pay for road assistance?")
    return 0


def car_details():
    insurance = ask_amount("How much do you pay for your car insurance?")
    road_taxes = ask_amount("How much do you pay for road taxes?")
    parking_permit = cost_parking_permit()
    road_assistance = cost_road_assistance()
    return insurance, road_taxes, parking_permit, road_assistance


def menu():

    choices = f"Please choose one of the following options:\n" \
                    f"1 - Add house\n" \
                    f"2 - Delete house\n" \
              f"3 - Show house\n" \
                    f"9 - Exit\n" \
                    f"Your choice: "

    return choices


if __name__ == '__main__':
    # test setup
    user = User("Floor", "Harmsen", "floor.harmsen@gmail.com")
    # housing_details = (735, 15)
    # car_details = (38, 39, 0, 10)

    # interface setup
    print("Welcome to Flora's household calculator!")
    # user = user_details()

    menu_options = menu()
    choice = int(input(menu_options))

    while choice != 9:
        if choice == 1:
            print("1 - Add housing details")
            housing_details()
            print(user.house)
        elif choice == 2:
            print("2 - Delete housing details.")
            del user.house
            print(user.house)
        elif choice == 3:
            print("Here are your housing details:")
            print(user.house)
        menu_options = menu()
        choice = int(input(menu_options))

    # if yes_or_no("Do you have a car?"):
    #     # car_details = car_details()
    #     user.car = Car(*car_details)
    # else:
    #     user.car = False
    # print(user)
    # print(user.car.total_costs)
    # print(user.house)
    # print(user.car)

    # del user.car
    #
    # print(user)
    # print(user.car)
