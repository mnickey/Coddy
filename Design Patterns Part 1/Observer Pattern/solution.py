class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
        
    def detach(self, observer):
        self._observers.remove(observer)
        
    def notify(self, data):
        for observer in self._observers:
            observer.update(data)
            
class Observer:
    def update(self, data):
        pass

# Write your WeatherStation class here
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify(self._temperature)
    
    def get_temperature(self):
        return self._temperature


# Write your WeatherDisplay class here
class WeatherDisplay(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"Display {self.name}: Current temperature is {temperature}C")
