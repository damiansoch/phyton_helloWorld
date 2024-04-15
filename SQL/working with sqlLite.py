import sqlite3

DB_NAME = "sqllite_db.db"

# 1 -> creates bd if absent

with sqlite3.connect(DB_NAME) as sqlite_conn:
    print(sqlite_conn)
    print(type(sqlite_conn))

# # 2 -> create table

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_req = """CREATE TABLE IF NOT EXISTS courses (
#                     id INTEGER PRIMARY KEY,
#                     title TEXT NOT NULL,
#                     students_qty INTEGER,
#                     reviews_qty INTEGER
#                 );"""
#     try:
#         sqlite_conn.execute(sql_req)
#     except Exception as e:
#         print(e)


# # 3 -> insert data

# data = [
#     {"id": 1, "title": "Introduction to Python", "students_qty": 100, "reviews_qty": 25},
#     {"id": 2, "title": "Advanced Python Programming", "students_qty": 80, "reviews_qty": 30},
#     {"id": 3, "title": "Data Science with Python", "students_qty": 120, "reviews_qty": 40},
#     {"id": 4, "title": "Machine Learning Basics", "students_qty": 150, "reviews_qty": 35},
#     {"id": 5, "title": "Deep Learning Fundamentals", "students_qty": 130, "reviews_qty": 45},
#     {"id": 6, "title": "Web Development with Flask", "students_qty": 90, "reviews_qty": 20},
#     {"id": 7, "title": "Database Design Principles", "students_qty": 70, "reviews_qty": 15},
#     {"id": 8, "title": "Front-End Essentials with React", "students_qty": 110, "reviews_qty": 50},
#     {"id": 9, "title": "Cloud Computing with AWS", "students_qty": 100, "reviews_qty": 30},
#     {"id": 10, "title": "Cybersecurity Basics", "students_qty": 60, "reviews_qty": 10}
# ]
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     insert_query = "INSERT INTO courses (id, title, students_qty, reviews_qty) VALUES (?, ?, ?, ?)"
#     try:
#         for course in data:
#             sqlite_conn.execute(insert_query,
#                                 (course['id'], course['title'], course['students_qty'], course['reviews_qty']))
#         print("Courses have been inserted successfully.")
#     except Exception as e:
#         print(e)


# # 4 -> read data
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     select_query = "SELECT * FROM courses"
#
#     # Execute the query
#     sql_cursor = sqlite_conn.execute(select_query)
#
#     courses_form_db = []
#
#     for record in sql_cursor:
#         # print(record)
#         course_id, title, students_qty, reviews_qty = record
#         course_dict = {
#             "id": course_id,
#             "title": title,
#             "students_qty": students_qty,
#             "reviews_qty": reviews_qty,
#         }
#         courses_form_db.append(course_dict)
#
#     for course in courses_form_db:
#         print(course)
