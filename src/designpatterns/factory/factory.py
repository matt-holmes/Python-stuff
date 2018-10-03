#factory.py

import abc

class Footwear(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def action(self):
        pass

class FlipFlops(Footwear):
    def action(self):
        return "walking"

class Sneakers(Footwear):
    def action(self):
        return "running"

class Boots(Footwear):
    def action(self):
        return "hiking"

class Factory:
    def getFootwear(self, mood):
        if mood == "lazy":
            return FlipFlops()
        elif mood == "energenic":
            return Sneakers()
        elif mood == "motivated":
            return Boots()
        else:
            return None
