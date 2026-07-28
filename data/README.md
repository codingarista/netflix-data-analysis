# Dataset Description

This folder contains the raw datasets used for the Netflix data analysis project.

# Dataset Source

The original dataset is obtained from Kaggle:

Netflix Movies and TV Shows Till 2025

https://www.kaggle.com/datasets/bhargavchirumamilla/netflix-movies-and-tv-shows-till-2025


Original data source:

TMDb (The Movie Database)


The dataset contains Netflix movie and TV show metadata, including titles, genres, release information, ratings, popularity metrics, and financial information.

---

## Dataset Files

| File | Description |
|---|---|
| netflix_movies_detailed_up_to_2025.xls | Raw Netflix movie dataset containing movie metadata, popularity metrics, and financial information |
| netflix_tv_shows_detailed_up_to_2025.xls | Raw Netflix TV show dataset containing TV show metadata and related information |

---


# Dataset Structure

The raw datasets contain the following information:

| Category | Description |
|---|---|
| Title Information | Movie and TV show titles |
| Content Type | Movie / TV Show classification |
| Country | Production country information |
| Release Information | Release year and date information |
| Genre Information | Content genre categories |
| Language | Original language information |
| Popularity Metrics | Popularity score and vote count |
| Rating Metrics | Average user rating |
| Financial Information | Budget and revenue information |
| Duration Information | Runtime or season information |


## Data Processing Pipeline

The raw datasets are processed through the following workflow:

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

Normalize column names
Remove unnecessary spaces
Add content_type label
|
v
Dataset Integration
Combine Movie and TV Show datasets
|
v
Data Cleaning
Remove unnecessary columns
Handle missing values
Detect numerical outliers using IQR method
|
v
Feature Engineering
main_country
region
release_decade
ROI
vote_group
duration_int
duration_unit
|
v
Processed Dataset
netflix_c_cleanedBI.csv


## Dataset Information

The datasets contain Netflix movie and TV show information, including:

- Title information
- Content type (Movie / TV Show)
- Country
- Release year
- Genres
- Language
- Popularity metrics
- Vote count
- Vote average
- Budget
- Revenue
- Duration information

---

## Data Processing Steps

### 1. Data Loading

Load Netflix movie and TV show datasets from this folder.

### 2. Data Standardization

The datasets are standardized by:

- Converting column names to lowercase
- Removing unnecessary spaces
- Adding content type labels

### 3. Dataset Integration

The movie and TV show datasets are merged into a single analytical dataset.

This allows consistent analysis across different content types.


### 4. Data Cleaning

The cleaning process includes:

- Removing unnecessary columns
- Handling missing values
- Removing records with missing critical fields
- Detecting numerical outliers using IQR method

Remove unnecessary columns

The following columns are removed because they are not required for analytical purposes:

```text
show_id
director
cast
rating
description

Missing value handling

Missing values are processed based on column characteristics:

| Column  | Processing                       |
| ------- | -------------------------------- |
| genres  | Fill missing values with Unknown |
| country | Extract main_country feature     |
| budget  | Fill missing values with 0       |
| revenue | Fill missing values with 0       |


Remove records with missing critical fields

Records missing important analytical fields are removed:

release_year
duration

Outlier detection

Numerical columns are evaluated using the IQR (Interquartile Range) method to identify potential abnormal values.

The detected outliers are analyzed but not directly removed from the dataset.


### 5. Feature Engineering

Additional analytical features are created:

| Feature | Description |
|---|---|
| main_country | Extract the primary country from country information |
| region | Classify countries into geographic regions |
| release_decade | Group content by release decade |
| ROI | Calculate return on investment |
| vote_group | Categorize ratings into High / Medium / Low |
| duration_int | Extract numerical duration value |
| duration_unit | Extract duration type (Movie / TV Show related unit) |

---

## Output Dataset

After running the analysis pipeline, the processed dataset will be generated:

output/netflix_c_cleanedBI.csv

This cleaned dataset is used for:

- Business intelligence analysis
- Visualization
- Exploratory data analysis
- Further modeling experiments


## Usage

Run the analysis pipeline from the project root directory:

```bash
python src/analysis.py