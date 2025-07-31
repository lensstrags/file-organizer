import os
import sys
import calendar
from datetime import datetime

# FIXME: Parameterize the root path: You could allow passing the root path (e.g., via argparse) instead of hardcoding it.

def create_dir(current_dir, new_dir):
    """Creates new directory new_dir and returns the absolute path of the new directory."""
    try:
        if not os.path.exists(current_dir):
            raise FileNotFoundError(f"{current_dir} does not exist.")
        
        current_dir = os.path.join(current_dir, new_dir)
        os.makedirs(current_dir, exist_ok=True)
        print(f"Directory {current_dir} created.")
        return current_dir
    
    except FileNotFoundError as e:
        print(e)
        sys.exit()      # Terminates the program


def main():
    root = "C:\\Users\\noc-user.SYSTEM\\Desktop\\backupRadioReport"
    year_dir = datetime.now().year
    imc = {
        "north": ["jax", "tall"],
        "south": ["orl", "tmp", "ftm", "lkw", "mia"]
    }

    root = create_dir(root, str(year_dir))  # Creates new directory for the current year. Filesystem is now: root\current_year

    for i in range(1, 13):
        month_dir = create_dir(root, calendar.month_name[i])    # Creates directory for every month of the year. Ex: root\current_year\January or root\current_year\February.
        for key, values in imc.items():
            region_dir = create_dir(month_dir, key)             # Creates region directory. Ex: root\current_year\january\north or root\January\current_year\south
            for value in values:
                create_dir(region_dir, value)         # Creates a directory for every imc. Ex: root\current_year\January\north\jax.
    


if __name__ == "__main__":
    main()
