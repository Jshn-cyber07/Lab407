#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:48:53 2022

@author: jashansingh
"""
import numpy as np                         # import numpy
import matplotlib.pyplot as plt            # import matplotlib.pyplot
# Define all required constants 
solar_mass = 1            # solar mass (M_s)  2.0 *10**30 kg
big_G = 39.5              # universal graitational constant in AU^3M_s^-1yr^-2.
# Note that 1 AU = 1.496 * 10^11 m  
mass_jupiter = 0.001                       # in MS
orbit_r_jupiter = 5.2                      # in AU 

mass_earth = 3*10**(-6)                    # in Ms

# Define Initial conditions 
initial_xe, initial_ye = 1,0      # Initial Corridates of Earth units are AU
initial_vxe, initial_vye = 0,6.18 # Initial velocity of Earth Units are AU/yr

initial_xj, initial_yj = 5.2,0    # Initial Corridates of Jupiter units are AU
initial_vxj, initial_vyj = 0,2.63 # Initial velocity of Jupiter, units are AU/yr





# Initialize time array
time = np.linspace(0.0001, 10, 100000) 


# define time step 
t0 = 0                # time staring at 0
dt = 0.0001 # vaule of time increment = 0.0001

# Initialize final vaules of position and velocity of Earth and Jupiter array 
# with same number of elements as time_vaule array

final_xe = np.zeros(np.shape(time)) # final values of earth's position in x-dir
final_ye = np.zeros(np.shape(time)) # final values of earth's position in y-dir

final_vxe = np.zeros(np.shape(time))# final values of earth's velocity in x-dir
final_vye = np.zeros(np.shape(time))# final values of earth's velocity in y-dir

final_xj = np.zeros(np.shape(time)) # final values of jupiter's position in x-dir
final_yj = np.zeros(np.shape(time)) # final values of jupiter's position in y-dir

final_vxj = np.zeros(np.shape(time))# final values of jupiter's velocity in x-dir  
final_vyj = np.zeros(np.shape(time))# final values of jupiter's velocity in x-dir



# Define euler_cromer method function and use FOR loop for 100,000 itrations

"""###################### Question 2 a ####################################"""
################## PLEASE UNCOMMENT THIS SECTION TO SEE Q2a'S RESULT ##########

# def euler_cromer(t,xe,ye,vxe,vye,xj,yj,vxj,vyj,xs=0,ys=0):
#     """Returns final_xe, final_ye,final_vxe and final_vye  after modyfing according to Euler-Cromer 
#     method."""
    
    
#     for i in range(len(time)): 
        
#         rej = np.sqrt((xe-xj)**2+(ye-yj)**2) # Distance betweeen Earth and Jupiter
#         res = np.sqrt((xe-xs)**2+(ye-ys)**2) # Distance between Earth and Sun
#         rsj = np.sqrt((xs-xj)**2+(ys-yj)**2)  # Distance between Sun and Jupiter
        
#         final_vxe[i]= vxe
#         vxe = vxe - (big_G*solar_mass*xe*dt)/res**3 - (big_G*mass_jupiter*(xe-xj)*dt)/rej**3
#         final_xe[i] = xe
#         xe = xe + vxe*dt
        
#         final_vye[i]= vye
#         vye = vye -(big_G*solar_mass*ye*dt)/res**3 - (big_G*mass_jupiter*(ye-yj)*dt)/rej**3
#         final_ye[i] = ye
#         ye = ye +vye*dt
        
#         final_vxj[i]= vxj
        
#         vxj = vxj -(big_G*solar_mass*xj*dt)/rsj**3 - (big_G*mass_earth*(xj-xe)*dt)/rej**3
#         final_xj[i]=xj
#         xj = xj + vxj*dt
        
#         final_vyj[i]=vyj
#         vyj = vyj -(big_G*solar_mass*yj*dt)/rej**3 - (big_G*mass_earth*(yj-ye)*dt)/rej**3
#         final_yj[i]=yj
#         yj = yj + vyj*dt
  
