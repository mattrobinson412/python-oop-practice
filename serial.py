"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "Initiates a serial number generator at the 'start' value."
        self.start = self.next = start
    
    def generate(self):
        "Generates a new serial number in increments of 1, starting from the 'start' value."
        self.next += 1
        print(self.next - 1)

    def reset(self):
        "Resets the serial numbers to the intial 'start' value."
        self.next = self.start
        print(self.next)
    
    def __repr__(self):
        "Provides representation for the Serial Generator."
        print(f"<SerialGenerator start = {self.start} next = {self.next}>")
        

serial = SerialGenerator(start=100)
serial.generate()
serial.generate()
serial.generate()
serial.reset()
serial.generate()
serial.generate()
serial.__repr__()

        

