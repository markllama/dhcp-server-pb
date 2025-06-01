#!/usr/bin/env python
#
#
#
import argparse
import ldap3
import yaml


# domain:
# server:
# user:
#   "cn": "",
#   "pw": ""

ldap_server = "intel2.lab.lamourine.org"

ldap_user = {
    'dn': "cn=admin,dc=lab,dc=lamourine,dc=org",
    'pw': "This is $uch a G@mble"
}

def parse_args():
        parser = argparse.ArgumentParser()

        parser.add_argument("--db-user")
        return parser.parse_args()

if __name__ == "__main__":
    print("Hello")

    opts = parse_args()
    
    server = ldap3.Server(ldap_server, get_info=ldap3.ALL)
    connection = ldap3.Connection(server, user=ldap_user['dn'], password=ldap_user['pw'])
    connection.bind()

    print(connection)

    result = connection.search("dc=lab,dc=lamourine,dc=org", "(objectclass=dhcpHost)", attributes=ldap3.ALL_ATTRIBUTES)

#    print(result)
    for l in connection.entries:
        print(l.entry_to_ldif()) 

