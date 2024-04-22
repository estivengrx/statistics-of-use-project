import pandas as pd

def export_problem_solution(file_path: str, output_path: str, problem_column: str, problem_2_column: str):
    """
    This function reads an Excel file, filters the input DataFrame based on certain conditions for each sheet,
    and exports the filtered DataFrame to a new Excel file, this was made to solve the change in exporting data
    from StayFree app.

    Parameters:
    file_path (str): The path of the input Excel file.
    output_path (str): The path where the output Excel file should be saved.
    problem_column (str): The name of the first column to search and filter.
    problem_2_column (str): The name of the second column to search and filter.

    Returns:
    Exports the data into an excel file.
    """
    # Create an ExcelWriter object to write to multiple sheets in the same Excel file
    with pd.ExcelWriter(output_path) as writer:
        # Iterate over the sheets in the input Excel file
        for sheet in ['Usage Count', 'Usage Time', 'Device Unlocks']:

            if sheet != 'Device Unlocks':
                # Reading the current sheet into a DataFrame
                data = pd.read_excel(file_path, sheet_name=sheet)
                
                # Creating a boolean mask that is True for each row that meets all of the following conditions:
                # - The index is not a float
                # - The value in the problem column is a string and its first character is uppercase
                # - The value in the solution column is 'motorola moto g(6) plus'
                mask = (pd.Series(data.index).map(lambda x: not isinstance(x, float)) &
                        data[problem_column].map(lambda x: isinstance(x, str) and x[0].isupper()) &
                        (data[problem_2_column] == 'motorola moto g(6) plus'))

                # Apply the mask to the DataFrame to get a new DataFrame that only includes the rows that meet the conditions
                data_mask = data.loc[mask].reset_index(drop=True)
                data_mask.to_excel(writer, sheet_name=f'App - {sheet}', index=False)

                # Apply the inverse of the mask to the DataFrame to get a new DataFrame that only includes the rows that do not meet the conditions
                data_not_mask = data.loc[~mask].reset_index(drop=True)
                data_not_mask.to_excel(writer, sheet_name=f'Web - {sheet}', index=False)
            else:
            # Adding the sheet 'Device Unlocks' to the final data
                data = pd.read_excel(file_path, sheet_name=sheet)
                data.to_excel(writer, sheet_name=sheet, index=False)


if __name__ == "__main__":
    # Paths of the input and output Excel files
    file_path = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/tests/fourth_data_april_22_2024.xls"
    output_path = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/tests/filtered_usage_data.xlsx"
    # Define the names of the problem and solution columns
    problem_column = 'Unnamed: 0'
    problem_2_column = 'Device'

    # Call the function with the defined parameters
    export_problem_solution(file_path, output_path, problem_column, problem_2_column)