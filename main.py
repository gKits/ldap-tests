from ldap3 import (
    Server,
    Connection,
    ALL,
    NTLM
)


server = Server('172.16.221.2', get_info=ALL)
# conn = Connection(server)
# conn.bind()

conn = Connection(server, auto_bind=True, user='DAP/Administrator', password='Test123!', authentication=NTLM)
print(conn)
conn.extend.who_am_i()
