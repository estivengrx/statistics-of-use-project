import pandas as pd
from os import listdir, remove, path

def read_excel_sheets(file_path: str) -> dict:
    """
    Read different sheets of an Excel file into separate dataframes and apply specific transformations.

    Parameters:
        file_path (str): The path to the Excel file.

    Returns:
        dict: A dictionary containing the transformed dataframes for each sheet.
    """
    
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    # Create a dictionary to store the dataframes for each sheet
    dataframes_dict = {}
    
    # Read each sheet and store it in the dictionary
    for sheet_name in sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name).rename({'Unnamed: 0': ''}, axis=1)
        dataframes_dict[sheet_name] = df

    # Get a list of sheet names from the dictionary
    sheet_names_list = list(dataframes_dict.keys())  
    
    transformed_dataframes = {}

    # Process each sheet
    for sheet_name in sheet_names_list:
        dataframe = dataframes_dict[sheet_name]

        if 'Web' in sheet_name:
            # Drop the 'Total Usage' column and remove the last 4 rows
            dataframe = dataframe.drop(columns=['Total Usage'])
            dataframe = dataframe.iloc[:-4]
            
            grouped_data = dataframe.groupby('Device')

            # Transformation of every dataframe in the groupby
            for device, group in grouped_data:
                # Transpose the dataframe and set the first row as column headers
                group = group.T
                group.columns = group.iloc[0]

                # Eliminate duplicated columns in the dataframe
                group = group.loc[:, ~group.columns.duplicated()]

                # Drop the first row since it is now the header
                group = group[1:].reset_index().rename({'index': 'date'}, axis=1)
                group = group.iloc[1:]

                if 'Time' in sheet_name:
                    # Time transformation to minutes (code made in main_notebook_data_transformation notebook)
                    for col in group.columns:
                        if col != 'date':
                            group[col] = round(pd.to_timedelta(group[col]).dt.total_seconds() / 60, 2)
                        else:
                            pass

                # Format the sheet name and device name for the transformed dataframe's key
                sheet_name_appropriate = sheet_name.lower() \
                                                  .replace('-', '') \
                                                  .replace('  ', ' ') \
                                                  .replace(' ', '_')
                
                device_name_appropriate = device.split(' ')[-1]
                # Store the transformed dataframe in the final dictionary
                transformed_dataframes[f'{sheet_name_appropriate}_{device_name_appropriate}'] = group
                        
        # For sheets containing 'App' or 'Device', perform different transformations
        elif ('App' in sheet_name) or ('Device' in sheet_name):
            if 'Device' in dataframe.columns:
                # If 'Device' column exists, drop both 'Total Usage' and 'Device'
                dataframe = dataframe.drop(columns=['Total Usage', 'Device'])
            else:
                # If 'Device' column does not exist, only drop 'Total Usage'
                dataframe = dataframe.drop(columns=['Total Usage'])

            dataframe = dataframe.iloc[:-4].T
            dataframe.columns = dataframe.iloc[0]

            dataframe = dataframe.loc[:, ~dataframe.columns.duplicated()]

            dataframe = dataframe[1:].reset_index().rename({'index': 'date'}, axis=1)

            # Time transformation to minutes, only for time data, not count data
            if 'Time' in sheet_name:
                
                for col in dataframe.columns:
                    if col != 'date':
                        dataframe[col] = round(pd.to_timedelta(dataframe[col]).dt.total_seconds() / 60, 2)
                    else:
                        pass

            sheet_name_appropriate = sheet_name.lower() \
                                              .replace('-', '') \
                                              .replace('  ', ' ') \
                                              .replace(' ', '_')
            transformed_dataframes[sheet_name_appropriate + '_motorola'] = dataframe

    # Format the sheet names for the transformed dataframe's key
    final_data = {key.lower().replace('plus', 'motorola').replace('extension', 'edge'): value for key, value in transformed_dataframes.items()}
    return final_data

def transform_dataframe(dataframe: pd.DataFrame, values_greater_than: int) -> pd.DataFrame:
    """
    Filter and transform a pandas DataFrame based on the sum of values in each column.

    Parameters:
        dataframe (pd.DataFrame): The input DataFrame to be processed.
        values_greater_than (int): The minimum sum value required for a column to be included in the transformed DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame containing only the 'date' column and the columns whose sum of values is greater than or equal to 'values_greater_than'.
    """
    
    data_copy = dataframe.copy()

    # Packing the name of columns and sums in a dictionary to use in further codes
    dictionary_sums = {}
    for column in data_copy:
        if (column != 'date') and \
           (sum(data_copy[column]) >= values_greater_than):
            
            dictionary_sums[column] = sum(data_copy[column])

    names_of_columns_to_stay = [column_name for column_name in dictionary_sums.keys()]
    names_of_columns_to_stay.insert(0, 'date')

    # Filtering dataframe
    transformed_dataframe = data_copy[names_of_columns_to_stay]
    
    return transformed_dataframe

if __name__ == "__main__":

    # Replace the file_path with the actual path to the Excel file
    raw_files_path = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/raw/"
    processed_files_path = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/processed/"

    for raw_file in listdir(raw_files_path):
        if raw_file.endswith('.xls') or raw_file.endswith('.xlsx'):
            full_path = path.join(raw_files_path, raw_file)
            file_keyword = full_path.split('/')[-1].split('.')[0].split('_')[0]
            folder_name = f'{full_path.split("/")[-1].split(".")[0]}' + '_'
            transformed = read_excel_sheets(full_path)

            # Save the dataframes into csv files
            for key, values in transformed.items():
                output_file = (
                    f'{processed_files_path}{folder_name}{file_keyword}_{key}.csv'
                    if 'device' in key
                    else f'{processed_files_path}{file_keyword}_{key}.csv'
                )
                values.to_csv(output_file, index=None, sep=';')

            # Transformations in the datasets
            dir_list = listdir(processed_files_path)

            for file in dir_list:
                if 'device' not in file and 'git' not in file and file_keyword in file:
                    file_path = f'{processed_files_path}{file}'
                    data = pd.read_csv(file_path, delimiter=';', parse_dates=['date'])
                    data_transformed = transform_dataframe(data, 100)
                    data_transformed = data_transformed.set_index('date')
                    data_transformed.sort_values(by='date', ascending=True, inplace=True)
                    data_transformed = data_transformed.drop_duplicates()
                    data_transformed = data_transformed.reset_index()
                    data_transformed['total_usage'] = data_transformed.sum(axis=1, numeric_only=True)

                    # Saving the files as desired
                    export_path = f'{processed_files_path}{folder_name}{file}'
                    data_transformed.to_csv(
                        export_path, sep=';', index=False, date_format='%Y-%m-%d'
                    )
                    remove(file_path)
