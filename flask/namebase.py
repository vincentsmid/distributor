import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        # connect to a SQLite database. If database does not exist, it is created
        conn = sqlite3.connect('user_data.db')
    except Error as e:
        print(e)
        
    if conn:
        return conn

def close_connection(conne):
    conn = create_connection()

    conn.close()

def create_table(conn):
    try:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS User (
                name text, 
                username text, 
                email text, 
                company text
            )
        """)
        conn.commit()
        print("Table created successfully")

    except Error as e:
        print(e)

def add_user(name, username, email, company):
    conne = create_connection()

    try:
        c = conne.cursor()
        c.execute("""
            INSERT INTO User 
            VALUES (?,?,?,?)
        """, (name, username, email, company))
        conne.commit()
        print(f"User {name} added successfully")

    except Error as e:
        print(e)

def get_all_users():
    conne = create_connection()
    
    try:
        c = conne.cursor()
        c.execute("SELECT * FROM User")
        rows = c.fetchall()
        close_connection(conne)
        
        return rows

    except Error as e:
        print(e)
        return {'error': str(e)}

def main():
    # Creating a connection
    conn = create_connection()

    # Creating table
    create_table(conn)

    print("All users:")
    get_all_users()

    # Closing connection
    close_connection(conn)


if __name__ == "__main__":
    main()
