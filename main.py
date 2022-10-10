from ldap3 import Server, Connection, ALL, NTLM
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersToGroups
from misc import RANDOM_FIRSTNAMES, RANDOM_GROUP_NAME, RANDOM_LASTNAMES
from random import randint, choice


serverName = '172.16.221.2'
connUser = 'TESTDAP\\Administrator'
connUserPwd = 'Test123!'
usersOU = 'OU=test-ou,DC=testdap,DC=com'
groupsDN = 'CN=test-groups,OU=test-ou,DC=testdap,DC=com'

groupsDnList = []
usersDnList = []


server = Server(serverName, get_info=ALL)
conn = Connection(server, user=connUser, password=connUserPwd, authentication=NTLM)
conn.bind()

conn.add(usersOU, 'organizationalUnit')
conn.add(groupsDN, 'organizationalUnit')

for group in RANDOM_GROUP_NAME:
    currentGroup = f'cn={group},ou=test-groups,dc=stand,dc=local'
    groupsDnList.append(currentGroup)
    conn.add(currentGroup, 'group')


for _ in range(100):
    firstname = RANDOM_FIRSTNAMES[randint(len(RANDOM_FIRSTNAMES))]
    lastname = RANDOM_LASTNAMES[randint(len(RANDOM_LASTNAMES))]
    currentUser = f'cn={firstname}.{lastname},ou=test-ou,dc=stand,dc=local'
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

for _ in range(0, 300):
    rndUser = choice(usersDnList)
    rndGroup = choice(groupsDnList)
    addUsersToGroups(conn, rndUser, rndGroup)
