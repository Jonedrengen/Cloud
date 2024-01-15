import mysql.connector
from mysql.connector import errorcode

#db connection imports
import mysql.connector
from mysql.connector import errorcode

#db connection string
config = {'host' : 'cloud-main.mysql.database.azure.com', 
          'database' : 'cloud_main', 
          'user' : 'cloud', 
          'password' : 'Fedsvin12'}


#execute query function
def execute_query(sql_query):
    result = None
    try:
        print("Making connection")
        # using ** to unpack the config dict in the connect() function. This basically means that each key-value pair are inserted as an argument (so 4 arguments in this case). 
        # so host, database, user and password becomes arguments, with their respected values inside
        connection = mysql.connector.connect(**config)
        print("connection succesfull")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("something wrong with username or pass")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("db does not exist (or something else is wrong with the db maybe)")
        else:
            print("connection NOT made :(", err)
    else:
        # if the connection is successfull and no exceptions raised, execute the following
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql_query)
        print("query executed")
        if sql_query.startswith("SELECT"):
            result = cursor.fetchone()
            print("fetching one SELECT value:", result)
        else:
            connection.commit()
            print("commiting changes, since no SELECT command")
        cursor.close()
        connection.commit()
    return result

def delete_sim(InstanceState):
    if InstanceState == 1:

        pass

def Check_Instance():
    Instance_check_query = f"SELECT GraphID FROM cloud_main.activeinstance"
    result = execute_query(Instance_check_query)
    final_result = result[0]
    return final_result


result = Check_Instance()
print(result)