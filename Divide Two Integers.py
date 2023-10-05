import sys
import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maxi = (2**31)-1
        mini = -2**31
        if (dividend>=0 and divisor>=0) or (dividend<0 and divisor<0):
            k = dividend // divisor
            if k>maxi:
                return maxi
            else:
                return k
        else:
            k = (dividend / divisor)
            if not isinstance(k, int):
                k = math.ceil(k)

            if k<mini:
                return mini
            else:
                return k