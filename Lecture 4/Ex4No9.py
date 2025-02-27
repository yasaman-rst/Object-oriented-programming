class WeatherStation:
    def __init__(self, name:str):
        self.__name = name
        self.__observations = []

    def add_observation(self, observation:str):
        self.__observations.append(observation)

    def latest_observation(self):
        return self.__observations[-1] if self.__observations else "" #If the list self.__observations is not empty, return the last observation.

    def number_of_observations(self):
        return len(self.__observations)

    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

# Example:
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())  

station.add_observation("Thunderstorm")
print(station.latest_observation())  

print(station.number_of_observations())  
print(station) 