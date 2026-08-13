import bibtexparser
from collections import Counter
import os
import pandas as pd
def get_year(block):
    """Extracts DOI or a cleaned title for matching using v2 Field values."""
    # Try DOI first. In v2, .get() returns a Field object.
    year_field = block.get('year')
    if year_field:
        # We access the .value attribute of the Field object
        return str(year_field.value).strip()
    return None

# --- PATH CONFIGURATION ---
# Get the absolute path of the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative paths for data input and results output
# This ensures the code works on any computer without modification
data_folder = os.path.join(BASE_DIR, "data")
output_directory = os.path.join(BASE_DIR, "output")

#File nane
bib_files_config = [
    {'file': "modal_only_techreport_step_2_2_n_17.bib", 'type': 'report'},
    {'file': "Considered_citations_step_2_3_n_83.bib",       'type': 'article'},
    {'file': "modal_only_book_step_2_2_n_1.bib",          'type': 'book'},
    {'file': "modal_only_incollection_step_2_2_n_2.bib", 'type': 'chapter'},
    {'file': "modal_only_inproceedings_step_2_3_n_34.bib", 'type': 'inproceedings'},
    {'file': "modal_only_phdthesis_step_2_2_n_20.bib",     'type': 'phdthesis'}
]

sorted_years = list(range(1979, 2027))
all_publications_data = {}

for item in bib_files_config:
    # Construction dynamique du chemin complet
    filepath = os.path.join(data_folder, item['file'])
    type_name = item['type']

    if not os.path.exists(filepath):
        print(f"⚠️  Fichier non trouvé : {filepath}")
        continue

    try:
        with open(filepath, encoding='utf-8') as bibtex_file:
            articles = bibtexparser.parse_file(bibtex_file)

        all_years = [get_year(b) for b in articles.blocks if hasattr(b, 'entry_type')]

        valid_years = [int(year) for year in all_years if year and year.isdigit() and year != 'None']

        publications_per_year = Counter(valid_years)
        all_publications_data[type_name] = publications_per_year

        print(f" '{type_name}' : {len(valid_years)} total number of years extracted.")

    except Exception as e:
        print(f" Error in {item['file']} : {e}")

#------------------------------------------------------------------------------
print("\nGenerating CSV files...")

for type_name, pub_counter in all_publications_data.items():
    # Sorting Data for Chronological Display
    sorted_counts = [pub_counter.get(str(year), 0) for year in sorted_years]

    df = pd.DataFrame({
        'Year': sorted_years,
        'Count': sorted_counts
    })

    output_file = os.path.join(output_directory, f'count_{type_name}.csv')

    # Saving data as CSV file
    df.to_csv(output_file, index=False, header=False, sep='\t')
    print(f" Saved : {output_file}")

print("\nIt's done.")
