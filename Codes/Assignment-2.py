import numpy as np
from scipy.integrate import quad
#defining two functions with exp(-2|x|) and exp(-3|x|) as their variable parts and then integrating them
#function_A
def integrand(x):
    return(np.exp(-2*abs(x)))
integral_fa=quad(integrand,-np.inf,np.inf)
print(integral_fa)

#function_B
def integrand(x):
    return(np.exp(-3*abs(x)))
integral_fb=quad(integrand,-np.inf,np.inf)
print(integral_fb)

#As we can see that integrals of function A and B are (1) and (2/3) respectively
#The Constant part of functions were M and N.

#The PDF(probability distribution function) integrates to 1 which is 
#sum of function A and B along with their constants

# So M(integration of fa) + N(integration of fb)=1
#So M(1)+N(2/3)=1 which gives relation M + (2N/3)=1
