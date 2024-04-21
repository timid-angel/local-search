class BagItem:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
    
    def __str__(self):
        return f"Name: {self.name}, Weight: {self.weight}, Value: {self.value}"