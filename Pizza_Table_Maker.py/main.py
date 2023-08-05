
#In a file called pizza.py, implement a program that expects exactly one command-line argument,
#the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate,
#a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format.
#If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv,
# or if the specified file does not exist, the program should instead exit via sys.exit.
#completed and submitted

from tabulate import tabulate
import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        sys.exit("Invalid command line argument.")

    filename = sys.argv[1]
    items = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                items.append(line.rstrip().split(","))
        headers = items[0]
        table = items[1:]
        print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist.")

if __name__ == '__main__':
    main()
