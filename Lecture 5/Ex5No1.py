class City:
    
    postcodes = {
        "Helsinki": "00100",
        "Turku": "20100",
        "Tampere": "33100",
        "Salo": "24100",
        "Oulu": "90100",
        "Jyväskylä": "40100"
    }

    def __init__(self, name: str, population: int):
        self.name = name
        self.__population = population
