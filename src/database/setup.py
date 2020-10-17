import sys
import mysql.connector
import time

DB = None
DB_name = "db.users"
MAX_RETRIES = 40

TABLE_DESCRIPTION = (
    f"CREATE TABLE IF NOT EXISTS {DB_name} ("
    "  `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
    "  `name` varchar(50) not null,"
    "  `email` varchar(120) not null,"
    "  `password` varchar(120) not null,"
    "  `created_at` timestamp not null default now(),"
    "  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
    "  CONSTRAINT unique_user_email UNIQUE (email)"
    ") ENGINE=InnoDB")


def init_db():
    """
    Connect to MySql DB and create "posts" table
    :return:
    """
    mydb = mysql.connector.connect(
        host="mydb",
        port="3306",
        database="db",
        user="root",
        password="pp",
        auth_plugin='mysql_native_password'
    )

    cursor = mydb.cursor()

    try:
        print("Creating table posts:")
        cursor.execute(TABLE_DESCRIPTION)
        print("Table posts created successfully.")
    except mysql.connector.Error as err:
        print(err.msg)
        raise err

    return mydb


def db_startup():
    global DB
    loop_counter = 0
    while loop_counter < MAX_RETRIES:
        try:
            DB = init_db()
            return DB
        except mysql.connector.errors.InterfaceError:
            print(f"DB is not ready yet. #{loop_counter}")
            time.sleep(5)
            loop_counter += 1

    if loop_counter == MAX_RETRIES:
        raise Exception("FAILURE: DB Connection took too long")


def execute_command(command):
    print(f"executing: {command}", file=sys.stderr)
    cursor = DB.cursor()
    cursor.execute(command)
    return cursor


def execute_and_fetch(command):
    cursor = execute_command(command)
    results = cursor.fetchall()
    print(f"query 5 first results: {results[:5]}", file=sys.stderr)
    return results

