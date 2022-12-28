import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()


def create_table(table_name, fields):
    columns = []

    for i in range(int(fields)):
        columns.append(input("Column : "))

    command = "CREATE TABLE {} {};".format(table_name, tuple(columns))

    cur.execute(command)

    con.commit()
    con.close()

    print("Done")


def select_from(table_name):
    try:
        entry = input("Do you need any filter (yes/no) ? : ")
        if entry == "yes":
            column = input("Column : ")
            condition = input("Condition : ")

            command = f"SELECT * FROM {table_name} WHERE {column} {condition} ;"
            cur.execute(command)
            records = cur.fetchall()
            print(records)

        elif entry == "no":
            command = f"SELECT * FROM {table_name};"
            cur.execute(command)
            records = cur.fetchall()
            print(records)
        else:
            print("Invalid input. Try again")
            select_from(input("Enter table name : "))
    except sqlite3.OperationalError as error:
        if "no such table" in error:
            print("Table not found. Try again:")


while True:
    action = input("Action ( create / select / insert ) : ").casefold()
    if action == "create":
        create_table(input("Enter table name : "), input("Enter number of table fields : "))
        break
    elif action == "select":
        select_from(input("Enter table name : "))
        break
    elif action == "insert":
        cur.execute("PRAGMA table_info(movies);")
        records = cur.fetchall()
        print(len(records))
        break
    else:
        print("Invalid input. Try again")
   
