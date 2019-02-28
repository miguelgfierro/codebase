# From https://realpython.com/instance-class-and-static-methods-demystified/


class Pizza:
    """Factory using classmethod decorator
    
    Examples:
        >>> pizza = Pizza.margherita()
        >>> type(pizza)
        <class 'python.data_structures.factory_classmethod.Pizza'>
        >>> print(pizza)
        Pizza(['mozzarella', 'tomatoes'])
        >>> pizza2 = Pizza.prosciutto()
        >>> print(pizza2)
        Pizza(['mozzarella', 'tomatoes', 'ham'])
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return "Pizza({})".format(self.ingredients)

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])
