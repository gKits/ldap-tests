from ldap3 import (
    Server,
    Connection,
    ALL,
    NTLM
)

server = Server('172.16.221.2', get_info=ALL)
# conn = Connection(server)
# conn.bind()

conn = Connection(server, auto_bind=True, user='TESTDAP\\Administrator', password='Test123!', authentication=NTLM)
conn.start_tls()
conn.extend.standard.who_am_i()
print(conn)
