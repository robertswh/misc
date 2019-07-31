# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:54:19 2017

@author: roberw
"""

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import time as tm


#Area of a circle is pi*r**2
#if we know the area of a square with side = 1m is 1m^2 then the probability
#that a randomly placed dot in the square is within a circle that fits
#perfectly indise the square is pi*r^2/1. If the number of dots inside the
#circle is n and the total number of dots is N then we arrive at the equation
#n/N = pi*r^2 /1. We can then re-arrange to get
#pi = n/(N*r^2)


def create_random_coordinates(n_points):
    x = np.random.rand(n_points) - 0.5
    y = np.random.rand(n_points) - 0.5
    df = pd.DataFrame({'x_coordinate':x,
                       'y_coordinate':y})
    return df


def get_distance_from_origin(df):
    df['dist_origin'] = np.sqrt(df['x_coordinate']**2 +\
                                df['y_coordinate']**2)
    return df


def add_circle_flag(df):
    df['within_circle'] = np.where(df['dist_origin']<=0.5, 1, 0)
    return df


def plot_coordinates(df):
    plt.clf()
    df_circle = df[df['within_circle'] == 1]
    df_not_circle = df[df['within_circle'] == 0]
    plt.plot(df_circle['x_coordinate'], df_circle['y_coordinate'], 'ro')
    plt.plot(df_not_circle['x_coordinate'], df_not_circle['y_coordinate'], 'bo')
    plt.xlim(-0.5,0.5)
    plt.ylim(-0.5,0.5)
    my_pi = len(df_circle) / (len(df)*0.5**2)
    result = 'No of point: %d\npi = %.3f'%(len(df), my_pi)
    plt.annotate(s=result, xy=(0,0))

def create_data_and_plot(n_points):
    df = create_random_coordinates(n_points)
    df = get_distance_from_origin(df)
    df = add_circle_flag(df)
    plot_coordinates(df)

n_list = np.array([10,100,1000,10000])
for n in n_list:
    plt.figure()
    create_data_and_plot(n)

#not used in loop
def calculate_pi(df):
    return np.sum(df['within_circle']) / (len(df) * 0.5**2)

monte_pi = calculate_pi(df)