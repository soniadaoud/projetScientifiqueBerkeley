import numpy as np
import matplotlib.pyplot as plt

#Abscisse
x = np.linspace(-10,10,200000)

#Lipid mass - Green
x_lip = 2.3
y_lip = -1
a_lip = 0.2
b_lip = 0.4
alpha_lip = 0 #angle in rad

#Calcium mass - Yellow
x_cal = 2
y_cal = 1.2
a_cal = 0.2
b_cal = 0.5
alpha_cal = 0 #angle in rad


#general - ellipse centered on x0,y0 with main axis a and small axis b, angle of rotation alpha
def general_ellipse(x0,y0,a,b,alpha):
    #x = np.linspace ( x0 - (a*np.cos(alpha))/2 , x0 + (a*np.cos(alpha))/2  , 2000 )
    A = (b**2)*(np.sin(alpha)**2)+(a**2)*(np.cos(alpha)**2)
    B = 2*(x-x0)*np.cos(alpha)*np.sin(alpha)*((b**2)+(a**2))
    C = ((x-x0)**2)*((b**2)*(np.cos(alpha)**2)+(a**2)*(np.sin(alpha)**2))-(a**2)*(b**2)
    y = (y0 + (-B+np.sqrt(B**2-4*A*C))/(2*A))
    z = (y0 + (-B-np.sqrt(B**2-4*A*C))/(2*A))
    return y,z,x



x,y,z = general_ellipse(x_lip,y_lip,a_lip,b_lip,alpha_lip)
x1,y1,z1 = general_ellipse(x_cal,y_cal,a_cal,b_cal,alpha_cal)
print(x,y,z)
plt.plot(x,y,'r-')

# plt.plot(x1,y1,'b-')
# plt.plot(x1,y1,'b-')

plt.show()



# Parameters Verification - avoid intersections
#
# def check(y_1,y_2):
#     intersect = np.argwhere(np.diff(np.sign(y_1 - y_2)) != 0).reshape(-1) + 0
#     if (intersect!=[]):
#         x_intersect = []
#         y_intersect = []
#         for idx in intersect:
#             if np.isnan(y_1[idx])==False & np.isnan(y_2[idx])==False:
#                 x_intersect.append(x[idx])
#                 y_intersect.append(y_2[idx])
#         if len(x_intersect)%2!=0:
#             x_intersect=x_intersect[:-1]
#             y_intersect=y_intersect[:-1]
#         if y_intersect != []:
#             plt.plot(x_intersect, y_intersect, 'bo')
#             return True


# def domain(y):
#     domain = []
#     for i in x:
#         if  (np.isnan(y[i])==False):
#             domain.append(i)
#     return domain
#
# def intersectDomain(y,z):
#     intersectDomain = []
#     domain1=domain(y)
#     domain2=domain(z)
#     for i in len(domain1):
#         for j in len(domain2):
#             if (domain1[i] == domain2[j]):
#                 intersectDomain.append(domain1[i])
#     return intersectDomain
#
# y,z = general_ellipse(2.3,-1,0.2,0.4,np.pi/3)
#
# print('domaine de definition de y' , domain(y))
# y1,z1 = general_ellipse(2,1.2,0.2,0.5,np.pi/4)
#
# print('domaine de definition de y1' , domain(y1))
#
# print('intersection des deux domaines de defintion' , intersectDomain(y,y1))
