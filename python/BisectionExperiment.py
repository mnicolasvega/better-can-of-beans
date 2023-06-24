from Bisection import Bisection
import numpy

bisection = Bisection()
linear = lambda x: numpy.sin(x)
result = bisection.perform(linear, 1, 5)
print(f"f(%.16f) ~= %.16f" % (result, linear(result)))
