from ldap3 import (
    Server,
    Connection,
    ALL,
    NTLM,
    Tls,
)
import ssl

tls_config = Tls(
    validate=ssl.CERT_NONE,
    # version=ssl.PROTOCOL_TLSv1
)
server = Server('172.16.221.2', get_info=ALL, use_ssl=False, tls=tls_config)
# conn = Connection(server)
# conn.bind()

conn = Connection(server, auto_bind=True, user='TESTDAP\\Administrator', password='Test123!', authentication=NTLM)
conn.extend.standard.who_am_i()
print(conn)

group_dn = 'cn=TestUsers,ou=0_Groups,dc=AD-DAP_TEST,dc=testdap,dc=LOCAL'
object_class = 'groupOfNames'
attr = {
    'cn': 'TestUsers',
    'member': 'uid=Administrator,ou=Users,dc=AD-DAP_TEST,dc=testdap,dc=com',
    'description': 'Test group',
    'sAMAccountName': 'TestGroup'
}
conn.add(group_dn, object_class, attr)
