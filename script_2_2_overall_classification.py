import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

# --- PATH CONFIGURATION ---
# Get the absolute path of the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative paths for data input and results output
# This ensures the code works on any computer without modification
data_folder = os.path.join(BASE_DIR, "data")
output_directory = os.path.join(BASE_DIR, "output")

# Create the output directory automatically if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# the following information can be verified using 'Considered_citations_step_2_3_n_83_classement.bib'
data = [
    (
        ['Material', 'Wall', 'Building'],
        [8, 23, 58],
        ['#a6cee3', '#1f78b4', '#b2df8a'],
        '(a)'
    ),
    (
        ['Theoretical', 'Numerical', 'Both (num. & exp.)'],
        [7, 64, 18],
        ['#33a02c', '#fb9a99', '#e31a1c'],
        '(b)'
    ),
    (
        ['Modal Analysis', 'Modal Reduction', 'Modal Synthesis', 'Modal Modeling', 'Modal simulation'],
        [14, 27, 3, 9, 36],
        ['#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#b15928'],
        '(c)'
    )
]

fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(2,2, height_ratios=[1, 1], hspace=0.2, wspace=0.2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, :])
axes = [ax1, ax2, ax3]
for i, ax in enumerate(axes):
    labels, values, colors, label_fig = data[i]

    # Tracé des barres
    bars = ax.bar(labels, values, color=colors, edgecolor='#444', linewidth=1.2, alpha=0.8)

    # --- CORRECTION CLÉ ICI ---
    # Calculer la valeur maximale et ajouter une marge (ex: 10%)
    y_max = max(values) * 1.15
    ax.set_ylim(0, y_max)

    # Ajouter le texte (a), (b), (c) en haut à droite
    ax.text(0.98, 0.96, label_fig, transform=ax.transAxes, fontsize=11,
            fontweight='bold', va='top', ha='right')

    # Grid, ticks, et style
    ax.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
    ax.set_axisbelow(True)

    # Étiquettes sur les barres (annotées en gras)
    for bar in bars:
        height = bar.get_height()
        # Le texte est placé à 'height + 1', ce qui sera toujours visible
        # car l'axe Y a été étendu.
        ax.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                f'{height}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Titre de l'axe Y global (centré sur toute la figure)
fig.text(0.05, 0.5, 'Number of articles', va='center', rotation='vertical', fontsize=11, fontweight='bold')

# plt.tight_layout(rect=[0.06, 0.02, 1, 1])
plt.savefig(os.path.join(output_directory, "Figure_3_18_08_26.tiff"), format='tiff', bbox_inches='tight', dpi=800, pil_kwargs={'compression': 'tiff_lzw'})
plt.show()
