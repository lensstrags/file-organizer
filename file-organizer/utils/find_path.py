
import os
import calendar
from utils.config import Config
from utils.logger import Logging

class LoadData:
    """LoadData extracts and returns the directory path for a given file.
    
    The LoadData class takes a filename as a string (e.g., 'jax030525), extracts the year, month, city, and region,
    and returns the directory the file belongs to in the format /year/month/region/city.
     
     Attributes:
        error_logger (Logging): Object used to log errors in a file.
        config (config): Configuration object containing region-to-city mappings.
        year (int or str): Extracted year from the file name.
            Example:
                filename = jax030525
                year = 2025
        month (str): Full month name extracted from filename.
            Example:
                filename = jax030525
                month = March
        city (str): 3-letter city code extracted from filename.
            Example:
                filename = jax030525
                city = jax
        region (str): 'north' or 'south' depending on the city.
        """
    
    def __init__(self):
        """Initializes LoadData with default values and loads configuration."""
        self.error_logger = Logging()
        self.config = Config()
        self.year = None
        self.month = None
        self.city = None
        self.region = None

    def _set_attribute_instances(self, myfile):
        region_data = self.config.get_region_dict()             # Assigns region_data to a dict mapping each region (North - South) to a list containing it's corresponding IMCs.

        # Set region for the given file
        is_found = False
        for region, cities in region_data.items():
            for city in cities:
                if city in myfile:
                    self.city = city
                    self.region = region
                    is_found = True
                    break
            if is_found:
                myfile = myfile.replace(city, "")       # Remove city code from the string myfile. Now myfile = MMDDYY.csv
                break

        if not is_found:
            self.city = "Unknown"
            self.region = "Unknown"
            self.error_logger.log_error(f"No matching city found in filename: {myfile}")

        # Extract and set the month
        try:
            self.month = calendar.month_name[int(myfile[:2])]
            myfile = myfile.replace(myfile[:4], "") # Remove MM and DD from the string. Now myfile = YY.csv
        except (ValueError, IndexError):
            self.month = "Unknown"
            self.error_logger.log_error(f"Error extracting the month from {myfile}")

        # Extract and set the year
        try:
            self.year = int(myfile[:2]) + 2000
        except (ValueError, IndexError):
            self.year = "Unknown"
            self.error_logger.log_error(f"Error extracting the year from {myfile}")

    

    def get_dir_path(self, myfile):
        """Return the directory path for the given file.
        
        Args:
            myfile (str): filename in the format cityMMDDYY
            
        Returns:
            The directory path for the given file as a string.
        """

        self._set_attribute_instances(myfile)
        dir_path = os.path.join(str(self.year), self.month, self.region, self.city)
        return dir_path
    
    def display(self):
        print(f"City code: {self.city}")
        print(f"Year: {self.year}")
        print(f"Month: {self.month}")
        print(f"region: {self.region}")
        
    

def main():
    file_path = LoadData()

    dir_path = file_path.get_dir_path("tall061725.csv")
    file_path.display()
    print(f"Directory path: {dir_path}")


if __name__== "__main__":
    main()
        