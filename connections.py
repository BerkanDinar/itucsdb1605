import psycopg2 as dbapi2

class Connections:
    def __init__(self, cp):
        self.cp = cp
        return

    def get_connectionlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = """SELECT connections.ConnectionId, connections.MainUserId, u1.FirstName, u1.LastName,
                  connections.FriendUserId, u2.FirstName, u2.LastName
                  FROM articles JOIN users  u1 ON connections.MainUserId = u1.UserId
                  JOIN users u2 ON connections.FriendUserId = u2.UserId
                  """
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        
    def get_userlist(self):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM users ORDER BY FirstName ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

    def delete_connection(self, ConnectionId):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM connections WHERE ConnectionId = '%s'" % (ConnectionId)
            cursor.execute(query)
            connection.commit()
            return
    def add_connection(self, MainUserId, FriendUserId):
        with dbapi2.connect(self.cp) as connection:
            cursor = connection.cursor()
            query =  "INSERT INTO connections (MainUserId, FriendUserId) VALUES ('%s','%s')" % (MainUserId, FriendUserId)
            cursor.execute(query)
            connection.commit()
            return
