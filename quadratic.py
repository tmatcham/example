
## @package quadratic_solver
#This package contains a quadratic solver
import math

##A solver for quadratic equations in the form ax^2+bx+c=0
#Will return any roots of the equation in a list
#If complex roots are allowed, the returned values may be complex
#If complex roots are not allowed and there are no non-complex roots then a ValueError will be returned
#If both the quadratic and linear coefficients are zero then a ValueError will be returned
#@param a (numeric) The quadratic coefficient
#@param b (numeric) The linear coefficient
#@param c (numeric) The constant
#@param complex_allowed (optional) (bool) If True, complex roots will be returned (if appropriate). If False, a ValueError will be returned if the discriminant is negative
def quadratic_solver(a, b, c, complex_allowed=False):
    if a==0:
        if b==0:
            ##If the quadratic and linear coefficients are both zero, raise a ValueError
            raise ValueError("Both 'a' and 'b' were zero, meaning there was no defined value for 'x'")
        else:
            ##If the quadratic coefficient is zero, return the constant divided by the linear coefficient
            return([-c/b])

    ##@var discriminant (float) The discriminant of the equation
    discriminant=b**2-4*a*c

    if discriminant<0:
        if complex_allowed:
            ##If the discriminant is negative and complex roots are allowed, return two complex roots
           return([(-b-1j*math.sqrt(-discriminant))/(2*a), (b+1j*math.sqrt(-discriminant))/(2*a)])
        else:
            ##If the discriminant is negative and complex roots are not allowed, raise a ValueError
            raise ValueError("The discriminant was negative and complex results were not allowed")
    elif discriminant==0:
        ##If the discriminant is zero, return one real root
        return([-b/(2*a)])
    else:
        ##If the discriminant is positive, return two real roots
        return([(-b-math.sqrt(discriminant))/(2*a), (-b+math.sqrt(discriminant))/(2*a)])