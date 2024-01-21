# Statistics of Use Project

This project aims to analyze usage statistics from various devices collected through StayFree application. The data is initially in Excel format and is processed and transformed into CSV files for further analysis.

## Project Structure

The project consists of several Python scripts that perform different tasks:

- `from_excel_to_transformed_dataframes.py`: This script reads Excel files from the `data/raw` directory, transforms the data into a more usable format, and saves the transformed data as CSV files in the `data/processed` directory.

- `device_unlocks_unification.py`: This script unifies device unlock data from different sources.

- `data_unification_from_different_dates.py`: This script unifies data from different dates.

- `fill_missing_dates.py`: This script fills missing dates in the data with the mean of the respective column.

## How to Run

1. Clone this repository.
2. Navigate to the project directory.
3. Run the Python scripts in the following order:
    - `from_excel_to_transformed_dataframes.py` To make various transformations into the data
    - `unifying data.py` To unify data from different raw excel files
    - `database_upload_files.py`  To upload files to a SQLServer database

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
