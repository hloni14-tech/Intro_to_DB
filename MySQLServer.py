def create_database(host: str, user: str, password: str, db_name: str = "alx_book_store"):
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(host=host, user=user, password=password)
        cursor = cnx.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
        print(f"Database '{db_name}' created successfully!")
    except Error as e:
        print(f"Error connecting to the database server: {e}")
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if cnx is not None and cnx.is_connected():
            try:
                cnx.close()
            except Exception:
                pass

    if __name__ == "__main__":
       main()