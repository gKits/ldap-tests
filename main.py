from ldap3 import Server, Connection, ALL, NTLM
from elizabeth import Text, Address, Personal
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersToGroups
import random

serverName = 'AD-DAP_TEST.testdap.com'
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

data = Text('en')
for _ in range(0, 10):
    currentGroup = 'cn=' + data.word() + ',ou=test-groups,dc=stand,dc=local'
    groupsDnList.append(currentGroup)
    conn.add(currentGroup, 'group')

address = Address('en')
person = Personal('en')
for _ in range(0, 10):
    address_country = address.country()
    conn.add('ou=' + address_country + ',ou=test-ou,dc=stand,dc=local', 'organizationalUnit')
    for _ in range(0, 10):
        name = person.name(gender='male')
        surname = person.surname(gender='male')
        currentUser = 'cn=' + name + '.' + surname + ',' + 'ou=' + address_country + ',ou=test-ou,dc=stand,dc=local'
        usersDnList.append(currentUser)
        conn.add(
            currentUser,
            'User',
            {
                'givenName': name,
                'sn': surname,
                'departmentNumber': 'DEV',
                'telephoneNumber': 1111
            }
        )

for _ in range(0, 300):
    rndUser = random.choice(usersDnList)
    rndGroup = random.choice(groupsDnList)
    addUsersToGroups(conn, rndUser, rndGroup)
