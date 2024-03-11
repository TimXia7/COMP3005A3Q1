import psycopg2

# Assignment Functions:
# Most information I needed for this was from the psycopg2 
# documentation, specifically: https://www.psycopg.org/docs/usage.html

def reCreateTable():
    cur.execute("""
        DROP TABLE IF EXISTS Students;
    
        CREATE TABLE IF NOT EXISTS Students (
            student_id			SERIAL		PRIMARY KEY,
            first_name			TEXT		NOT NULL,
            last_name			TEXT		NOT NULL,
            email				TEXT		UNIQUE NOT NULL,
            enrollment_date		DATE		
        );


        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
                
    """)

    conn.commit()


def getAllStudents():
    cur.execute("SELECT * FROM Students")
    tuples = cur.fetchall()

    # Hardcoded, just for formatting to make it more readable. These prints don't change the data printed!
    print()
    print("student_id, first_name, last_name, email, enrollment_date")

    for tuple in tuples:
        print(tuple)
    
    print()


def addStudent(first_name, last_name, email, enrollment_date):
    newStu = (first_name, last_name, email, enrollment_date)
    cur.execute("""
        INSERT INTO Students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
    """, newStu)

    conn.commit()


def updateStudentEmail(student_id, new_email):
    updateStu = (new_email, student_id)
    cur.execute("""
        UPDATE Students 
        SET email = %s
        WHERE student_id = %s
    """, updateStu)

    conn.commit()


def deleteStudent(student_id):

    deleteTarget = (student_id,)

    cur.execute("""
        DELETE FROM Students WHERE student_id = %s
    """, (deleteTarget))

    conn.commit()


# There's no main function, just global code so everything can be accessed across all functions with ease.
# Not the smartest solution for a larger system, but for an assignment, it should be just fine.
hostname = 'localhost'
database = 'Assignment3Q1' 
username = 'postgres'
pwd = 'postgres'
port_id = 5433

try:
    # holds a connection object to connect to the database
    conn = psycopg2.connect(    
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    # Cursor: allows the python code to execute PostgreSQL 
    # commands in a db session (facilliates connection)
    cur = conn.cursor()  

    # Re-create the table:
    reCreateTable()

    # Assignment function execution (with some additional formatting) begin here:

    print("\ngetAllStudents()    (Original Content):")
    getAllStudents()
    print()
    
    addStudent("This", "Guy", "someEmail@gmail.com", "2000-01-01")
    print("After adding the student with addStudent():")
    getAllStudents()
    print()

    updateStudentEmail(3, 'jimsEmail@gmail.com')
    print("After updating a student with updateStudentEmail:")
    getAllStudents()
    print("\n")


    deleteStudent(1)
    print("After deleting the student just added with addStudent():")
    getAllStudents()



except Exception as error:
    print(error)
finally: #To ensure that the connection object and cursor always close:
    # close the cursor
    cur.close()
    # close the connection, once we are finished with it.
    conn.close() 
