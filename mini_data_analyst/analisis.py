#!/usr/bin/env python3
"""
Mini Data Analyst - Basic Data Analysis and Visualization Script

This script reads a CSV file containing numerical data, performs basic statistical
analysis, and generates a scatter plot comparing two columns.

Author: Mini Data Analyst
Date: 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from pathlib import Path

def load_data(csv_file='datos.csv'):
    """
    Load data from CSV file using pandas.
    
    Args:
        csv_file (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame: Loaded data
    """
    try:
        data = pd.read_csv(csv_file)
        print(f"✅ Successfully loaded data from '{csv_file}'")
        print(f"   Shape: {data.shape[0]} rows, {data.shape[1]} columns")
        return data
    except FileNotFoundError:
        print(f"❌ Error: File '{csv_file}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        sys.exit(1)

def perform_statistical_analysis(data):
    """
    Perform basic statistical analysis on the data.
    
    Args:
        data (pandas.DataFrame): Input data
        
    Returns:
        dict: Dictionary containing statistical measures
    """
    print("\n" + "="*50)
    print("📊 STATISTICAL ANALYSIS")
    print("="*50)
    
    stats = {}
    
    for column in data.columns:
        print(f"\n📈 Statistics for '{column}':")
        print("-" * 30)
        
        # Calculate basic statistics
        mean_val = data[column].mean()
        median_val = data[column].median()
        std_val = data[column].std()
        min_val = data[column].min()
        max_val = data[column].max()
        
        # Store statistics
        stats[column] = {
            'mean': mean_val,
            'median': median_val,
            'std': std_val,
            'min': min_val,
            'max': max_val
        }
        
        # Print statistics
        print(f"   Mean:     {mean_val:.2f}")
        print(f"   Median:   {median_val:.2f}")
        print(f"   Std Dev:  {std_val:.2f}")
        print(f"   Min:      {min_val:.2f}")
        print(f"   Max:      {max_val:.2f}")
    
    return stats

def create_scatter_plot(data, col1='col1', col2='col2'):
    """
    Create and display a scatter plot comparing two columns.
    
    Args:
        data (pandas.DataFrame): Input data
        col1 (str): Name of the first column (x-axis)
        col2 (str): Name of the second column (y-axis)
    """
    print("\n" + "="*50)
    print("📊 CREATING SCATTER PLOT")
    print("="*50)
    
    # Set up the plot
    plt.figure(figsize=(10, 8))
    
    # Create scatter plot
    plt.scatter(data[col1], data[col2], 
                alpha=0.7, 
                s=60, 
                c='steelblue', 
                edgecolors='white', 
                linewidth=1)
    
    # Add trend line
    z = np.polyfit(data[col1], data[col2], 1)
    p = np.poly1d(z)
    plt.plot(data[col1], p(data[col1]), "r--", alpha=0.8, linewidth=2)
    
    # Customize the plot
    plt.xlabel(f'{col1}', fontsize=12, fontweight='bold')
    plt.ylabel(f'{col2}', fontsize=12, fontweight='bold')
    plt.title(f'Scatter Plot: {col1} vs {col2}\nMini Data Analyst Project', 
              fontsize=14, fontweight='bold', pad=20)
    
    # Add grid
    plt.grid(True, alpha=0.3)
    
    # Add correlation coefficient
    correlation = data[col1].corr(data[col2])
    plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
             transform=plt.gca().transAxes, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.8),
             fontsize=10)
    
    # Adjust layout and display
    plt.tight_layout()
    print("✅ Scatter plot created successfully!")
    print("   Close the plot window to continue...")
    plt.show()

def main():
    """
    Main function to orchestrate the data analysis workflow.
    """
    print("🚀 MINI DATA ANALYST")
    print("="*50)
    print("Starting data analysis...")
    
    # Load data
    data = load_data()
    
    # Display first few rows
    print(f"\n📋 First 5 rows of data:")
    print(data.head())
    
    # Perform statistical analysis
    stats = perform_statistical_analysis(data)
    
    # Create scatter plot
    if len(data.columns) >= 2:
        col1, col2 = str(data.columns[0]), str(data.columns[1])
        create_scatter_plot(data, col1, col2)
    else:
        print("❌ Error: Need at least 2 columns for scatter plot!")
        sys.exit(1)
    
    print("\n" + "="*50)
    print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
    print("="*50)

if __name__ == "__main__":
    main()
