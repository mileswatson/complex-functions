# Complex Functions
This is a python program that uses the pygame module to animate complex functions. It displays four boxes (of distance 0, 1, 2, 3, and 4 from 0) and shows an animation detailing their movement from z to f(z).

## How to use
This program is mainly to be used from the command line. Here is an example usage to animate f(z) = z*i :

    C:\YourDirectoryHere\complex-functions\src> python animate.py "z*i"
    
Have a go experimenting with each of the operators available, and see what you can come up with! Here's another example to get you started that animates f(z) = z / (z.realpart*i + z.imaginarypart) :

    C:\YourDirectoryHere\complex-functions\src> python animate.py "z/(z.r*i+z.i)"

You may be suprised to see that all values are mapped onto the unit circle!

    
