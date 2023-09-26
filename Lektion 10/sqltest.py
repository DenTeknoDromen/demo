import mysql.connector

# Skapar en koppling mellan sql databasen och koden
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="person"
)
mycursor = mydb.cursor()


def new_table():
    name = input("Enter name of new table: ")
    mycursor.execute(f"CREATE TABLE {name} "
                     "(id INT AUTO_INCREMENT PRIMARY KEY)")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)


def del_table():
    name = input("Enter name of table to delete: ")
    mycursor.execute(f"DROP TABLE {name}")


def new_column():
    name = input("Enter name of new column: ")
    mycursor.execute("ALTER TABLE persons \n"
                     f"ADD {name} VARCHAR(100)")
    mycursor.execute("SHOW COLUMNS FROM persons")


def new_row():
    indata = input("Enter name: ")
    mycursor.execute(f"INSERT INTO persons (name) VALUES ('{indata}')")
    print(f"Row added {indata}")


def show_all():
    mycursor.execute("SELECT * FROM persons")
    results = mycursor.fetchall()
    for x in results:
        print(x)


def update_row():
    curr_row = input("Enter row to update: ")
    updateto = input("Enter new name: ")
    mycursor.execute(f"UPDATE persons SET surname='{updateto}' "
                     f"WHERE name='{curr_row}'")


def temp():
    indata = input("Enter: ")
    mycursor.execute(f"SELECT {indata} FROM persons")
    results = mycursor.fetchall()
    for x in results:
        print(x)


def commit():
    mydb.commit()
    print("Changes commited")


def delete():
    indata = input("Enter number to delete: ")
    mycursor.execute(f"DELETE FROM persons WHERE id={indata}")


while True:
    indata = input("> ")
    if indata == "new_table":
        new_table()
    elif indata == "del_table":
        del_table()
    elif indata == "new_column":
        new_column()
    elif indata == "new_row":
        new_row()
    elif indata == "show_all":
        show_all()
    elif indata == "update_row":
        update_row()
    elif indata == "delete":
        delete()
    elif indata == "commit":
        commit()
    elif indata == "temp":
        temp()
    elif indata == "exit":
        break

mycursor.close()
mydb.close()
