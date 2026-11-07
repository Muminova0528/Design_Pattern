from db_connection import DBConnection

connection1 = DBConnection()
connection2 = DBConnection()
connection3 = DBConnection()

print(connection1.get_session())
print(connection2.get_session())
print(connection3.get_session())

print(connection1 is connection2 is connection3)