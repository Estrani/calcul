class Calcul:

    def __init__(self, number_one, number_two):
        self.set_number_one()
        self.set_number_two()

    def set_number_one(self, number_one):
        self.__number_one = number_one

    def set_number_two(self, number_two):
        self.__number_two = number_two

    def get_number_one(self):
        return self.__number_one
    
    def get_number_two(self):
        return self.__number_two
    

    def Addition(n1, n2):
        return n1 + n2
    
    def Soustraction(n1, n2):
        return n1 - n2
    
    def Multiplication(n1, n2):
        return n1 * n2
    
    def Division(n1, n2):
        return n1 / n2