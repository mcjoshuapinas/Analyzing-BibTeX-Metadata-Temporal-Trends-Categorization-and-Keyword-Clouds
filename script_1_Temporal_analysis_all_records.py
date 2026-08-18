import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

def make_autopct(values):
    def my_autopct(pct):
        # Calculate the absolute value based on the percentage
        total = sum(values)
        val = int(round(pct * total / 100.0))
        # Return formatted string: "Count (Percentage)"
        return f'{val}\n({pct:.1f} %)'
    return my_autopct

# --- PATH CONFIGURATION ---
# Get the absolute path of the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative paths for data input and results output
# This ensures the code works on any computer without modification
output_directory = os.path.join(BASE_DIR, "output")

# Create the output directory automatically if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# --- DATA LOADING: SURVEY RESPONSES ---
# Path to the thermal comfort survey CSV file
my_lib_articles = os.path.join(output_directory, "count_articles.csv")
my_lib_conference = os.path.join(output_directory, "count_inproceedings.csv")
my_lib_report = os.path.join(output_directory, "count_report.csv")
my_lib_thesis = os.path.join(output_directory, "count_phdthesis.csv")
my_lib_book = os.path.join(output_directory, "count_book.csv")
my_lib_chapter = os.path.join(output_directory, "count_chapter.csv")

#dataframe reading
df_articles = pd.read_csv(my_lib_articles, sep='\t', header=None)
df_articles.columns = ['year', 'nb_articles']
df_conference = pd.read_csv(my_lib_conference, sep='\t', header=None)
df_conference.columns = ['year', 'nb_conference']
df_report = pd.read_csv(my_lib_report, sep='\t', header=None)
df_report.columns = ['year', 'nb_report']
df_thesis = pd.read_csv(my_lib_thesis, sep='\t', header=None)
df_thesis.columns = ['year', 'nb_thesis']
df_book = pd.read_csv(my_lib_book, sep='\t', header=None)
df_book.columns = ['year', 'nb_book']
df_chapter = pd.read_csv(my_lib_chapter, sep='\t', header=None)
df_chapter.columns = ['year', 'nb_chapter']

#coupling dataframes
df_nb = df_articles['nb_articles'] + df_conference['nb_conference'] + df_report['nb_report'] + df_thesis['nb_thesis'] + df_book['nb_book'] + df_chapter['nb_chapter']
df_total = pd.concat([df_articles['year'], df_nb], axis=1)
#_____________________________________________________________________________________________________________
df_total.columns = ['year', 'nb_total']
df_year_nb_per_type = pd.concat([df_articles['year'], df_articles['nb_articles'],  df_conference['nb_conference'], df_thesis['nb_thesis'], df_report['nb_report'], df_total['nb_total']], axis=1)

#_____________________________________________________________________________________________________________
y_stack = df_year_nb_per_type[['nb_articles', 'nb_conference', 'nb_thesis', 'nb_report']].values.T
#_____________________________________________________________________________________________________________
# 1. Configuration
years = np.arange(1979, 2027) # 48 années
n_categories = 5
width = 0.15  # Largeur de chaque petite barre
x = np.arange(len(years))  # Position centrale pour chaque année

#ploting
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8), constrained_layout=True)

# 2. Data and style definitions
data = [df_articles['nb_articles'], df_conference['nb_conference'],
        df_thesis['nb_thesis'], df_report['nb_report'], df_nb]
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#9467BD', '#D62728']
labels = ['PRA', 'CA', 'DD', 'TR', 'T']
sizes = [89, 34, 20, 17, 4]
# 3. Offset Path
for i in range(n_categories):
    # Le calcul x - (n_categories/2)*width + i*width permet de centrer le groupe
    offset = (i - n_categories / 2) * width + width / 2
    ax1.bar(x + offset, data[i], width=width, label=labels[i], color=colors[i], zorder=3)

# 4. Configuration of plot 1
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=90, fontsize=8)
ax1.legend()
ax1.text(0.98, 0.92, '(a)', transform=ax1.transAxes, fontsize=10,
         fontweight='bold', va='top', ha='right')

ax1.set_ylabel('Number of records',
         fontsize=10, fontweight='bold',
         va='center', ha='center', rotation=90)

# 4. Configuration of plot 2
ax2.stackplot(df_year_nb_per_type['year'], y_stack, labels=['PRA', 'CA', 'DD', 'TR'], colors=['#1F77B4', '#FF7F0E', '#2CA02C', '#9467BD'])
ax2.legend(loc='upper right')
ax2.set_xticks(df_year_nb_per_type['year'])
ax2.set_xticklabels(df_year_nb_per_type['year'], rotation=90, fontsize=8)
ax2.legend()
ax2.text(0.98, 0.92, '(b)', transform=ax2.transAxes, fontsize=10,
         fontweight='bold', va='top', ha='right')
ax2.set_ylabel('Number of records',
         fontsize=10, fontweight='bold',
         va='center', ha='center', rotation=90)

ax2.set_xlabel('Year of publication', fontsize=10, fontweight='bold')
# 4. Configuration of plot 3
ax3.pie(sizes, labels=['PRA', 'CA', 'DD', 'TR', 'B'], colors=['#1F77B4', '#FF7F0E', '#2CA02C', '#9467BD', '#8C564B'],
        autopct=make_autopct(sizes),
        startangle=0,
        pctdistance=1.28,
        labeldistance=0.8,
        )
ax3.text(0.98, 0.98, '(c)', transform=ax3.transAxes, fontsize=10,
        fontweight='bold', va='top', ha='right')
# 5. Saving figure as .tiff file
plt.savefig(os.path.join(output_directory, "Figure_2_18_08_26.tiff"), format='tiff', bbox_inches='tight', dpi=800, pil_kwargs={'compression': 'tiff_lzw'})
plt.show()
