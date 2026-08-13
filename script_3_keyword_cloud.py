import matplotlib.pyplot as plt
from wordcloud import WordCloud
import bibtexparser
from collections import Counter
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


# 1. Load and parse the BibTeX file
# Replace with your actual file path
bibtex_file_path = os.path.join(data_folder, "key_words_latest_contribution.bib")

# with open(bibtex_file_path, "r", encoding="utf-8") as bibtex_file:
#     bib_database = bibtexparser.parse_file(bibtex_file)
bib_database = bibtexparser.parse_file(bibtex_file_path)
# 2. Extract and clean keywords
keywords_list = []

for entry in bib_database.entries:
  # BibTeX entries usually store keywords in the 'keywords' field
  raw_keywords = None
  for field in ["keywords", "Keywords", "keyword", "KEYWORD"]:
      if field in entry:
          raw_keywords = entry[field]
          break

  if raw_keywords:
    for sep in [";", "/", "\n"]:
      raw_keywords = raw_keywords.replace(sep, ",")

    split_keywords = [kw.strip().lower() for kw in raw_keywords.split(",")]

    # Filter out empty strings
    for kw in split_keywords:
      if kw:
        keywords_list.append(kw)

# 3. Combine keywords into a single text block for the WordCloud generator
keyword_counts = Counter(keywords_list)

formatted_word_freqs = {
    word.replace("_", " "): count for word, count in keyword_counts.items()
}

# 4. Generate the Word Cloud
# All attributes can be adjusted, specially 'max_words'
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    colormap="viridis",
    max_words=10,
).generate_from_frequencies(formatted_word_freqs)

# 5. Display the result using Matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig(os.path.join(output_directory, "Figure_5_10_08_26.tiff"), format='tiff', bbox_inches='tight', dpi=300, pil_kwargs={'compression': 'tiff_lzw'})
plt.show()