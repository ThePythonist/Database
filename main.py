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


# create_table(input("Enter table name : "), input("Enter number of table fields : "))
# cur.execute("CREATE TABLE  (id INT, name VARCHAR(50), job VARCHAR(50), age INT);")
# cur.execute("INSERT INTO customers VALUES (1102,'Ava','Female',20);")

# cur.execute("SELECT * FROM customers;")
# records = cur.fetchall()
# print(records)

# con.commit()
# con.close()
# print('Done')

while True:
    entry = input("Action : ").casefold()
    if entry == "create":
        create_table(input("Enter table name : "), input("Enter number of table fields : "))
        break
    else:
        cur.execute("SELECT * FROM movies;")
        records = cur.fetchall()
        print(records)
