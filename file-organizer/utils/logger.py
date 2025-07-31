# Error logging

class Logging:
    def __init__(self):
        self.log_file = "C:\\Users\\noc-user.SYSTEM\\Desktop\\backupRadioReport\\error_log.txt"

    def log_error(self, error_to_log):
        with open(self.log_file, "a") as myfile:
            myfile.write(f"{error_to_log}\n")

def main():
    error_logger = Logging()
    error_logger.log_error("this is a test...")

if __name__=="__main__":
    main()
