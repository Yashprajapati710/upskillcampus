import sqlite3

DB_NAME = "students.db"


def add_student(name, age, course, email, phone):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students(name,age,course,email,phone) VALUES(?,?,?,?,?)",
        (name, age, course, email, phone)
    )

    conn.commit()
    conn.close()


def view_students():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    conn.close()
    return rows


def search_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE id=?", (student_id,))
    row = cur.fetchone()

    conn.close()
    return row


def update_student(student_id, name, age, course, email, phone):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    UPDATE students
    SET name=?, age=?, course=?, email=?, phone=?
    WHERE id=?
    """, (name, age, course, email, phone, student_id))

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()