#!/usr/bin/env python
#
#
#
import ldap3

ldap_proto = "https"
ldap_server = "intel2.lab.lamourine.org"
ldap_uri = f"{ ldap_proto }://{ ldap_server }"

ldap_user = {
    'dn': "cn=admin,dc=lab,dc=lamourine,dc=org",
    'pw': "This is $uch a G@mble"
}

if __name__ == "__main__":
    print("Hello")

    server = ldap3.Server(ldap_server)
    connection = ldap3.Connection(server, user=ldap_user['dn'], password=ldap_user['pw'])
    connection.bind()

    print(connection)

    result = connection.search("dc=lab,dc=lamourine,dc=org", "(objectclass=top)")

    print(result)
    print(connection.entries)