# euler_cromer(t0,initial_xe,initial_ye,initial_vxe,initial_vye,initial_xj,initial_yj,
#               initial_vxj,initial_vyj)

# # A plot showing Earth's and Jupiter's Orbit
# plt.plot(final_xe,final_ye, label='Earth', c='blue',ls=':')
# plt.plot(final_xj,final_yj,label='Jupiter', c='r',ls="-")
# plt.title('Orbits of Earth and Jupiter around the Sun')
# plt.xlabel('x (AU)')
# plt.ylabel('y (AU)')
# plt.legend(loc='lower right')


# def gravitational_force(G,Ma,Mb,d):
#     """ Returns the vaule of gravitaion force according to Newton's law of 
#     universal gravitation.
#     """
#     return (G*Ma*Mb) / d**2
# fg_earth_sun = gravitational_force(6.67*10**-11, 2*10**30, 5.9*10**24, 1.496 * 10**11)
# fg_earth_jupiter = gravitational_force(6.67*10**-11, 1.9*10**27, 5.9*10**24,
#                                         4.2*1.496 *10**11)
# print("Net Gravitation Force on Earth",(fg_earth_sun - fg_earth_jupiter),'N') 



"""Question 2B, If, mass of Jupiter is 1000 times it's original vaule Time peried 
is 3 years """
################# PLEASE UNCOMMENT THIS SECTION TO SEE Q2B'S RESULT ##########

# time2 = np.linspace(0.0001, 3, 30000) 
# final_xe = np.zeros(np.shape(time2)) # final values of earth's position in x-dir
# final_ye = np.zeros(np.shape(time2)) # final values of earth's position in y-dir

# final_vxe = np.zeros(np.shape(time2))# final values of earth's velocity in x-dir
# final_vye = np.zeros(np.shape(time2))# final values of earth's velocity in y-dir

# final_xj = np.zeros(np.shape(time2)) # final values of jupiter's position in x-dir
# final_yj = np.zeros(np.shape(time2)) # final values of jupiter's position in y-dir

# final_vxj = np.zeros(np.shape(time2))# final values of jupiter's velocity in x-dir  
# final_vyj = np.zeros(np.shape(time2))# final values of jupiter's velocity in x-dir

# def euler_cromer(t,xe,ye,vxe,vye,xj,yj,vxj,vyj,xs=0,ys=0):
#     """Returns final_xe, final_ye,final_vxe and final_vye  after modyfing according to Euler-Cromer 
#     method."""
    
    
#     for i in range(len(time2)): 
        
#         rej = np.sqrt((xe-xj)**2+(ye-yj)**2) # Distance betweeen Earth and Jupiter
#         res = np.sqrt((xe-xs)**2+(ye-ys)**2) # Distance between Earth and Sun
#         rsj = np.sqrt((xs-xj)**2+(ys-yj)**2) # Distance betweeb Sun and Jupiter
        
#         final_vxe[i]= vxe
#         vxe = vxe - (big_G*solar_mass*xe*dt)/res**3 - (big_G*mass_jupiter*1000*(xe-xj)*dt)/rej**3
#         final_xe[i] = xe
#         xe = xe + vxe*dt
        
#         final_vye[i]= vye
#         vye = vye -(big_G*solar_mass*ye*dt)/res**3 - (big_G*mass_jupiter*1000*(ye-yj)*dt)/rej**3
#         final_ye[i] = ye
#         ye = ye +vye*dt
        
#         final_vxj[i]= vxj
#         vxj = vxj -(big_G*solar_mass*xj*dt)/rsj**3 - (big_G*mass_earth*(xj-xe)*dt)/rej**3
#         final_xj[i]=xj
#         xj = xj + vxj*dt
        
