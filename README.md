# Netflix Data Analysis Project

A Python-based data analysis project that explores Netflix movies and TV shows datasets.

This project demonstrates an end-to-end data analysis workflow, including:

- Data ingestion
- Data cleaning
- Exploratory Data Analysis (EDA)
- Missing value handling
- Outlier detection
- Feature engineering
- Business intelligence dataset preparation

---

# Project Overview

The objective of this project is to analyze Netflix movie and TV show datasets and discover insights related to:

- Content distribution trends
- Country production patterns
- Release year analysis
- Movie and TV show characteristics
- Audience rating performance
- Financial performance indicators


The project combines Netflix movie and TV show datasets into a unified analytical dataset and creates additional features for downstream business analysis and visualization.


---

# Technology Stack

## Programming Language

- Python


## Data Processing

- Pandas
- NumPy


## Data Visualization

- Matplotlib
- Seaborn


## Development Environment

- VS Code
- Jupyter Notebook

## Version Control

- Git
- GitHub

# Project Structure

```
netflix-data-analysis/
│
├── data/
│   ├── README.md
│   ├── netflix_movies_detailed_up_to_2025.xls
│   └── netflix_tv_shows_detailed_up_to_2025.xls
│
├── src/
│   └── analysis.py
│
├── notebooks/
│   └── Netflix project.ipynb
│
├── output/
│   └── netflix_c_cleanedBI.csv
│
├── images/
│
├── requirements.txt
│
├── Dockerfile
│
└── README.md
```


---

# Data Pipeline

```
Netflix Movie Dataset
        |
        |
Netflix TV Show Dataset
        |
        v
Data Loading
        |
        v
Data Standardization

- Normalize column names
- Remove unnecessary spaces
- Add content type label

        |
        v

Dataset Integration

Merge Movie and TV Show datasets

        |
        v

Data Cleaning

- Remove unused columns
- Handle missing values
- Detect numerical outliers

        |
        v

Feature Engineering

- main_country
- region
- release_decade
- ROI
- vote_group
- duration_int
- duration_unit

        |
        v

Cleaned Dataset

netflix_c_cleanedBI.csv
```


---

# Analysis Workflow

## 1. Data Loading

The project loads two raw datasets:

- Netflix movie dataset
- Netflix TV show dataset


The datasets are imported using Pandas and combined into a single DataFrame.


---

## 2. Data Standardization

The following preprocessing steps are applied:

- Convert column names to lowercase
- Remove unnecessary spaces
- Add content type classification


Example:

```
Movie
TV Show
```


---

## 3. Dataset Integration

Movie and TV show datasets are merged into one unified dataset.

The final dataset contains both:

- Movie
- TV Show


This allows consistent analysis across different content types.


---

# Data Cleaning

## Removed Columns

The following columns were removed because they were not required for analytical purposes:

```
show_id
director
cast
rating
description
```


---

## Missing Value Handling

Missing values are processed according to column characteristics.

Examples:

| Column | Handling |
|---|---|
| genres | Fill with Unknown |
| country | Generate main_country |
| budget | Fill with 0 |
| revenue | Fill with 0 |


Records missing critical analytical fields are removed:

```
release_year
duration
```


---

## Outlier Detection

Numerical columns are evaluated using the IQR (Interquartile Range) method.

The process identifies potential abnormal values without directly modifying the dataset.


---

# Feature Engineering

Additional analytical features are created to support business intelligence analysis.


| Feature | Description |
|---|---|
| main_country | Extract primary production country |
| region | Classify countries into geographic regions |
| release_decade | Group content by release decade |
| ROI | Calculate return on investment |
| vote_group | Categorize ratings into High / Medium / Low |
| duration_int | Extract numerical duration value |
| duration_unit | Extract duration type |


---

# Output Dataset

After executing the analysis pipeline, the processed dataset is generated:


```
output/netflix_c_cleanedBI.csv
```


The cleaned dataset is prepared for:

- Business intelligence analysis
- Data visualization
- Exploratory data analysis
- Machine learning experiments


---

# Installation

Clone this repository:

```bash
git clone <repository-url>
```

Move into project directory:

```bash
cd netflix-data-analysis
```


Install required packages:

```bash
pip install -r requirements.txt
```


---

# How to Run

Execute the analysis pipeline:

```bash
python src/analysis.py
```


After successful execution:

```
output/netflix_c_cleanedBI.csv
```

will be generated automatically.


---

# Current Features

Implemented:

- Dataset loading
- Data merging
- Data cleaning
- Missing value handling
- IQR outlier detection
- Feature engineering
- BI-ready dataset generation


---

# Future Improvements

Potential improvements:

- Add automated visualization reports
- Build interactive dashboard using Power BI / Streamlit
- Add data validation pipeline
- Containerize execution with Docker
- Implement machine learning models for prediction


---

# Dataset Source

Dataset source:

Kaggle - Netflix Movies and TV Shows Till 2025

https://www.kaggle.com/datasets/bhargavchirumamilla/netflix-movies-and-tv-shows-till-2025


The dataset is sourced from TMDb (The Movie Database) and contains Netflix movie and TV show metadata, including content information, ratings, popularity metrics, and financial data.



# Author

Arista (@codingArista)

Python Data Analytics Portfolio Project

A self-developed data analysis project with AI-assisted development.


Built with:

- Python
- Pandas
- NumPy
- GitHub
- Git



