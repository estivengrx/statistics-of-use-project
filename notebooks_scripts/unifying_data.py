import pandas as pd
from os import listdir, path, remove
from functools import reduce

def device_unlocks_unification(data_directory: str):
    """
    Concatenates device unlock data from multiple files in the specified directory.

    Parameters:
    - data_directory (str): The path to the directory containing device unlock data files.

    Returns:
    - pd.DataFrame: A DataFrame containing the concatenated device unlock data.

    This function reads all files in the specified directory that contain the keyword
    'device' in their filenames. It then merges these files based on the 'date' column,
    creating a consolidated DataFrame. The resulting DataFrame is saved to a CSV file
    named 'device_unlocks.csv' in the same directory.
    """

    file_list = listdir(data_directory) 
    device_files = [file for file in file_list if 'device' in file] # Files filter

    merged_df = pd.DataFrame()

    # Iterate over the device files and merge them on the 'date' column
    for file in device_files:
        file_path = path.join(data_directory, file)
        df = pd.read_csv(file_path, sep=';', parse_dates=['date'])

        # Concatenate the current DataFrame to the merged DataFrame
        merged_df = pd.concat([merged_df, df[['date', 'Device Unlocks']]], axis=0)
    
    # Save the consolidated DataFrame to a CSV file
    output_filepath = f'{data_directory}device_unlocks_motorola.csv'
    merged_df.to_csv(output_filepath, index=False, sep=';')

    # Remove the original device files
    for device_file in device_files:
        remove(path.join(data_directory, device_file))

def data_unification_from_different_dates(data_directory: str):
    """
    Unify data files with different dates based on specified keywords.

    Parameters:
    - data_directory (str): The directory containing the data files.

    The function reads data files from the specified directory, identifies relevant keywords,
    and merges the files with the same keyword into a unified DataFrame. It then saves the
    unified DataFrame to a new CSV file and removes the original files.

    Note: This function assumes that the files are in CSV format and use ';' as the separator.
    """
    file_list = [file for file in listdir(data_directory) if 'device' not in file]

    keywords = [
        'app_usage_count_motorola', 'app_usage_time_motorola', 
        'web_usage_count_chrome', 'web_usage_time_chrome',
        'web_usage_count_edge', 'web_usage_time_edge',
        'web_usage_count_motorola', 'web_usage_time_motorola'
    ]

    # Process files for each keyword
    for keyword in keywords:
        # Select files that contain the current keyword
        files_with_keyword_list = [
            pd.read_csv(f'{data_directory}{filter_file}', sep=';') for filter_file in file_list if keyword in filter_file
        ]

        # Merge selected files into a unified DataFrame and fill NaN values with 0
        final_dataframe_unified = reduce(lambda left, right: pd.merge(left, right, how='outer'), files_with_keyword_list).fillna(0)

        # Save the unified DataFrame to a new CSV file
        output_filepath = f'D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/processed/{keyword}.csv'
        final_dataframe_unified.to_csv(output_filepath, index=False, sep=';')

        # Remove files with the current keyword from the original file list
        files_to_remove = [x for x in file_list if keyword in x]   
        for not_unified_file in files_to_remove:
            remove(f'{data_directory}{not_unified_file}')

def fill_missing_dates(data_directory: str):
    """
    Fills missing dates in CSV files in the specified directory.

    Parameters:
    - data_directory (str): The path to the directory containing the CSV files.

    This function reads each CSV file in the specified directory into a DataFrame,
    checks for missing dates in the 'date' column, and if a date is missing, adds a new
    row with that date and sets all other columns to zero. The DataFrame is then saved
    back to the CSV file.
    """

    file_list = [file for file in listdir(data_directory) if file.endswith('.csv')]

    for file in file_list:
        file_path = path.join(data_directory, file)
        df = pd.read_csv(file_path, sep=';', parse_dates=['date'])

        df.set_index('date', inplace=True)
        df = df.resample('D').asfreq()

        if 'device' in file:
            df.replace({0: float('NaN')}, inplace=True)

        df = df.fillna(method='ffill')  # forward fill to fill based on previous data

        df.reset_index(inplace=True)
        df.to_csv(file_path, index=False, sep=';')

if __name__ == "__main__":
    data_directory = 'D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/processed/'
    data_unification_from_different_dates(data_directory)
    device_unlocks_unification(data_directory)
    fill_missing_dates(data_directory)