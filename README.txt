Tim Xia
101222137
COMP 3005`


There should be 3 files in this submission:

    1. crud.py              the source code for the submission, and where the functions are stored.

    2. studentDb.sql        a copy of the queries required to create and update the data base initially, should you need it.

    3. README.txt           what you are reading right now


VIDEO LINK: "https://youtu.be/vlhU9ginJkk"

EXECUTION INSTRUCTIONS (Should you choose to, though the video and code should be adequate):

    Note that running the actual code is not a requirement for marking. This is confirmed by the discussion post    
    titled "A3 Q1 – Getting the PostgreSQL password and port number from user" from the Q&A discussion board that can 
    be found here: "https://brightspace.carleton.ca/d2l/le/content/264064/viewContent/3563281/View" (ctrl+f to find it)

    But if you need to test anything, instructions are below this paragrpah. Note that you may have to change some of 
    the code IF you choose to run this as the password of your accounts may not be the same. This was the topic mentioned 
    by the professor in the discussion post mentioned above.

    1. Open postgresql and create a new database called Assignment3Q1.

    2. Ensure that the database has the following properties, or change the code starting in the try block around line 78.
        hostname = 'localhost'
        database = 'Assignment3Q1' 
        username = 'postgres'
        pwd = 'postgres'
        port_id = 5433

    3. Install psycopg2:
    - Linux/Windows: pip install psycopg2 

    4. Assuming you have python installed, run with "python crud.py".


ADDITIONAL NOTES:

1. The majority of documentation I used to learn psycopg are the following:
    - General Information: https://wiki.postgresql.org/wiki/Main_Page
    - Learning how to create tables: https://www.postgresqltutorial.com/postgresql-python/create-tables/
    - Learning how to use execute to change data: https://www.psycopg.org/docs/usage.html 

    That, and the knowledge I have from querying in SQL from the lectures and assignments.

    And of course, Python from COMP 1405.