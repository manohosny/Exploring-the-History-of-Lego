# Import pandas
import pandas as pd

# Read colors data
colors = pd.read_csv('datasets/colors.csv')

# Print the first few rows
colors.head()

# How many distinct colors are available?
num_colors = colors.rgb.size

# Print num_colors
print('Number of distinct colors:', num_colors)

# Summarize colors based on whether they are transparent or not?
colors_summary = colors.groupby('is_trans').count()
colors_summary

%matplotlib inline
# Read sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')

# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets[['year', 'num_parts']].groupby('year').mean()

# Plot trends in average number of parts by year
parts_by_year.plot()

# themes_by_year: Number of themes shipped by year
themes_by_year = sets.groupby('year')[['theme_id']].nunique()
themes_by_year.head()

# Get the number of unique themes released in 1999
num_themes = themes_by_year.loc[1999,'theme_id']

# Print the number of unique themes released in 1999
print(num_themes)
