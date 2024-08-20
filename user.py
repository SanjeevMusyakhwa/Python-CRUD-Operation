#curd operation
import sqlite3
def create_connection (): #function for creating user
    try: #error ayo vane handle garna ko lagi
        conn = sqlite3.connect("users.sqlite3") #db sanga connect garna yedi xaena vane chai create garxa
        return conn
    except Exception as e:
        print(f"Error: {e}") # error lai handle garxa
        #options haru
INPUT_STRING = """ 
Enter the option:
    1. Create Table
    2. Dump users from CSV into users table
    3. Add New Users Into Users Table
    4. Query All Users From Table
    5. Query Users By id Form Table
    6. Query Specified No Of Records From Table
    7. Delete All Users
    8. Delete User by id
    9. Update User
    10. Press Any Key To Exit
"""

def create_table(conn): #table create garna lai 
    CREATE_USERS_TABLE_QUERY ="""
       CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,
            company_name CHAR(255) NOT NULL,
            address CHAR(255) NOT NULL,
            city CHAR(255) NOT NULL,
            county CHAR(255) NOT NULL,
            state CHAR(255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR(255) NOT NULL,
            phone2 CHAR(255),
            email CHAR(255) NOT NULL,
            web text
        );
    """
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE_QUERY) #exeute the query
    print("User's Table Created Sucessfully")


import csv
def read_csv(): #csv file lai read gareko
    users = [] #null List
    with open("sample_users.csv","r") as f: #Sample_users.csv file lai read gareko
        data = csv.reader(f) #Data ma rakheko csv.reader lai
        for user in data:
            users.append(tuple(user))
    # print(users)
    return users[1:]

#list vitra  ma data store gareko

COLUMNS =(
    "first_name",
    "last_name",
    "company_name",
    "address",
    "city",
    "county",
    "state",
    "zip",
    "phone1",
    "phone2",
    "email",
    "web"
)

def insert_users(conn, users):
    user_add_query = """
        INSERT INTO users
        (
       first_name,last_name,company_name,address,city,county,state,zip,phone1,phone2,email,web
        )
        values(?,?,?,?,?,?,?,?,?,?,?,?);
        """
    cur = conn.cursor()
    cur.executemany(user_add_query,users)
    conn.commit()       
    print(f"{len(users)} users were imported sucessfully")

def select_users(conn,no_of_users = 0): #conncection auxa

    print("...................")
    cur = conn.cursor()
    if no_of_users:
        users = cur.execute("SELECT * FROM users LIMIT ?",(no_of_users,))
    else:
        users =  cur.execute("SELECT * FROM users")
    for user in users:
        print(user)

def select_users_by_id(conn,user_id):
    cur = conn.cursor()
    users= cur.execute("SELECT * FROM users WHERE id = ?;",(user_id,))
    for user in users:
        print(user)
def delete_users(conn):
    cur = conn.cursor()
    users = cur.execute("DELETE FROM users;")
    conn.commit()
    print("All the users were deleted sucessfully")

def delete_users_by_id(conn,user_id):
    cur = conn.cursor()
    users = cur.execute("DELETE FROM users WHERE id = ?;",(user_id))
    conn.commit()
    print(f"User with id {user_id} has been deleted sucessfully")

def update_user_by_id(conn,user_id,column_name,column_value):
    UPDATE_QUERY =  f"UPDATE users set{column_name} = ? where id = ?;"
    cur = conn.cursor()
    cur.execute(UPDATE_QUERY,(column_value,user_id))
    conn.commit()
    print(f"[{column_name}] was updated with value [{column_value}] of user with id[{user_id}]"
    )

def main(): #yaha bata chai main code suru hunxa
    conn = create_connection() #connection lai create gareko
    user_input = input(INPUT_STRING) #user sanga input mageko
    if user_input == '1': 
        create_table(conn)
    elif user_input == '2':
        users = read_csv()
        insert_users(conn,users)
    elif user_input =='3':
        data =[]
        for column in COLUMNS:
            column_value = input(f"Enter the value of {column}: ")
            data.append(column_value)
        insert_users(conn,[tuple(data)])
    elif user_input == '4':
        select_users(conn)
    elif user_input == '5':
        user_id = input("Enter the user id " )
        if (user_id.isnumeric()):
            select_users_by_id(conn,user_id)
    elif user_input =='6':
        no_of_users = input("Enter the no of users")
        if(no_of_users.isnumeric() and int(no_of_users) > 0):
            select_users(conn,no_of_users=int(no_of_users))
    elif user_input == '7':
        confirm = input("Are you Sure you want to delete all the users")
        if confirm == 'y':
            delete_users(conn)
        else:
            print("Deletion cancelled")
    elif user_input == '8':
        user_id = input("Enter the user id you want to delete")
        if user_id.isnumeric() and int(id)> 0:
            delete_users_by_id(conn,user_id =  int(user_id))

    elif user_input =='9':
        user_id = input("enter the user_id")
        if user_id.isnumeric():
            column_name = input(f"Enter the id You want to edit. Please make sure is with in {COLUMNS}: ")
            if column_name in COLUMNS:
                column_value = input(f"Enter the value of {column_name,column_value}")
                update_user_by_id(conn,user_id,column_name,column_value)
    else:
        exit()
        
main()




