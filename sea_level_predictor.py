import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data points')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create array of years from 1880 to 2050
    years_extended = np.arange(1880, 2051)
    line_of_best_fit = slope * years_extended + intercept


    # Plot the regression line
    plt.plot(years_extended, line_of_best_fit, color='red', label='1st Line of Best Fit')


    # Create second line of best fit

    # Filter data for years from 2000 to the most recent year
    df_filtered = df[df['Year'] >= 2000]


    # Perform linear regression on the filtered data
    slope, intercept, r_value, p_value, std_err = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])

    # Create array of years from 2000 to 2050
    years_recent_extended = np.arange(2000, 2051)
    line_of_best_fit_recent = slope * years_recent_extended + intercept

    # Plot the regression line
    plt.plot(years_recent_extended, line_of_best_fit_recent, 
            color='green', label='2nd Line of Best Fit')

    
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Show legend
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()