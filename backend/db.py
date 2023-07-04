import pandas as pd
from sqlalchemy import create_engine

def access_db(query):

    conn_azure = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:autism-db.database.windows.net,1433;Database=autism-db;Uid=thedarklord100;Pwd=vijayant@SQL1;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=SqlPassword"
    conn_azure = "mssql+pyodbc:///?odbc_connect=" + conn_azure

    engine = create_engine(conn_azure)
    conn = engine.connect()

    df = pd.read_sql(query, conn)
    
    conn.close()
    engine.dispose()

    return df