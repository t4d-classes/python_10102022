""" contact module """

class Address:
    """ address class """

    def __init__(
        self, street: str, city: str, state: str, zip_code: str) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def mailing(self) -> str:
        """ mailing method """
        return f"{self.street}\n{self.city}, {self.state} {self.zip_code}"


class PersonA:
    """ person a class """

    def __init__(
        self, first_name: str, last_name: str, street: str,
        city: str, state: str, zip_code: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address = Address(street, city, state, zip_code)

    def full_name(self) -> str:
        """ full name method """
        return self.first_name + " " + self.last_name

    def mailing(self) -> str:
        """ mailing method """
        return self.full_name() + "\n" + self.address.mailing()


class PersonB:
    """ person b class """

    def __init__(self, first_name: str, last_name: str, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def full_name(self) -> str:
        """ full name method """
        return self.first_name + " " + self.last_name

    def mailing(self) -> str:
        """ mailing method """
        return self.full_name() + "\n" + self.address.mailing()
