class Config:
    def __init__(self):
        self.region = {
            "north": ["jax", "tall"],
            "south": ["orl", "tmp", "ftm", "lkw", "mia"]
        }
    
    def get_region_dict(self):
        return self.region
    
    def get_region_data(self):
        return self.region.values()

    def display(self):
        print(f"Region dict: {self.get_region_dict()}")
        print(f"Region values: {self.get_region_data()}")
    
def main():
    region = Config()
    region.display()

if __name__=="__main__":
    main()