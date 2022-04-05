import sqlite3

def write_to_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)
    print("Данные сохранены")

def read_blob_data(emp_id):
    try:
        sqlite_connection = sqlite3.connect('informatics.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к БД")

        sql_fetch_blob_query = """SELECT * from informatics where id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0])
            photo = row[1]
            return photo

        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")