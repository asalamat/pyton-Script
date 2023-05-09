import json
import os
from ldap3 import Server, Connection, ALL, NTLM

# Active Directory server information
AD_SERVER = 'dch004.lcbo.com'
AD_USER = 'ali.salamat@lcbo.com'
AD_PASSWORD = 'fffff'

# Define the LDAP search base and filter
search_base = 'ou=Computers,dc=example,dc=com'
search_filter = '(&(objectClass=computer)(objectCategory=computer))'

# Connect to the Active Directory server
server = Server(AD_SERVER, get_info=ALL)
conn = Connection(server, user=AD_USER, password=AD_PASSWORD, authentication=NTLM)
conn.bind()

# Search for computers
conn.search(search_base, search_filter, attributes=['sAMAccountName'])

# Create the inventory dictionary
inventory = {
    '_meta': {
        'hostvars': {}
    },
    'all': {
        'hosts': [],
        'vars': {}
    }
}

# Add the hosts to the inventory
for entry in conn.entries:
    host = entry['sAMAccountName'].value.split('.')[0]
    inventory['all']['hosts'].append(host)
    inventory['_meta']['hostvars'][host] = {}

# Print the inventory in JSON format
print(json.dumps(inventory, indent=2))
