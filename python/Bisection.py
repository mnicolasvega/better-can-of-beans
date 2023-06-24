from typing import Callable
import numpy

class Bisection:
    def __init__(self, iterations: int = -1, exp: int = 10):
        self.iterations = iterations
        self.epsilon = 10 ** -exp

    def perform(self, func: Callable[[float], float], start: float, end: float):
        if end <= start:
            raise Exception("end <= start")
        if numpy.sign(func(start)) == numpy.sign(func(end)):
            raise Exception("f(start) and f(end) have same sign")
        i = 0
        while (self.iterations < 0 or i < self.iterations):
            mid = (end + start) / 2
            vstart = func(start)
            vmid = func(mid)
            if abs(vmid) <= self.epsilon:
                break 
            if numpy.sign(vstart) == numpy.sign(vmid):
                start = mid
            else:
                end = mid
            i = i + 1
        return mid
