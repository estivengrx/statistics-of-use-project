import pandas as pd
from os import listdir, path, remove

def device_unlocks_concatenation(data_directory: str) -> pd.DataFrame:
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
    device_files = [file for file in file_list if 'device' in file]  # Device unlocks data

    merged_df = pd.DataFrame()  # Empty dataframe

    # Iterate over the device files and merge them on the 'date' column
    for file in device_files:
        file_path = path.join(data_directory, file)
        df = pd.read_csv(file_path, sep=';', parse_dates=['date'])

        merged_df = pd.concat([merged_df, df[['date', 'Device Unlocks']]], axis=0)
    
    merged_df.to_csv(f'{data_directory}device_unlocks.csv', index=False)

    for device_file in device_files:
        remove(f'{data_directory}{device_file}')

if __name__ == "__main__":
    data_directory = 'D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/processed/'
    device_unlocks_concatenation(data_directory)