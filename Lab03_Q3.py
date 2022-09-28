#Braulio Ojeda Valencia, Jashandeep Singh
#WORKLOAD: Jashan
#TITLE: Calculating quantum mechanical observables: 
    
# Pseudocodes:
# Import necessary packages (like numpy)



import numpy as np                         # import numpy
import matplotlib.pyplot as plt            # import matplotlib.pyplot
from math import factorial
from gaussxw import gaussxw
# Define hermite polynomial function (H_n(x)), H_0(x) = 1 and H_1(x) = 2x

"""
# def H(n,x): 
#     "Returns Hermite Polynomial
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 2 * x
#     else:
#         return (2 * x * H(n-1,x) - 2 * (n-1) * H(n-2,x)) Delete this la
"""


def H(n,x): 
     """Returns Hermite Polynomial"""
     if n == 0:
         return 1 
     else:
         H =[1]
         for n in range(n):
             H.append(2 * x * H[n] - 2 * (n) * H[n-1])
         return H[-1]

# Define intergal function (eq.8)

def potential_well(n,x):
    """Return eq.8"""
    return 1 /(np.sqrt(2**n * factorial(n) * (np.sqrt(np.pi)))) * np.exp(-x**2 / 2) * H(n,x)
  
# Define range of x-axis, -4 < x < 4
x = np.linspace(-4, 4,100)      # x-axis (array of 100 values)
y = []                          # y-axis
n = 0
# Write algorithm, use while and for loop to get the wave function
while n < 4:
    lst = []    # empty list to save the output of for loop after single itration
    for i in x:
        ans = potential_well(n, i)
        lst.append(ans)
    y.append(lst)
    n += 1
    
# print('Wavefunction between -4 < x <4, when  n = 0\n',y[0],'\n')
# print('Wavefunction between -4 < x <4, when  n = 1\n',y[1],'\n')
# print('Wavefunction between -4 < x <4, when  n = 2\n',y[2],'\n')
# print('Wavefunction between -4 < x <4, when  n = 3\n',y[3],'\n')

# Plot wave function
plt.plot(x,y[0],label ='n = 0',c='black')
plt.plot(x,y[1],label ='n = 1',c='r')
plt.plot(x,y[2],label ='n = 2',c='orange')
plt.plot(x,y[3],label ='n = 3',c='g')
plt.title('Quantum Harmonic Oscillator')
plt.xlabel('x values')
plt.ylabel('Wave function ($\Psi_n$)')
plt.legend(loc='lower right')


######################### Question 3b ########################################
# n = 30 and -10 < x < 10

new_x = np.linspace(-10, 10,1000)       
new_n = 30
new_y = []
for j in new_x:
    new_ans = potential_well(new_n, j)
    new_y.append(new_ans)
plt.plot(new_x,new_y,label='n=30',c='blue')
plt.title('Quantum Harmonic Oscillator')
plt.xlabel('x values')
plt.ylabel('Wave function ($\Psi_n$)')
plt.legend(loc='lower right')

######################### Question 3c ########################################
# Define <|x|^2> function 
n = 5 
def uncertainty_x_sqr(z):
    """ A """
    return ((z*(1+z**2)) / ((1-z**2)**3)) * ((np.abs(potential_well(n,z/1-z**2)))**2)

def uncertainty_x(n,z):
    return (np.tan(z)**2 * np.abs(potential_well(n, np.tan(z)))) / np.cos(z)**2

# Set up Gaussian quad. algorithm
N = 100
a = -np.pi /2
b = np.pi /2 

# Calculate the sample number points(x_k) and weights (w_k), then map them
# to the required intergraion domian
x,w = gaussxw(N)
print(x,w)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

# Perform the intergration 
s =0.0
for k in range(len(x)):
    s += wp[k] * uncertainty_x(n,xp[k])  
print(np.sqrt(s))








    
            
            
        

        
  
    

        
                               

    



