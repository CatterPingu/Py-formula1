import pandas as pd
from fastf1.ergast import Ergast


class FastF1Mngr:
    ergast = None

    def __init__(self):
        if FastF1Mngr.ergast is None:
            FastF1Mngr.ergast = Ergast()

    def fetch_driver_standings(self, year):

        # Get driver standings for the specified season
        standings_response = self.ergast.get_driver_standings(season=year)

        # Extract and parse the content from the response
        try:
            standings_data = standings_response.content[0]  # Access the first element of the list
        except:
            raise IndexError

        # Extracting specific columns from the standings data
        selected_columns = ['position', 'points', 'wins', 'driverNumber', 'driverCode', 'constructorNames']
        selected_data = standings_data[selected_columns]

        # Create DataFrame with selected data
        selected_df = pd.DataFrame(selected_data)

        return selected_df