# LEGO Sets and Colors Analysis README

## Overview
This project provides a Python script to analyze LEGO sets and colors data. The main objectives are to determine the number of distinct colors available, summarize colors based on their transparency, analyze trends in the average number of parts in LEGO sets by year, and determine the number of unique themes released in a specific year (1999 in this case).

## Dependencies
- Python 3.x
- pandas
- matplotlib

## Dataset
Two datasets are used in this project:

1. `colors.csv`: Contains information about LEGO colors.
   - Expected columns: rgb (color code), is_trans (transparency indicator).
   
2. `sets.csv`: Contains information about LEGO sets.
   - Expected columns: year (release year of the set), num_parts (number of parts in the set), theme_id (ID of the theme of the set).

Both datasets should be placed in a folder named `datasets` in the root directory of the project.

## Usage

1. Place the `colors.csv` and `sets.csv` data files in the `datasets` directory.
2. Run the script. The script will:
   - Load the data.
   - Analyze and print the number of distinct colors.
   - Summarize colors based on their transparency.
   - Plot trends in the average number of parts in LEGO sets by year.
   - Determine and print the number of unique themes released in 1999.
3. Analyze the results and visualizations.

## Analysis Results

- Number of distinct colors available.
- Summary of colors based on their transparency.
- A plot showing trends in the average number of parts in LEGO sets by year.
- Number of unique themes released in 1999.

## Future Improvements

- Extend the analysis to consider other aspects of LEGO sets, such as popularity or sales figures.
- Visualize the data using more advanced graphs and charts for a deeper understanding of the trends.
- Integrate with a database for more efficient data storage and retrieval.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
