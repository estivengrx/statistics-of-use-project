# Statistics of Use Project

This project aims to analyze usage statistics from various devices collected through StayFree application. The data is initially in Excel format and is processed and transformed into CSV files for further analysis.
The primary source of data stems from the StayFree application, capturing insights into user behaviors and interactions. The dataset is initially structured in Excel format and is subsequently processed and transformed into CSV files for streamlined analysis.

The data is from 10/19/2022 to 01/08/2024.

The inspiration for this project arises from the increasing need to comprehend and derive meaningful patterns from the vast array of my own device usage data. By delving into the statistics provided by StayFree, we aim to uncover valuable insights that can inform user habits, preferences, and the broader landscape of digital engagement.

## Project Structure

- [`data/`](command:_github.copilot.openRelativePath?%5B%22data%2F%22%5D "data/"): Contains raw data in Excel format and processed data in CSV format.
- [`notebooks_scripts/`](command:_github.copilot.openRelativePath?%5B%22notebooks_scripts%2F%22%5D "notebooks_scripts/"): Contains Python scripts and Jupyter notebooks for data transformation and unification.
- [`src/`](command:_github.copilot.openRelativePath?%5B%22src%2F%22%5D "src/"): Contains Python scripts for data processing and feature building.
- [`sql/`](command:_github.copilot.openRelativePath?%5B%22sql%2F%22%5D "sql/"): Contains SQL queries used in the project.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%22requirements.txt%22%5D "requirements.txt"): Lists the Python dependencies required for this project.

## Main Scripts and Notebooks

- [`from_excel_to_transformed_dataframes.py`](command:_github.copilot.openSymbolInFile?%5B%22notebooks_scripts%2Ffrom_excel_to_transformed_dataframes.py%22%2C%22from_excel_to_transformed_dataframes.py%22%5D "notebooks_scripts/from_excel_to_transformed_dataframes.py"): Transforms raw Excel data into processed dataframes.
- [`unifying_data.py`](command:_github.copilot.openSymbolInFile?%5B%22notebooks_scripts%2Funifying_data.py%22%2C%22unifying_data.py%22%5D "notebooks_scripts/unifying_data.py"): Unifies data from different dates.
- [`database_upload_files.py`](command:_github.copilot.openSymbolInFile?%5B%22notebooks_scripts%2Fdatabase_upload_files.py%22%2C%22database_upload_files.py%22%5D "notebooks_scripts/database_upload_files.py"): Handles uploading data to the database.
- [`data_transformation_tests.ipynb`](command:_github.copilot.openSymbolInFile?%5B%22notebooks_scripts%2Fdata_transformation_tests.ipynb%22%2C%22data_transformation_tests.ipynb%22%5D "notebooks_scripts/data_transformation_tests.ipynb"): Contains tests for data transformation.

## How to Run

1. Clone this repository.
2. Navigate to the project directory.
3. Run the Python scripts in the following order:
    - `from_excel_to_transformed_dataframes.py` To make various transformations into the data
    - `unifying data.py` To unify data from different raw excel files
    - `database_upload_files.py`  To upload files to a SQLServer database

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
