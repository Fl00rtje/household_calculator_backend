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
               f"Email:\n {self.email_address}"


class Data(User):
    def __init__(self, first_name, last_name, email_address):
        super().__init__(first_name, last_name, email_address)
        self.house = None
        self.car = None


class House:
    def __init__(self, rent_mortgage, service_costs):
        self.rent_mortgage = rent_mortgage
        self.service_costs = service_costs

    @property
    def total_costs(self):
        return self.rent_mortgage + self.service_costs

    def __str__(self):
        return f"Housing costs: €{self.total_costs} per month. \n" \
               f" - rent/mortgage: €{self.rent_mortgage} \n" \
               f" - service costs: €{self.service_costs}"


if __name__ == '__main__':
    # test setup
    user = Data("Flora", "Oceania", "flora.oceania@gmail.com")
    print(user)
    user.first_name = "Floor"
    print(user)

    house = House(10, 10)
    print(house)
    house.rent_mortgage = 20
    print(house)

    user.house = house
    user.house.rent_mortgage = 30
    print(user.house.rent_mortgage)