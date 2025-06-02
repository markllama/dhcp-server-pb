# `dhcp-server-pb`
An Ansible playbook to create an LDAP backed DHCP server

## HISTORY

A decade ago I wrote a [blog
post](https://electron-swamp.blogspot.com/2014/05/robust-and-flexable-dhcp-and.html)
about how to create an ISC DHCP server backed by an OpenLDAP
database. The goal was to allow the DHCP lease reservations to be
managed just by modifying the database. For normal use, DHCP host
records change rarely and are almost always added rather than removed
or modified. In a lab space, especially when using DHCP to initate PXE
network boot and OS installation, the hosts may cycle through much more
quickly, and asking lab users to manually edit the DHCP server
configuration file is undesirable. The ISC DHCP server is able to pull
its configuration from an LDAP server and offers a way to create a
more user-friendly update method using either a web or CLI interface.

I recently revisited that post and I found that a couple of small
things had changed and some new options have appeared since then.

The simple change was that I had to look harder to find the LDAP DHCP
schema file in the available packages and convert it to LDIF
format. It's still in the ISC Github repository, but it's not always
included in the DHCP server packages.

One new option was Ansible, which, while it existed in 2014, it wasn't
yet widely used, since its release in Feb 2012. The other is software
containers. Again they weren't yet widely used. The final change will
completely obsolete this exercise; ISC has deprecated ISC DHCP in
favor of ISC Kea. Kea comes native with the ability to manage the
configuration from either MariaDB (aka MySQL) or PostgreSQL.

In this repo I make use of Ansible, but so far remain with ISC DHCP
and OpenLDAP `slapd`. I have created an ISC DHCP server container,
but I haven't containerized OpenLDAP yet and given the move to ISC
Kea and a relational database, I probably won't go much farther in
this direction.

The original post used Red Hat Enterprise Linux or Fedora Linux as the
OS base. The current version is built using Ubuntu, though the hooks
exist to implement it on RPM based systems as well.

## Usage

The DHCP server with its attached LDAP server are deployed using the
ansible playbook `dhcp-server-pb.yaml`.
	
	ansible-playbook --vault-secrets-file vault-secrets dhcp-server-pb.yaml

### Preparation

    git clone https://github.com/markllama/dhcp-server-pb
	cd dhcp-server-pb

#### Host Initialization

I am starting currently with a minimal installation of [Ubuntu
Server](https://ubuntu.com/download/server). I have installed it from
USB live installer and set a static IP address. I created a non-root
user, granted that user `sudo` access with *NOPASSWD* and installed an
SSH public key. With this, I can configure logins from my deployment
system using SSH to a user with sudo privileges to execute the Ansible
commands.

* Ubuntu Server
  * Minimal Installation
  * Fixed IP Address
  * SSH server installed
* Local user
  * SSH Public key in `.ssh/authorized_keys`
  * `sudo` access with *NOPASSWD*

#### Ansible Setup

On the deployment server, 

#### Host Variables

#### Managing Secrets - Ansible Vault

### Execution

## Implementation

## TODO

* Adapt to RPM based systems
* Convert to use software containers
* Re-implement with ISC Kea and MariaDB

## References

* ISC DHCP - https://www.isc.org/dhcp/
* OpenLDAP `slapd` - https://www.openldap.org/

* ISC Kea - https://www.isc.org/kea/
* MariaDB - https://mariadb.com/
  
