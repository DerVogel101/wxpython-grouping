from pydantic import BaseModel, field_validator, PositiveInt
from typing import Optional

class Person(BaseModel):
    id_: PositiveInt
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class Group(BaseModel):
    items: list[Person]

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __len__(self):
        return len(self.items)

    def append(self, value):
        self.items.append(value)

    def extend(self, values):
        self.items.extend(values)

    def insert(self, index, value):
        self.items.insert(index, value)

    def remove(self, value):
        self.items.remove(value)

    def pop(self, index=-1):
        return self.items.pop(index)

    def clear(self):
        self.items.clear()

    def index(self, value, start=0, end=None):
        return self.items.index(value, start, end)

    def count(self, value):
        return self.items.count(value)

    def sort(self, *, key=None, reverse=False):
        self.items.sort(key=key, reverse=reverse)

    def get_ids(self) -> set[PositiveInt]:
        return set([person.id_ for person in self.items])

    @field_validator('items', mode="before")
    def validate_items(cls, v):
        all_ids = [person.id_ for person in v]
        all_unique_ids = set(all_ids)
        if len(all_ids) != len(all_unique_ids):
            raise ValueError("Not all ids are Unique")
        return v


class Round(BaseModel):
    round_: dict[str, Group]

    def __getitem__(self, key):
        return self.round_[key]

    def __setitem__(self, key, value):
        self.round_[key] = value

    def __delitem__(self, key):
        del self.round_[key]

    def __len__(self):
        return len(self.round_)

    def __iter__(self):
        return iter(self.round_.items())

    def __contains__(self, item):
        return item in self.round_

    def __repr__(self):
        return f"Round(round_={self.round_!r})"

    def __str__(self):
        return str(self.round_)

    def __eq__(self, other):
        if isinstance(other, Round):
            return self.round_ == other.round_
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(frozenset(self.round_.items()))


    @field_validator('round_', mode="before")
    def validate_ids(cls, v: dict[str: Group]):
        items: tuple[Group] = tuple(v.values())
        len_items = 0
        ids = set()
        for item in items:
            ids_ = item.get_ids()
            len_items += len(ids_)
            ids |= ids_
        if len(ids) != len_items:
            raise ValueError("No Unique Groups in Round")
        return v


class Rounds(BaseModel):
    rounds: dict[int, Round]

    def __getitem__(self, key):
        return self.rounds[key]

    def __setitem__(self, key, value):
        self.rounds[key] = value

    def __delitem__(self, key):
        del self.rounds[key]

    def __len__(self):
        return len(self.rounds)

    def __iter__(self):
        return iter(self.rounds.items())

    def __contains__(self, item):
        return item in self.rounds

    def __repr__(self):
        return f"Round(round_={self.rounds!r})"

    def __str__(self):
        return str(self.rounds)

    def __eq__(self, other):
        if isinstance(other, Round):
            return self.rounds == other.round_
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(frozenset(self.rounds.items()))


if __name__ == "__main__":
    person = Person(id_=1)
    person2 = Person(id_=2)
    person3 = Person(id_=3)
    person4 = Person(id_=4)
    person5 = Person(id_=5)
    person6 = Person(id_=6)

    rounds = Rounds(rounds={
        1: Round(round_={
            "a":Group(items=[person,person2]),
            "b":Group(items=[person3])
        }),
        2: Round(round_={
            "a":Group(items=[person4,person5]),
            "b":Group(items=[person6])
        })
    })