#         final_vyj[i]=vyj
#         vyj = vyj -(big_G*solar_mass*yj*dt)/rej**3 - (big_G*mass_earth*(yj-ye)*dt)/rej**3
#         final_yj[i]=yj
#         yj = yj + vyj*dt
   
    
    
# euler_cromer(t0,initial_xe,initial_ye,initial_vxe,initial_vye,initial_xj,initial_yj,
#               initial_vxj,initial_vyj)

# # A plot showing Earth's Orbit
# plt.plot(final_xe,final_ye, label='Earth', c='blue',ls=':')
# plt.title('Earth\' orbit when mass of Jupiter is equal to mass of Sun')
# plt.xlabel('x (AU)')
# plt.ylabel('y (AU)')

""" Question 2C, replace earth with asteroid at an orbital disance of 3.3 AU, 
inital conditions are xa =3.3AU, ya =0.0AU, vax = 0 AU/yr, vay = 3.46 AU/yr"""
################# PLEASE UNCOMMENT THIS SECTION TO SEE Q2C'S RESULT ##########

initial_xa, initial_ya = 3.3, 0
initial_vxa, initial_vya=0,3.46

time3 = np.linspace(0.0001, 20, 200000) 
final_xa = np.zeros(np.shape(time3)) # final values of asteroid's position in x-dir
final_ya = np.zeros(np.shape(time3)) # final values of earth's position in y-dir

final_vxa = np.zeros(np.shape(time3))# final values of asteroid's velocity in x-dir
final_vya = np.zeros(np.shape(time3))# final values of asteroid'svelocity in y-dir

final_xj = np.zeros(np.shape(time3)) # final values of jupiter's position in x-dir
final_yj = np.zeros(np.shape(time3)) # final values of jupiter's position in y-dir

final_vxj = np.zeros(np.shape(time3))# final values of jupiter's velocity in x-dir  
final_vyj = np.zeros(np.shape(time3))# final values of jupiter's velocity in x-dir

def euler_cromer(t,xa,ya,vxa,vya,xj,yj,vxj,vyj,xs=0,ys=0):
    """Returns final_xe, final_ye,final_vxe and final_vye  after modyfing according to Euler-Cromer 
    method."""
    
    
    for i in range(len(time3)): 
        
        raj = np.sqrt((xa-xj)**2+(ya-yj)**2) # Distance betweeen Earth and Jupiter
        ras = np.sqrt((xa-xs)**2+(ya-ys)**2) # Distance between Earth and Sun
        rsj = np.sqrt((xs-xj)**2+(ys-yj)**2) # Distance betweeb Sun and Jupiter
        
        final_vxa[i]= vxa
        vxa = vxa - (big_G*solar_mass*xa*dt)/ras**3 - (big_G*mass_jupiter*(xa-xj)*dt)/raj**3
        final_xa[i] = xa
        xa = xa + vxa*dt
        
        final_vya[i]= vya
        vya = vya -(big_G*solar_mass*ya*dt)/ras**3 - (big_G*mass_jupiter*(ya-yj)*dt)/raj**3
        final_ya[i] = ya
        ya = ya +vya*dt
        
        final_vxj[i]= vxj
        vxj = vxj -(big_G*solar_mass*xj*dt)/rsj**3 - (big_G*mass_earth*(xj-xa)*dt)/raj**3
        final_xj[i]=xj
        xj = xj + vxj*dt
        
        final_vyj[i]=vyj
        vyj = vyj -(big_G*solar_mass*yj*dt)/raj**3 - (big_G*mass_earth*(yj-ya)*dt)/raj**3
        final_yj[i]=yj
        yj = yj + vyj*dt
   
euler_cromer(t0,initial_xa,initial_ya,initial_vxa,initial_vya,initial_xj,initial_yj,
              initial_vxj,initial_vyj)

# A plot showing Earth's Orbit
plt.plot(final_xa,final_ya, label='Asteroid', c='g',ls=':')
plt.title('Earth\' orbit when mass of Jupiter is equal to mass of Sun')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')


 


    


        













