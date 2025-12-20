# import sqlite3
# def show_all_students():
#     with sqlite3.connect("test.db") as conn:
#         cursor = conn.cursor()
#         query = """SELECT * FROM  students
#         """
#         result = cursor.execute(query)
#         for item in result:
#             print(item)

# def insert_into_students(f_name, l_name, email):
#     with sqlite3.connect("test.db") as conn:
#         cursor = conn.cursor()
#         query = f"""
#                 INSERT  INTO students VALUES (?, ? , ?,?,?)
#                 """
#         try:
#             cursor.execute(query, (None, f_name, l_name, email, "2020-01-10"))
#             conn.commit()
#         except Exception as ex:
#             print(ex)
#         finally:
#             conn.close()
# insert_into_students("amir", "sabouri", "amirr@bl;alal")


import psycopg
try:

    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="soroush_babei",
        user="postgres",
        password="root"
    )
    cursor = conn.cursor()
    query = """INSERT INTO students VALUES (default, %s, %s, %s, %s)"""
    cursor.execute(query, ('sara', 'saraei', 'sara@bob.com', '2020-01-01'))
    conn.commit()
    # raw_data = cursor.execute("SELECT * FROM students")
    # data = raw_data.fetchall()
    # print(raw_data)
    # for datium in data:
    #     print(datium)
except Exception as ex:
    print(ex)