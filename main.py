from ldap3 import (
    #  Server,
    Connection,
    # ALL
)


# server = Server('172.16.221.2')
# conn = Connection(server)
# conn.bind()

conn = Connection('172.16.221.2', auto_bind=True)
print(conn)
