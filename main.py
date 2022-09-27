from ldap3 import (
    #  Server,
    Connection,
    # ALL,
    NTLM
)


# server = Server('172.16.221.2')
# conn = Connection(server)
# conn.bind()

conn = Connection('172.16.221.2', auto_bind=True, user='DAP\\Administrator', password='Test123!', authentication=NTLM)
print(conn)
