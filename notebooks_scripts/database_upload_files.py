import os
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.types import Date

def upload_csv_to_sql_server(csv_folder_path, database_name, server_name, username, password):
    # Create the connection string for SQL Server
    connection_string = f"mssql+pyodbc://{username}:{password}@{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server"

    engine = create_engine(connection_string, echo=True)

    # csv files in the directory
    csv_files = [file for file in os.listdir(csv_folder_path) if file.endswith(".csv")]

    for csv_file in csv_files:

        csv_path = os.path.join(csv_folder_path, csv_file)
        df = pd.read_csv(csv_path,
                         delimiter=';')

        df.columns = df.columns.str.replace(' ', '_')
        df.columns = df.columns.str.lower()

        # upload the DataFrame to the database
        table_name = os.path.splitext(csv_file)[0]
        df.to_sql(table_name, 
                  con=engine, 
                  if_exists='replace',
                  index=False,
                  dtype={'date': Date()}  # Set 'date' column as datetime dtype in the database
                  )
        
        print(f"Uploaded {csv_file} to {database_name}.{table_name}")

if __name__ == "__main__":
    csv_folder_path = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/data/processed"
    database_name = "statistics_of_use_db"
    server_name = "DESKTOP-8PK64UI"
    username = "main_estiven"

    password_file_path = "D:/Estiven/Datos/Proyectos/statistics-of-use-project/notebooks_scripts/database_pass.txt"
    with open(password_file_path, "r") as file:
        password = file.read().strip()

    upload_csv_to_sql_server(csv_folder_path, database_name, server_name, username, password)