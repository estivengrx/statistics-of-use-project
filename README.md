# Statistics of Use Project

This project aims to analyze usage statistics from various devices collected through the StayFree application. The data is initially in Excel format and is processed and transformed into CSV files for further analysis.
The primary source of data stems from the StayFree application, capturing insights into user behaviors and interactions. The dataset is initially structured in Excel format and is subsequently processed and transformed into CSV files for streamlined analysis.

The data is from 10/19/2022 to 04/21/2024.

The inspiration for this project arises from the increasing need to comprehend and derive meaningful patterns from the vast array of my own device usage data. By delving into the statistics provided by StayFree, we aim to uncover valuable insights that can inform user habits, preferences, and the broader landscape of digital engagement.

## Key Insights from EDA, (Exploratory Data Analysis), and PowerBi report
![PowerBi report of the data](https://github.com/estivengrx/statistics-of-use-project/blob/main/statistics_of_use_power_bi_model_page-0001.jpg)
- The most used applications on the phone are WhatsApp, Instagram, YouTube, Chrome, and Spotify, while the most visited websites using the Edge browser are YouTube, Instagram, HBO Max, WhatsApp Web, and ChatGPT.

- The distribution of phone usage time tends to follow a normal distribution, with around 250 minutes being the most common usage duration. In contrast, the distribution of web browser usage time is skewed to the left, indicating fewer instances of prolonged web usage compared to phone usage.

- Phone usage tends to remain relatively steady across weekdays, with a slight increase during weekends. However, website usage is noticeably higher on weekends compared to weekdays, with Mondays being the least used day for both phone and web.

- The middle part of the year (likely influenced by mid-year college holidays) exhibits the highest phone usage, while web usage is lowest during this period.

- The analysis accounts for missing data by ensuring that dates present in one dataset are also present in the other datasets, providing a complete picture of usage patterns.

- A breakdown of device usage per month reveals that phone usage is consistently higher than web usage (both Edge and Chrome) across all months. However, web usage peaks during certain months, potentially indicating periods of increased online activity.

- On average, phone usage (5.76 hours) exceeds Edge browser usage (4.05 hours), suggesting a higher reliance on mobile applications compared to web browsing.

- An examination of phone usage throughout the week reveals a distinct pattern: usage is lowest on Mondays and gradually increases, peaking on Sundays. This trend could be influenced by work-life balance dynamics and leisure time availability.

- The distribution of phone and Edge usage by weekday further reinforces the observation that weekends (Saturday and Sunday) experience significantly higher usage compared to weekdays.

## Project Structure

- `reports/`: Contains the PowerBi reports that where made extracting the data from the SQLServer local database.
- `data/`: Contains raw data in Excel format and processed data in CSV format.
- `python_notebooks/`: Contains Jupyter notebooks for data transformation and unification.
- `python_scripts/`: Contains Python scripts for data transformation, unification, and uploading data to the database.
- `sql/`: Contains SQL queries used in the project.
- `requirements.txt`: Lists the Python dependencies required for this project.

## Main notebooks
- `EDA.ipynb`: It contains the EDA of the most important data, the phone usage time and the web usage time
  
## Main Scripts

- `from_excel_to_transformed_dataframes.py`: Transforms raw Excel data into processed dataframes.
- `unifying_data.py`: Unifies data from different dates.
- `database_upload_files.py`: Handles uploading data to the database.
- `data_transformation_tests.ipynb`: Contains tests for data transformation.

## How to Run

1. Clone this repository.
2. Navigate to the project directory.
3. Make sure the the paths of the files and directories that will be used in the scripts are well-written based on your local machine.
4. Run the Python scripts in the following order:
    - `from_excel_to_transformed_dataframes.py` To make various transformations into the data
    - `unifying data.py` To unify data from different raw excel files
    - `database_upload_files.py`  To upload files to a SQLServer database

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
