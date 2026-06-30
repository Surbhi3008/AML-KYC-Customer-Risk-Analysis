import pandas as pd
from sqlalchemy import create_engine

# 1. Database Connection Settings
USER = "postgres"
PASSWORD = "1234"
HOST = "localhost"
PORT = "5432"
DATABASE_NAME = "Customerriskscore"

# 2. Establish connection to your PostgreSQL database
engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}")

# 3. Your SQL project query (using lowercase table and column names)
query = """
    SELECT * 
    FROM aml_customers 
    WHERE risk_category = 'High Risk';
"""

try:
    print(f"Connecting to database: {DATABASE_NAME} using Python...")
    
    # 4. Run query and dump to Excel
    df = pd.read_sql_query(query, con=engine)
    
    output_filename = "High_Risk_Compliance_Alerts.xlsx"
    df.to_excel(output_filename, index=False)
    
    print("\n" + "="*50)
    print(" SUCCESS! Python successfully extracted your pgAdmin data.")
    print(f" Pulled {len(df)} high-risk customer profiles.")
    print(f" File saved as: {output_filename}")
    print("="*50)

except Exception as e:
    print("\n" + "="*50)
    print(f" CONNECTION ERROR: {e}")
    print("="*50)
