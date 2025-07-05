import psycopg2
from config.db_config import DB_PARAMS

def load_to_postgresql(df, table_name):
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        columns = ', '.join(row.index)
        placeholders = ', '.join(['%s'] * len(row))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

# this is new concept
# ye padhna hai