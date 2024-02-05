from tabulate import tabulate

def is_valid_year(year):
    try:
        year = int(year)
        if year < 1950 or year > 2100:
            raise ValueError("Year must be between 1950 and 2100")
        return True
    except ValueError:
        return False

def display_data(data):
    table = tabulate(data, headers='keys', tablefmt="grid")
    print(table)