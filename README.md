# Analyzing-BibTeX-Metadata-Temporal-Trends-Categorization-and-Keyword-Clouds
These Python scripts analyze BibTeX metadata for the purpose of reviewing articles.
There are four Python scripts, its usage can be understood by four consecutive steps.
- The first script named 'script_0_counting_records_per_document_type_and_publication_year.py' allows to read five BibTex files, previously categorized by peer-reviewed articles, conferences articles, doctoral dissertations, books, chapters and technical reports. It comtabilizes each kind of records by publication year, and it generates an independant CSV file.
- The second script named 'script_1_Temporal_analysis_all_records.py' enables to plot in a three subplot figure the temporal distribution of 164 reviewed records by publication year and document type. (a) Bar chart showing annual counts. (b) Stacked area chart illustrating cumulative trends. (c) Pie chart showing proportional distribution by document type. It requires the five CSV files generated in the previous step.
- The third script named 'script_2_2_overall_classification.py' allows to plot in three subplot figure the categorization of the 83 peer-reviewed articles. The data included in this script can be verified using the script named 'script_2_1_individual_classification.py' which needs the modified BibTex file 'Considered_citations_step_2_3_n_89_classement.bib'. The latter includes three aditional labels (scale, method, and topic).
- The fourth script named 'script_3_keyword_cloud.py' creates a customized keyword cloud figure. It requires 'key_words_latest_contribution.bib' which contains peer-reviewed articles and conferences articles.
All generated figures are .TIFF with a customized DPI. Other kinds of file can be as well generated.

Citation 
If you use this software in your research or industrial laboratory, please cite it as follows: DOI Code snippet @software{pinas_bib_2026, author = {Piñas, Joshua}, title = {Analyzing BibTeX metadata: temporal trends, categorization and keyword clouds}, year = {2026}, publisher = {Zenodo}, doi = {10.5281/zenodo.21922007}, url = {https://github.com/mcjoshuapinas/Analyzing-BibTeX-Metadata-Temporal-Trends-Categorization-and-Keyword-Clouds} }
or 
Piñas, Joshua. (2026). Analyzing BibTeX metadata: temporal trends, categorization and keyword clouds (Version v2.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21922007
