"""PLOT CARTESIAN ELLIPSE BY DIRECT PLOT"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Parameters

#Artery wall - Blue
a_wall_in=5
b_wall_in= 3
thick_wall = 1.1

#Lumen - Red
x_L= -1
R_L = 2.2

#Calcium/Lipid mass - Green
x_M = 3
a_M = 0.4
b_M = 1.2
#Graphs

#Abscisse
x = np.linspace(-10,10,200000)

#Artery wall - inside layer - ellipse centered on 0 with main axis a_wall_in and small axis b_wall_in
def artery_wall(a_wall_in, b_wall_in,thick_wall):
    y_wall_in = +(b_wall_in/a_wall_in)*np.sqrt(a_wall_in**2-x**2) #Positive part
    z_wall_in = -(b_wall_in/a_wall_in)*np.sqrt(a_wall_in**2-x**2) #Negative part

    #Artery wall - outside layer - ellipse centered on 0 with main axis a_wall_out and small axis b_wall_out
    a_wall_out=a_wall_in*thick_wall
    b_wall_out=b_wall_in*thick_wall
    y_wall_out = +(b_wall_out/a_wall_out)*np.sqrt(a_wall_out**2-x**2)
    z_wall_out = -(b_wall_out/a_wall_out)*np.sqrt(a_wall_out**2-x**2)
    return y_wall_in,z_wall_in,y_wall_out,z_wall_out

#Lumen - circle centered in x_L, radius R_L
def lumen(x_L,R_L):
    y_lumen = +np.sqrt(R_L**2 - (x-x_L)**2)
    z_lumen = -np.sqrt(R_L**2 - (x-x_L)**2)
    return y_lumen,z_lumen

#Calcium/lipid mass - ellipse centered on x_M with main axis a_M and small axis b_M
def mass(x_M,a_M,b_M):
    y_mass = +(b_M/a_M)*np.sqrt(a_M**2-(x-x_M)**2)
    z_mass = -(b_M/a_M)*np.sqrt(a_M**2-(x-x_M)**2)
    return y_mass,z_mass

#Parameters Verification - avoid intersections

def check_intersection(y_1,y_2):
    intersect = np.argwhere(np.diff(np.sign(y_1 - y_2)) != 0).reshape(-1) + 0
    if (intersect!=[]):
        x_intersect = []
        y_intersect = []
        for idx in intersect:
            if np.isnan(y_1[idx])==False & np.isnan(y_2[idx])==False:
                x_intersect.append(x[idx])
                y_intersect.append(y_2[idx])
        if len(x_intersect)%2!=0:
            x_intersect=x_intersect[:-1]
            y_intersect=y_intersect[:-1]
        if y_intersect != []:
            plt.plot(x_intersect, y_intersect, 'bo')
            return True

            #plots
def artery_plot(a_wall_in,
                b_wall_in,
                thick_wall,
                x_L,
                R_L,
                x_M,
                a_M,
                b_M):


    y_wall_in,z_wall_in,y_wall_out,z_wall_out = artery_wall(a_wall_in, b_wall_in, thick_wall)
    plt.plot(x,y_wall_in,'b-')
    plt.plot(x,z_wall_in,'b-')
    plt.plot(x,y_wall_out,'b-')
    plt.plot(x,z_wall_out,'b-')

    y_lumen,z_lumen = lumen(x_L,R_L)
    plt.plot(x,y_lumen,'r-')
    plt.plot(x,z_lumen,'r-')

    y_mass,z_mass = mass(x_M,a_M,b_M)
    plt.plot(x,y_mass,'g-')
    plt.plot(x,z_mass,'g-')

    plot_limit = a_wall_in*thick_wall*1.1
    plt.xlim([-plot_limit,plot_limit])
    plt.ylim([-plot_limit,plot_limit])
    plt.gca().set_aspect('equal', adjustable='box')


    #verifications
    if check_intersection(y_lumen,y_wall_in):
        red_patch = mpatches.Patch(color='red', label='crossing')
        plt.legend(handles=[red_patch])
    if check_intersection(y_mass,y_wall_in):
        red_patch = mpatches.Patch(color='red', label='crossing')
        plt.legend(handles=[red_patch])
    if x_M-a_M<x_L+R_L:
        red_patch = mpatches.Patch(color='red', label='crossing')
        plt.legend(handles=[red_patch])

    plt.show()
    print("a_wall_in=%f, b_wall_in=%f, thick_wall=%f,x_L=%f, R_L=%f, x_M=%f,a_M=%f,b_M=%f"%(a_wall_in, b_wall_in, thick_wall,x_L, R_L, x_M,a_M,b_M))

for a_wall_in in [4,6]:
    for R_L in [2.2,2.7]:
        for x_M in [3,3.6]:
            for x_L in [-1.2,-0.6]:
                artery_plot(a_wall_in,b_wall_in,thick_wall,x_L,R_L,x_M,a_M,b_M)
