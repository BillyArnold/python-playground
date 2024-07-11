#!/opt/homebrew/bin/python3

class MathTester():
    def __init__(self, numpy):
        self.numpy = numpy
        self.one_dimensional_array = self.numpy.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
        self.random_integers_between_50_and_100 = self.numpy.random.randint(low=50, high=101, size=(6,))
        self.sequence_of_integers = self.numpy.arange(5, 12)

    def print_values(self):
        print('Testing')
        print(self.random_integers_between_50_and_100)
