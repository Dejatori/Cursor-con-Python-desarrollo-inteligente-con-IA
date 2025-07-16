# Mini Data Analyst

A Python data analysis project that performs basic statistical analysis and creates visualizations from CSV data.

## Project Structure

```
mini_data_analyst/
├── datos.csv          # Sample dataset with numerical data
├── analisis.py        # Main analysis script
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Features

- 📊 **Data Loading**: Reads CSV files using pandas
- 📈 **Statistical Analysis**: Calculates mean, median, standard deviation, min, and max
- 📉 **Data Visualization**: Creates scatter plots with trend lines and correlation coefficients
- 🎨 **Professional Output**: Clean console output with formatted statistics
- 🔧 **Error Handling**: Robust error handling for file operations

## Installation

1. **Clone or download this project**

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install pandas matplotlib numpy
   ```

## Usage

### Running the Analysis

Execute the script from the command line:

```bash
python analisis.py
```

### Expected Output

The script will:

1. Load the `datos.csv` file
2. Display the first 5 rows of data
3. Calculate and print statistical measures for each column
4. Generate a scatter plot comparing the two columns
5. Show the plot in a pop-up window

### Sample Output

```
🚀 MINI DATA ANALYST
==================================================
Starting data analysis...
✅ Successfully loaded data from 'datos.csv'
   Shape: 30 rows, 2 columns

📋 First 5 rows of data:
    col1  col2
0  12.5   8.3
1  15.2  11.7
2  18.9  14.2
3  22.1  16.8
4  25.7  19.5

==================================================
📊 STATISTICAL ANALYSIS
==================================================

📈 Statistics for 'col1':
------------------------------
   Mean:     63.85
   Median:   63.85
   Std Dev:  32.50
   Min:      12.50
   Max:      115.20

📈 Statistics for 'col2':
------------------------------
   Mean:     49.85
   Median:   49.85
   Std Dev:  25.50
   Min:      8.30
   Max:      90.30

==================================================
📊 CREATING SCATTER PLOT
==================================================
✅ Scatter plot created successfully!
   Close the plot window to continue...
```

## Data Format

The script expects a CSV file with:

- Two or more columns of numerical data
- Column headers in the first row
- No missing values (for best results)

## Customization

You can modify the script to:

- Analyze different CSV files by changing the filename in `load_data()`
- Add more statistical measures
- Customize plot appearance
- Export results to files

## Requirements

- Python 3.7+
- pandas >= 1.5.0
- matplotlib >= 3.5.0
- numpy >= 1.21.0

## License

This project is open source and available under the MIT License.
