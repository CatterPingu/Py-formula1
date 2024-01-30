import time
import inquirer
from tabulate import tabulate
from yaspin import yaspin

def fetch_data():
    # Simulating data fetching
    with yaspin(text="Fetching data...", color="yellow") as spinner:
        time.sleep(2)  # Simulating API request
        spinner.text = "Data fetched successfully!"
        time.sleep(1)

    # Simulated data
    headers = ["Driver", "Team", "Points"]
    data = [
        ["Lewis Hamilton", "Mercedes", 347],
        ["Max Verstappen", "Red Bull Racing", 289],
        ["Valtteri Bottas", "Mercedes", 221],
        ["Sergio Perez", "Red Bull Racing", 190],
        ["Carlos Sainz", "Ferrari", 164],
    ]
    return headers, data

def display_data(headers, data):
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)

def main():
    # Example of using Inquirer for input
    questions = [inquirer.List("action", message="Choose an action", choices=["Display Standings", "Quit"])]
    while True:
        answer = inquirer.prompt(questions)
        action = answer["action"]

        if action == "Display Standings":
            headers, data = fetch_data()
            display_data(headers, data)
        elif action == "Quit":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
