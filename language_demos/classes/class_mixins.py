""" mixins """

from __future__ import annotations

# import json
from typing import Any
import jsonpickle
import yaml

class ItemListJsonMixin:
    """ item list json mixin class """

    _items: Any

    # def to_json(self):
    #     return json.dumps(self._items)

    def to_json(self) -> Any:
        """ to json """
        return jsonpickle.encode(self._items)


class ItemListYamlMixin:
    """ item list yaml mixin """

    _items: Any

    def to_yaml(self) -> Any:
        """ to yaml """
        return yaml.dump(self._items)   

class ItemList:
    """ item list """

    _items: Any

    def __init__(self) -> None:
        self._items = []


class Person:
    """ person class """

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self) -> str:
        """ person full name """
        return self.first_name + " " + self.last_name


class PeopleList(ItemList, ItemListJsonMixin, ItemListYamlMixin):
    """ people list """

    def __add__(self, person: Person) -> PeopleList:
        # __dict__ used for the built-in JSON module
        # self._items.append(person.__dict__)

        # jsonpickle package can serialize custom objects
        self._items.append(person)
        return self


people = PeopleList()

people += Person('Bob', 'Smith')
people += Person('Sally', 'Jones')

print(people.to_json())
print(people.to_yaml())
