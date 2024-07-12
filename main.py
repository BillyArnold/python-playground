from math_tester import MathTester
import numpy as np
import pandas as pd

def main():
    test = MathTester(np, pd)
    test.print_values()
    test.create_dataframe()

if __name__ == "__main__":
    main()