from ldap3 import Server, Connection, ALL, NTLM, Tls
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersToGroups
from misc import RANDOM_FIRSTNAMES, RANDOM_GROUP_NAME, RANDOM_LASTNAMES
from random import randint, choice
from ssl import CERT_NONE

tls_config = Tls(validate=CERT_NONE)

serverName = '172.16.221.2'
connUser = 'TESTDAP\\Administrator'
connUserPwd = 'Test123!'
usersOU = 'OU=test-ou,DC=testdap,DC=com'
groupsDN = 'CN=test-groups,OU=test-ou,DC=testdap,DC=com'

groupsDnList = []
usersDnList = []


server = Server(serverName, get_info=ALL, use_ssl=False, tls=tls_config)
conn = Connection(server, auto_bind=True, user=connUser, password=connUserPwd, authentication=NTLM)

conn.add(usersOU, 'organizationalUnit')
print(conn.result)
conn.add(groupsDN, 'organizationalUnit')
print(conn.result)

for group in RANDOM_GROUP_NAME:
    currentGroup = f'cn={group},ou=test-groups,dc=testdap,dc=com'
    groupsDnList.append(currentGroup)
    conn.add(currentGroup, 'Group')
    print(conn.result)


for _ in range(100):
    firstname = RANDOM_FIRSTNAMES[randint(0, len(RANDOM_FIRSTNAMES) - 1)]
    lastname = RANDOM_LASTNAMES[randint(0, len(RANDOM_LASTNAMES) - 1)]
    currentUser = f'cn={firstname}.{lastname},ou=test-ou,dc=testdap,dc=com'
    usersDnList.append(currentUser)
    conn.add(
        currentUser,
        'User',
        {
            'givenName': firstname,
            'sn': lastname,
            'departmentNumber': 'DEV',
            'telephoneNumber': 1111
        }
    )
    print(conn.result)

for _ in range(100):
    rndUser = choice(usersDnList)
    rndGroup = choice(groupsDnList)
    addUsersToGroups(conn, rndUser, rndGroup)
    print(conn.result)
