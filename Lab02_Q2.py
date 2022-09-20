#Braulio Ojeda Valencia, Jashandeep Singh
#WORKLOAD: Jashan
#TITLE: Trapezoidal and Simpson's rules for integration

import numpy as np                         # import numpy
import matplotlib.pyplot as plt            # import matplotlib.pyplot
from time import time                      # from time module import time func.

""" Q2a waht is the exact vaule of intergal? 
"""

exact_vaule = 3.141592653589793

""" Q2b Set N=4, compare exact vaules,trapezoidal and simpons rule
"""

# define a function which returns 4/(1+x^2)
def f(x): 
    return 4/(1+x**2)
      
# define all varaibles like no. of sclices, lower and upper bound.
a = 0                # Lower bound
b = 1                # Upper bound
N = 22               # Number of slices
h = (b-a)/ N         # Distance between adjacent slices

# define Trapezoidal Rule
s_time_trapezoidal = time()         # save the start time
accumulator = 0.5*f(a) + 0.5*f(b)   # accumulate sum of each iteration
for i in range(1,N):
    accumulator  +=f(a+i*h)       
trapezoidal_result = accumulator * h 
e_time_trapezoidal = time()         # save the end time  
diff_trapezoidal =  e_time_trapezoidal -   s_time_trapezoidal 

# define Simpson's Rule
s_time_simpson = time()             # save the start time
even_terms = 0                      # initialize even sum  
odd_terms  = 0                      # initialize odd sum
for k in range(1,N):
    if k % 2 == 0:                  # condition for Even/Odd k
        even_terms += f(a + k*h)
    else:
        odd_terms += f(a + k*h)
        
simpson_result = h/3 * (f(a)+f(b) + 2*even_terms + 4*odd_terms)
e_time_simpson = time()             # save the end time 
diff_simpson = e_time_simpson  - s_time_simpson 

print('Exact Vaule = {}\n Trapezoidal Result = {}\n Simpson Result = {}\n'
       .format(exact_vaule,trapezoidal_result,simpson_result))
# print('After comperison, it can be seen that Trapezodial Rule\'s accuracey is' 
#       'up to 1st order whereas for simpsons\'s rule it is upto 3rd order')

""" Q2c: (1)For each method (Trapezoidal and Simpson), how many slices do you 
need to approximate the integral with an error of O(10^−9)?
(2) How long does it takes to compute the integral with an error of O(10^−9) 
for each method? """

# Converting Float into Strings and then slicing string, now we have 10 digits 
# after the decimal. WE want to approximate the integrals with an error of O(10^−9)
# means 9 digits after the decimal.
 
# str_ev = (str(exact_vaule))[0:12]  
# str_trampzoidal_result = (str(trapezoidal_result))[0:12]
# str_simpson_result = (str(simpson_result))[0:12] 
# print(str_ev ,str_simpson_result)#,str_trampzoidal_result)

print('Question 2c: ')
print('For Simpson\'s Rule, N = 22')
print('For Trapezoidal Rule,  N = 2^15\n')
if N == 2**15:
    print('Total time taken to compute the interal with an error of order 10^-9' 
         '(Trapezidal Rule) =', diff_trapezoidal,'seconds')
if N== 22:
    print('\nTotal time taken to compute the interal with an error of order 10^-9' 
          '(Simpson\'s Rule) =', diff_simpson,'seconds\n')

"""Question 2d: Adapt the “practical estimation of errors” of the textbook (§ 5.2.1, p. 153)
to the trapezoidal method only to obtain the error estimation for N2 = 32 
(using N1 = 16).
"""
print('Question 2d:\n'
      'Let I1 be the result of Trapeoidal rule when N1 = 16 and '
      'Let I2 be the result of the Trapeoidal rule when N2 = 32\n'
      'Practical estimation of errors (e) = 1/3 (I2-I1)')

N1 = 16              
N2 = 32
h1 = (b-a)/ N1
h2 = (b-a)/ N2         

# define Trapezoidal Rule
accumulator1 = 0.5*f(a) + 0.5*f(b)   # accumulate sum of each iteration
for i in range(1,N1):
    accumulator1  +=f(a+i*h1)       
trapezoidal_result_N1 = accumulator1 * h1 

accumulator2 = 0.5*f(a) + 0.5*f(b)   # accumulate sum of each iteration
for i in range(1,N2):
    accumulator2  +=f(a+i*h2)       
trapezoidal_result_N2 = accumulator1 * h2
print('Practical estimation of errors =',1/3*
      (trapezoidal_result_N2 -trapezoidal_result_N1)) 
 








