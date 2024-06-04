class Pizza:
    """
    Represents a pizza that has an owner, toppings, and dressing.

    Argument:
    name (string): the pizza owner's name
    toppings (list): the toppings on the pizza
    dressing (string): the dressing on the pizza

    Attribute:
    price_of_topping (float): the cost of a topping
    price_of_dressing (int): the cost of dressing
    price_of_pizza (int): the cost of a regular pizza
    """
    price_of_topping = .5
    price_of_dressing = 1
    price_of_pizza = 10
    customer_count = 0

    def __init__(self, name, toppings, dressing=None):
        """
        Creates a pizza object

        :param name: name of pizza owner
        :param toppings: list containing all toppings
        :param dressing: string of dressing if wanted
        """
        self.add_customer()
        self.toppings = toppings
        self.name = name
        self.dressing = dressing

    @classmethod
    def add_customer(cls):
        """
        Update the prices of the pizza attributes
        """
        cls.customer_count += 1

    def add_dressing(self, sauce):
        """
        Add or edit a dressing of a pizza

        :param sauce: the dressing to add
        """
        self.dressing = sauce

    def add_topping(self, topping):
        """
        Add toppings to a pizza

        :param topping: the toppings to add
        """
        self.toppings.extend(topping)

    def change_name(self, new_name):
        """

        :param new_name: the name to change ownership to
        """
        self.name = new_name

    def __str__(self):
        """
        Prints out description of the pizza

        :return: string description of pizza
        """
        string = f'{self.name}\'s pizza costs ${self.check_price()} ' \
            f'and has: '
        if self.toppings:
            for topping in sorted(self.toppings):
                string += topping + ", "
        else:
            string += "no toppings "

        if self.dressing is not None:
            string += "and " + self.dressing + " dressing"
        else:
            string += "and no dressing"
        return string

    def __eq__(self, other):
        """
        Checks equality of pizzas, with toppings and dressing
        Name is not important

        :param other:
        :return: boolean showing if their equal
        """
        for topping in self.toppings:
            if topping not in other.toppings:
                return False
        if self.dressing != other.dressing:
            return False
        return True

    def __lt__(self, other):
        """
        Compares pizza less than by comparing their number of toppings

        :param other: other pizza to compare to
        :return: True if self is less than other
        """
        if len(self.toppings) < len(other.toppings):
            return True
        else:
            return False

    def __add__(self, other):
        """
        Adds two pizzas together

        :param other: other pizza to add
        :return: new pizza of both pizzas combined, only one dressing chosen
        """
        name = self.name + " & " + other.name
        if self.dressing is None and other.dressing is None:
            dressing = None
        elif self.dressing is None and other.dressing is not None:
            dressing = other.dressing
        elif self.dressing is not None and other.dressing is None:
            dressing = self.dressing
        else:
            dressing = self.dressing + "/" + other.dressing
        toppings = self.toppings + other.toppings
        pizza = Pizza(name, toppings, dressing)
        return pizza

    def __len__(self):
        """
        Returns length of pizza, or the number of toppings

        :return: number of toppings
        """
        return len(self.toppings)

    def __getitem__(self, key):
        """
        Gets a topping in the list

        :param key: index
        :return: returns topping in key index
        """
        if 0 < key < self.toppings:
            return self.toppings[key - 1]

    def check_price(self):
        """
        Gets the price of the pizza

        :return: price of pizza calculated with number of toppings
        and dressing
        """
        price = len(self.toppings) * self.price_of_topping\
            + self.price_of_pizza
        if self.dressing is not None:
            price += self.price_of_dressing
        return f'{price:.2f}'


def main():
    anchovy_pizza = Pizza("Alex", ["olives", "anchovies", "onions"],
                          "ranch")
    print(anchovy_pizza)
    print("Customer count: " + str(anchovy_pizza.customer_count))

    weird_pizza = Pizza("Vincent", ["shrimp", "cucumber",
                                    "peppers"])
    print(weird_pizza)
    print("Customer count: " + str(weird_pizza.customer_count))

    normal_pizza = Pizza("Amanda", [])
    print(normal_pizza)
    print("Customer count: " + str(normal_pizza.customer_count))
    print("Class customer count: " + str(Pizza.customer_count))

    idk_pizza = Pizza("Leslie", [], "BBQ Sauce")

    print()
    print(idk_pizza)
    print("Adding toppings and changing dressing...")
    idk_pizza.add_dressing("Peanut Butter")
    idk_pizza.add_topping(["Olives", "Chili Peppers"])
    print(idk_pizza)
    print("Changing owner...")
    idk_pizza.change_name("Rula")
    print(idk_pizza)

    # Note: names do not count for equality
    print()
    print("Equality operator testing...")

    same_pizza1 = Pizza("Steve", ["Cheese", "Chicken"], "tomato")
    same_pizza2 = Pizza("Eric", ["Cheese", "Chicken"], "tomato")
    different_pizza1 = Pizza("Mark", ["Cheese", "Steak", "Chicken"]
                             , "tomato")

    print(same_pizza1 == same_pizza2)
    print(same_pizza1 == different_pizza1)

    print()
    print("Overload of less than operator")
    print(same_pizza1 > different_pizza1)
    print(different_pizza1 > same_pizza1)

    print()
    print("Overload of +")
    together = anchovy_pizza + weird_pizza
    other_together = idk_pizza + normal_pizza
    print(together)
    print(other_together)

    print()
    print("getitem and len testing...")
    print(anchovy_pizza.toppings[2])
    print(len(anchovy_pizza))


if __name__ == "__main__":
    main()