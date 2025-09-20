def solution(a, b, c):
    once = a + b + c
    double = a ** 2 + b ** 2 + c ** 2
    triple = a ** 3 + b ** 3 + c ** 3
    
    if a == b == c:
        return once * double * triple
    elif a != b and a !=c and b != c:
        return once
    else:
        return once * double