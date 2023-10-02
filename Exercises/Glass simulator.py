"""Empty/full glass simulator (*)

Create a class that represents a glass of water. 
It should have a method for filling the glass, 
    and another method for emptying the glass. 
Also, there needs to be an internal/private attribute that keeps track of if the glass is empty or full. :: state
Depending on the current state (empty/full), the method that fills the glass should print either "Filling the glass with water" 
    or "The glass is already full". 
The other method should print either "Emptying the glass" 
    or "The glass is already empty".

Additional exercise: 
Add another method to break the glass. 
Every glass (instance) keeps track of it's internal state, and prints what happens when the different methods are executed. 
Eg. "The glass breaks. Now there is water all over the floor", or "The glass can not be filled, since it's broken", etc."""

class Glass:
    @property
    def state (self):
        return self._state
    
    @state.setter
    def state (self, state):
        if type(state)!= bool:
            self._state = False
        else:
            self._state = state

my_glass = Glass()
my_glass.state = "abracadabra"

print (my_glass.state)

