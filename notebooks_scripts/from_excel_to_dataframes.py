import pandas as pd

def read_excel_sheets(file_path):
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
                duplicated_columns = group.columns[group.columns.duplicated()]
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

            duplicated_columns = dataframe.columns[dataframe.columns.duplicated()]
            dataframe = dataframe.loc[:, ~dataframe.columns.duplicated()]

            dataframe = dataframe[1:].reset_index().rename({'index': 'date'}, axis=1)

            # Time transformation to minutes, only for time data, not count data
            if 'App' in sheet_name:
                
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
    final_data = {key.lower().replace('plus', 'motorola'): value for key, value in transformed_dataframes.items()}
    return final_data

if __name__ == "__main__":
    # Replace the file_path with the actual path to your Excel file
    excel_file_path = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/raw/StayFree Export - Total Usage - 6_24_23 (1).xls"
    transformed = read_excel_sheets(excel_file_path)

    # Save the dataframes into csv files
    path_final_files = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/processed/"
    for key, values in transformed.items():
        values.to_csv(path_final_files + key + '.csv', index=None)