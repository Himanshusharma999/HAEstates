import psycopg2
import os

from dotenv import load_dotenv
from choices import df

load_dotenv()

if __name__ == '__main__':
    conn = psycopg2.connect(
        host="localhost",
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
    with conn.cursor() as cur:
        # Run users.sql
        with open('users.sql') as db_file:
            cur.execute(db_file.read())
        # Run realestate.sql
        with open('realestate.sql') as db_file:
            cur.execute(db_file.read())

        # Import all produce from the dataset
        all_realestate = list(
            map(lambda x: tuple(x),
                df[['text', 'beds', 'baths', 'type', 'garage', 'sqrf', 'listPrice', 'stories', 'year_built']].to_records(index=False))
        )

        # Replace null values with default values
        all_realestate = [(text or '', beds or 0, baths or 0, type or '', garage or 0, sqrf or 0, listPrice or 0, stories or 0, year_built or 0) 
                          for text, beds, baths, type, garage, sqrf, listPrice, stories, year_built in all_realestate]
        
        args_str = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", i).decode('utf-8') for i in all_realestate)
        cur.execute("INSERT INTO Property (text, beds, baths, type, garage, sqrf, listPrice, stories, year_built) VALUES " + args_str)
        
        # Dummy farmer 1 sells all produce
        # dummy_sales = [(1, i) for i in range(1, len(all_produce) + 1)]
        # args_str = ','.join(cur.mogrify("(%s, %s)", i).decode('utf-8') for i in dummy_sales)
        # cur.execute("INSERT INTO Sell (farmer_pk, produce_pk) VALUES " + args_str)

        conn.commit()

    conn.close()