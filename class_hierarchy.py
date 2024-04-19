# Class Definitions

class Model:
    def __init__(self, name):
        # TODO: What is the difference between self.name and name?
        self.name = name

    def print_name(self):  # TODO: Snake case convention
        print(self.name)


class KNN(Model):  # TODO: Derived & base classes
    def __init__(self, name, k):  # TODO: Initializing base class
        super().__init__(name)
        self.k = k

    def print_k(self):
        print(f"k is {self.k}")

    def increment_k_and_print(self):
        self.k += 1
        print_k(self)  # TODO: Will this work?


# Driver Code

knn = KNN("KNN", 3)
knn.print_name()  # TODO: Will this work?

knn.increment_k_and_print()
