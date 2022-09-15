import psycopg2
class DatabaseVerification():
    def __init__(self, alter_names):
        self.alter_names = alter_names

    def get_all_existing_table_names(self):
        conn = psycopg2.connect(
        host = 'x',
        database = 'postgres',
        user = 'postgres',
        password = 'JVictor@00'
        )
        cursor = conn.cursor()

        query = """SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema='public'
                    AND table_type='BASE TABLE';
                """
        cursor.execute(query)
        all_tables = cursor.fetchall()
        cursor.close()
        conn.commit()

        array_all_tables = []
        for table in all_tables:
            array_all_tables.append(table[0])
        
        for crypto in self.alter_names:
            if crypto not in array_all_tables:
                print(f"{crypto} not exists in Database. Creating table...")
                cursor = conn.cursor()
                script = f"""CREATE TABLE {crypto} (Date TIMESTAMP NOT NULL, Price FLOAT(32), MarketCap FLOAT(32), Volume FLOAT(32) );"""
                cursor.execute(script)
        cursor.close()
        conn.commit()

        

