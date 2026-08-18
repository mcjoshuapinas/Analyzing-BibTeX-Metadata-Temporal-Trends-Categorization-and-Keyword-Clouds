import bibtexparser
from collections import Counter
import matplotlib.pyplot as plt
import os

def get_year(block):
    year_field = block.get('year')
    if year_field:
        return str(year_field.value).strip()
    return None

def get_scale(block):
    scale_field = block.get('scale')
    if scale_field:
        return str(scale_field.value).strip()
    return None

def get_method(block):
    method_field = block.get('method')
    if method_field:
        return str(method_field.value).strip()
    return None

def get_topic(block):
    topic_field = block.get('topic')
    if topic_field:
        return str(topic_field.value).strip()
    return None

# --- PATH CONFIGURATION ---
# Get the absolute path of the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative paths for data input and results output
# This ensures the code works on any computer without modification
data_folder = os.path.join(BASE_DIR, "data")
output_directory = os.path.join(BASE_DIR, "output")

my_lib_filename = os.path.join(data_folder, "Considered_citations_step_2_3_n_89_classement.bib")

articles = bibtexparser.parse_file(my_lib_filename)
# 2. Track classifications
#scale = material, wall, building
#method = theoretical, numerical, experimental, both
#topic = analysis, reduced, modeling, simulation, synthesis
#all_years = [get_year(b) for b in articles.blocks if hasattr(b, 'entry_type')]
#valid_years = [int(year) for year in all_years if year and year.isdigit() and year != 'None']
scale = [get_scale(b) for b in articles.blocks if hasattr(b, 'entry_type')]
method = [get_method(b) for b in articles.blocks if hasattr(b, 'entry_type')]
topic = [get_topic(b) for b in articles.blocks if hasattr(b, 'entry_type')]

scale_count = Counter(scale)
method_count = Counter(method)
topic_count = Counter(topic)

print("\nNombre de publications par scale type :")
for scale_type in ['material', 'wall', 'building']:
    print(f"{scale_type} : {scale_count[scale_type]} article(s)")

print("\nNombre de publications par method type :")
for method_type in ['theoretical', 'numerical', 'both']:
    print(f"{method_type} : {method_count[method_type]} article(s)")

print("\nNombre de publications par topic type :")
for topic_type in ['analysis', 'reduced', 'synthesis', 'modeling', 'simulation']:
    print(f"{topic_type} : {topic_count[topic_type]} article(s)")

# 3. Summary Report

# 4. Generate a Pie Chart or Bar Plot of the Contribution Scales
labels = ['Material', 'Wall', 'Building']
sizes = [scale_count['material'], scale_count['wall'], scale_count['building']+1]
colors = ['#a6cee3', '#1f78b4', '#b2df8a']  # Gradient blue theme

plt.figure(figsize=(7, 5))
plt.bar(labels, sizes, color=colors, edgecolor='#333333', width=0.6)
plt.ylabel("Number of Articles", fontsize=11, fontweight='bold')
plt.title("Distribution of Articles by Contribution Scale", fontsize=12, fontweight='bold', pad=15)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Clear top/right lines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add value tags above bars
for i, v in enumerate(sizes):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(output_directory, "Figure_3_a.tiff"), format='tiff', bbox_inches='tight', dpi=600, pil_kwargs={'compression': 'tiff_lzw'})
plt.show()

#_________________________________________________________________________
labels_method = ['Theoretical', 'Numerical', 'Both (num. & exp.']
sizes_method = [method_count['theoretical'], method_count['numerical'],
                method_count['both']]
colors = ['#33a02c', '#fb9a99', '#e31a1c']  # Gradient blue theme

plt.figure(figsize=(7, 5))
plt.bar(labels_method, sizes_method, color=colors, edgecolor='#333333', width=0.6)
plt.ylabel("Number of Articles", fontsize=11, fontweight='bold')
plt.title("Distribution of Articles by Contribution Method", fontsize=12, fontweight='bold', pad=15)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Clear top/right lines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add value tags above bars
for i, v in enumerate(sizes_method):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(output_directory, "Figure_3_b.tiff"), format='tiff', bbox_inches='tight', dpi=600, pil_kwargs={'compression': 'tiff_lzw'})
plt.show()

#_________________________________________________________________________
labels_topic = ['Modal Analysis', 'Modal Reduction', 'Modal Synthesis', 'Modal Modeling', 'Modal simulation']
sizes_topic = [topic_count['analysis'], topic_count['reduced'], topic_count['synthesis'], topic_count['modeling']
               ,topic_count['simulation']]
colors = ['#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#b15928']  # Gradient blue theme

plt.figure(figsize=(7, 5))
plt.bar(labels_topic, sizes_topic, color=colors, edgecolor='#333333', width=0.6)
plt.ylabel("Number of Articles", fontsize=11, fontweight='bold')
plt.title("Distribution of Articles by Contribution Topic", fontsize=12, fontweight='bold', pad=15)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Clear top/right lines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add value tags above bars
for i, v in enumerate(sizes_topic):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(output_directory, "Figure_3_c.tiff"), format='tiff', bbox_inches='tight', dpi=600, pil_kwargs={'compression': 'tiff_lzw'})
plt.show()