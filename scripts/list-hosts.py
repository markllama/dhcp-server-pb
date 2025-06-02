#!/usr/bin/env python
#
#
#

import argparse
try:
    import ldap3
except ModuleNotFoundError as e:
    print("FATAL: Missing required module 'ldap3'")
    exit(2)
import os
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

class LDAP_Config():

    def __init__(self, config_file=f"{os.getenv('HOME')}/.ldap_server"):
        self.config_file = config_file
        self.config = yaml.safe_load(open(config_file))

    @property
    def hostname(self):
        return self.config['server']

    @property
    def domain(self):
        return self.config['domain']    
        
    @property
    def fqdn(self):
        return ".".join([self.config['server'], self.config['domain']])

    @property
    def server_dn(self):
        # preface each element with dc=
        return "dc=" + ",dc=".join([self.config['server']] + self.config['domain'].split('.'))

    @property
    def bind_dn(self):
        return f"cn={self.config['user']['cn']},{self.server_dn}"

    @property
    def bind_pw(self):
        return self.config['user']['pw']
        
    
def parse_args():
        parser = argparse.ArgumentParser()

        parser.add_argument("--db-user")
        return parser.parse_args()

if __name__ == "__main__":
    print("Hello")

    opts = parse_args()
    config = LDAP_Config()
    
    server = ldap3.Server(config.fqdn, get_info=ldap3.ALL)
    connection = ldap3.Connection(server, config.bind_dn, password=config.bind_pw)
    connection.bind()

    print(connection)

    result = connection.search("dc=lab,dc=lamourine,dc=org", "(objectclass=dhcpHost)", attributes=ldap3.ALL_ATTRIBUTES)

#    print(result)
    for l in connection.entries:
        print(l.entry_to_ldif()) 

