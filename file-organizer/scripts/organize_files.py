# Driver program
import os
import shutil
from utils.find_path import LoadData
from utils.logger import Logging

def main():
    error_logger = Logging()
    file_info = LoadData()
    root_dir = "C:\\Users\\noc-user.SYSTEM\\Desktop"
    archives_dir = "data_archives"

    source_root_dir = os.path.join(root_dir, archives_dir)   # source_dir = 'C:\Users\noc-user.SYSTEM\Desktop\data_archives
    destination_root_dir = os.path.join(root_dir, "backupRadioReport")  # destination_root_dir = 'C:\Users\noc-user.SYSTEM\Desktop\backupRadioReport'

    for root, dir, files in os.walk(source_root_dir):
        for file in files:
            file_path = file_info.get_dir_path(file)
            destination_dir = os.path.join(destination_root_dir, file_path)
            source_dir = os.path.join(source_root_dir, file)
            try:
                if not os.path.exists(destination_dir):
                    raise FileNotFoundError(f"Directory {destination_dir} does not exist.")
                shutil.copy(source_dir, destination_dir)
            except FileNotFoundError as e:
                error_logger.log_error(e)
    

if __name__=="__main__":
    main()