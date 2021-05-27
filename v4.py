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


def user_details():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email_address = input("What is your email address? ")
    return User(first_name, last_name, email_address)


if __name__ == '__main__':
    user = user_details()
    user_data = Data(user)
    print(user_data)