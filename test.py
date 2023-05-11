import csv
from ldap3 import Server, Connection, ALL

# Define LDAP server connection details
server_address = 'dch004.lcbo.com'  # Replace with your LDAP server address
server_port = 389  # Replace with your LDAP server port
username = 'lcbo\\ueais'  # Replace with your username
password = 'M3rryXm@s4225'  # Replace with your password

# Connect to LDAP server
server = Server(server_address, port=server_port, get_info=ALL)
conn = Connection(server, user=username, password=password, auto_bind=True)

# Define LDAP search parameters
base_dn = 'DC=lcbo,DC=com'  # Replace with your search base
search_filter = '(objectCategory=computer)'

# Perform the LDAP search
conn.search(search_base=base_dn, search_filter=search_filter, attributes=['name', 'operatingSystem'])
entries = conn.entries

# Export the results to a CSV file
with open('ad_export.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['DNS Name', 'Operating System'])

    for entry in entries:
        dns_name = entry.name
        operating_system = entry.operatingSystem.value if 'operatingSystem' in entry else ''
        writer.writerow([dns_name, operating_system])

print('Export completed.')
