# A.I. Robustness: a Human-Centered Perspective on Technological Challenges and Opportunities
**Politecnico di Milano and Delft University of Technology**

## Table of Content
* [1. Data Collection](#data-collection)
* [2. Scripts](#scripts)

## 1. Data Collection
The documents in the repository contain the papers at different steps of the 
 * Downloaded Papers - The original list of 100'000 papers collected through 156 unique queries.
 * Classified Papers - The list of 1'800 papers inspected by the authors, organized in four batches.
 * Final List of Articles - The final list of 560 papers considered in the review.

The keywords for the queries can be find in [Queries Scopus & Google Scholar](https://github.com/AndreaTocchetti/ACMReviewPaperPolimiDelft/blob/main/Scripts/Article%20Download/queries_scopus.txt) and [Queries Semantic Scholar & Web of Science](https://github.com/AndreaTocchetti/ACMReviewPaperPolimiDelft/blob/main/Scripts/Article%20Download/queries_semscholar.txt)

## 2. Scripts
The Scripts folder contains the Python scripts used to manage the documents (e.g., duplicate removal).

### 2.1. Article Download
> Note: To be able to use the included scripts, Publish or Perish CLI needs to be installed. See [this guide](https://harzing.com/resources/publish-or-perish/command-line) for instructions on how to do so.

This folder contains the scripts used to download papers from Scopus, Semantic Scholar, and Web of Science alongside the respective queries.

Google Scholar was done manually through [Publish or Perish](https://harzing.com/resources/publish-or-perish).

### 2.2. Merge Keywords
This folder contains the scripts used for exploring papers and removing duplicates, as described in the survey paper.
