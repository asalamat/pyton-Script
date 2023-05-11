from ldap3 import Server, Connection, ALL

server = Server('10.9.11.70', get_info=ALL)
conn = Connection(server, 'lcbo\ueais', 'M3rryXm@s4225', auto_bind=True)

conn.search('dc=lcbo,dc=com', '(objectclass=computer)')

computers = [entry['attributes']['dNSHostName'] for entry in conn.entries]

with open('computers.txt', 'w') as f:
    for computer in computers:
        f.write(computer + '\n')
