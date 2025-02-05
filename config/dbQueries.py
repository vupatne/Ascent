from mysql.connector import pooling

connection_pool = pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                      pool_size=5,
                                                      pool_reset_session=True,
                                                      host='localhost',
                                                      database='ascent',
                                                      user='root',
                                                      password='flat601')


def selectqueryfunc(select_query, select_tuple):
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        mycursor = connection_object.cursor(prepared=True)
        mycursor.execute(select_query,select_tuple)
        result = mycursor.fetchall()
        mycursor.close()
        connection_object.close()
        return result

def insertqueryfunc(insert_query, insert_tuple):
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        mycursor = connection_object.cursor(prepared=True)
        mycursor.execute(insert_query,insert_tuple)
        connection_object.commit()
        mycursor.close()
        connection_object.close()

def deletequeryfunc(delete_query, delete_tuple):
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        mycursor = connection_object.cursor(prepared=True)
        mycursor.execute(delete_query,delete_tuple)
        connection_object.commit()
        mycursor.close()
        connection_object.close()
