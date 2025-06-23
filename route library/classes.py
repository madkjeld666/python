# classes.py

class Lokaal:
    def __init__(self, naam, richting):
        self.naam = naam
        self.richting = richting

    def __str__(self):
        return f"Lokaal: {self.naam}, Richting: {self.richting}"

    def to_dict(self):
        return {
            "naam": self.naam,
            "richting": self.richting
        }
