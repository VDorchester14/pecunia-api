'''
Basically this is the code I am going to use to initialize the database
and make changes to the tables and structure.

'''
import sqlite3

def connect_sqlite():
    #secure a connection
    connection = sqlite3.connect('datab.db')
    c = connection.cursor()
    return connection, c

#takes a table name and a 2d table of attributes and types
def add_table_sqlite(c, table_name, attributes):
    #create the query string
    attribute_string = ""
    for index, att in enumerate(attributes):
        attribute_string+= (str(att[0])+" "+str(att[1])+", ")
    attribute_string = attribute_string[:2]+str(")")#ending the query
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS {0}
                (attribute_string)'''.format(table_name))

#add some values to the table
def add_value_to_table_sqlite(c):
    #add in my data
    c.execute("INSERT INTO users VALUES ('vail.dorchester@colorado.edu','password')")
    c.commit()

#close connection
def close_connection_sqlite(connection):
    connection.close()

#the main method
def main():
    connection, cursor = connect_sqlite()
    add_table_sqlite(cursor, "users", [["email", "text"],["password","text"]])
    return

#__main__
if __name__ == "__main__":
    main()
