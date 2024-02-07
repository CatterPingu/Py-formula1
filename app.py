import inquirer
import typer
from yaspin import yaspin

from FastF1Mngr import FastF1Mngr
from utils import is_valid_year, display_data

app = typer.Typer()


@app.command()
def main():
    questions = [inquirer.List("action", message="Choose an action", choices=["Display Driver Standings",
                                                                              "Display Constructor Standings",
                                                                              "Race Results",
                                                                              "Driver Information",
                                                                              "Constructor Information",
                                                                              "Quit"])]

    fastf1 = FastF1Mngr()
    while True:
        answer = inquirer.prompt(questions)
        action = answer["action"]

        if action == "Display Driver Standings":
            while True:
                year = typer.prompt("Enter the year")
                if is_valid_year(year):
                    break
                else:
                    typer.echo("Invalid year. Please enter a valid year between 1950 and 2100.")
            try:
                with yaspin(text="Fetching standings data...", color="yellow") as spinner:
                    standings_data = fastf1.fetch_driver_standings(year)
                    spinner.ok("✔")
                display_data(standings_data)
            except IndexError:
                typer.echo(f"\nNo data for {year} exists\n",color=True)
        elif action == "Quit":
            print("Exiting...")
            break


if __name__ == "__main__":
    app()
