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
               f" - total: {self.total_costs} per month"


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


# --- ASKING THE USER FOR INPUT ---
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


# def car_details():
#     """
#     Function asks the user input for the car: insurance, road taxes, parking permit and road assistance.
#     :return: Returns a car object with the given input.
#     """
#     insurance = ask_amount("How much do you pay for your car insurance?")
#     road_taxes = ask_amount("How much do you pay for road taxes?")
#     parking_permit = cost_parking_permit()
#     road_assistance = cost_road_assistance()
#     return Car(insurance, road_taxes, parking_permit, road_assistance)


if __name__ == '__main__':
    user = user_details()
    user_data = Data(user)
    house = housing_details()
    user_data.house = house
    print(user_data)