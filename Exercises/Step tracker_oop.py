"""Create a class that can be used as a step tracker. It should have a property "steps" that is read only; 
a method step() that increases "steps" by 1 each time it is called; and a method reset() that resets the counter.
Instantiate the class, and write a loop that simulates walking 1000 steps. Then print the value of "steps"."""

class Tracker:
    
    @property
    def steps(self):
        return self._steps

    def step(self):
        self._steps += 1
    
    def reset (self):
        self._steps = 0

day1 = Tracker()

day1.reset()

for steps in range (1001):
    day1.step()

print (day1.steps)


    

