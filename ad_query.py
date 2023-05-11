from ldap3 import Server, Connection, ALL

# Active Directory server details
server_address = 'dch004.lcbo.com'
domain = 'lcbo.com'
username = 'lcbo\ueais'
password = 'M3rryXm@s4225'

# Output file path
output_file = 'computer_names.txt'

# LDAP query to retrieve computer names
ldap_query = '(objectClass=computer)'

try:
    # Connect to the Active Directory server
    server = Server(server_address, get_info=ALL)
    conn = Connection(server, user=f'{username}@{domain}', password=password, auto_bind=True)

    # Perform the LDAP search
    conn.search(search_base=domain, search_filter=ldap_query, attributes=['cn'])

    # Extract the computer names from the search results
    computer_names = [entry['cn'].value for entry in conn.entries]

    # Write the computer names to a text file
    with open(output_file, 'w') as file:
        file.write('\n'.join(computer_names))

    print(f"Computer names exported to {output_file} successfully.")

except Exception as e:
    print(f"Error: {str(e)}")

