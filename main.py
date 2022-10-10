from ldap3 import (
    Server,
    Connection,
    ALL,
    NTLM,
    MODIFY_ADD,
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

conn.search(search_base='cn=Administrator,DC=ad-dap_test,DC=testdap,DC=com', search_filter='(sAMAccountName=Administrator)')
print(conn.result)

group_dn = 'CN=TestGroup2,OU=TestOU,DC=testdap,DC=com'
user_dn = 'CN=Test User1,OU=TestOU,DC=testdap,DC=com'
conn.modify(group_dn, [MODIFY_ADD, 'member', [user_dn]])
print(conn.result)
