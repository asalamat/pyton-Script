from ldap3 import ALL, Connection, Server
from ldap3.core.exceptions import LDAPException

username = "lcbo\ueais"
password = "M3rryXm@s4225"
ldap_base = "dc=lcbo,dc=com"

server = Server(
    host="ldaps://dch005.lcbo.com",
    port=636,
    use_ssl=True,
    get_info=ALL,
conn.search('dc=lcbo,dc=com', '(objectclass=computer)')
computers = [entry['attributes']['dNSHostName'] for entry in conn.entries]

with open('computers.txt', 'w') as f:
    for computer in computers:
        f.write(computer + '\n')
