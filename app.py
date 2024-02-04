import warnings
import pandas as pd
from urllib3.exceptions import NotOpenSSLWarning
from fastf1.ergast import Ergast
from tabulate import tabulate
import inquirer
from yaspin import yaspin

# Suppress only the specific warning you're encountering
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)


def fetch_standings():
    # Initialize the Ergast object
    ergast = Ergast()

    # Get driver standings for the specified season (2023 in this case)
    standings_response = ergast.get_driver_standings(season=2023)

    # Extract and parse the content from the response
    standings_data = standings_response.content[0]  # Access the first element of the list

    # Extracting specific columns from the standings data
    selected_columns = ['position', 'points', 'wins', 'driverNumber', 'driverCode', 'constructorNames']
    selected_data = standings_data[selected_columns]

    # Create DataFrame with selected data
    selected_df = pd.DataFrame(selected_data)

    return selected_df


def display_data(data):
    table = tabulate(data, headers='keys', tablefmt="grid")
    print(table)


def main():
    questions = [inquirer.List("action", message="Choose an action", choices=["Display Upcoming Races",
                                                                              "Display Driver Standings",
                                                                              "Display Constructor Standings",
                                                                              "Race Results",
                                                                              "Driver Information",
                                                                              "Constructor Information",
                                                                              "Quit"])]

    while True:
        answer = inquirer.prompt(questions)
        action = answer["action"]

        if action == "Display Standings":
            with yaspin(text="Fetching standings data...", color="yellow") as spinner:
                standings_data = fetch_standings()
                spinner.ok("✔")
            display_data(standings_data)
        elif action == "Quit":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
