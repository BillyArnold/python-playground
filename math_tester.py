#!/opt/homebrew/bin/python3

class MathTester():
    def __init__(self, numpy, pd):
        self.numpy = numpy
        self.pd = pd
        self.one_dimensional_array = self.numpy.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
        self.random_integers_between_50_and_100 = self.numpy.random.randint(low=50, high=101, size=(6,))
        self.sequence_of_integers = self.numpy.arange(5, 12)

    def print_values(self):
        print('Testing')
        print(self.random_integers_between_50_and_100)
        print(self.sequence_of_integers)

    def create_dataframe(self):
                # Create and populate a 5x2 NumPy array.
        my_data = self.numpy.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])

        # Create a Python list that holds the names of the two columns.
        my_column_names = ['temperature', 'activity']

        # Create a DataFrame.
        my_dataframe = self.pd.DataFrame(data=my_data, columns=my_column_names)

        #adjustments
        my_dataframe["adjusted"] = my_dataframe["activity"] + 2

        # Print the entire DataFrame
        print(my_dataframe)
