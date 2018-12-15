# Complex Functions
This is a python program that uses the pygame module to animate complex functions. It displays four boxes (of distance 0, 1, 2, 3, and 4 from 0) and shows an animation detailing their movement from z to f(z).

## How to use
This program is mainly to be used from the command line. Here is an example usage to animate f(z) = z*i :

    C:\YourDirectoryHere\complex-functions\src> python animate.py "z*i"
    
Have a go experimenting with each of the operators available, and see what you can come up with! Here's another example to get you started that animates f(z) = z / (z.realpart*i + z.imaginarypart) :

    C:\YourDirectoryHere\complex-functions\src> python animate.py "z/(z.r*i+z.i)"

You may be suprised to see that all values are mapped onto the unit circle! The command below shows the use of a non-continuous function that multiplies z by it's imaginary part if it has a magnitude less than five - otherwise, it rotates it 45 degree clockwise.

    C:\YouDirectoryHere\complex-functions\src> python animate.py "z*(z.i) if z<5 else z*complex(0.707,0.707)"

Here is a list of some of the things you can do:
    
    complex(real, imaginary)        returns x*imaginary+real
    +                               adds two numbers
    -                               subtracts two numbers
    /                               divides two numbers
    *                               multiplies two numbers
    abs(z)                          returns the magnitude of the number
    int(z)                          returns the real part of the number as an integer
    float(z)                        returns the real part of the number as a float
    z.i                             returns the imaginary component of z
    z.r                             returns the real component of z
    z.get()                         returns a tuple containing (z.r, z.i)
    
    value if condition else value
    <                               compares the magnitudes
    >                               compares the magnitudes
    ==                              compares the whole value
    !=                              compares the whole value
    
    
