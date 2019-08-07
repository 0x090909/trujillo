# <VirtualHost *:80>
# 	# The ServerName directive sets the request scheme, hostname and port that
# 	# the server uses to identify itself. This is used when creating
# 	# redirection URLs. In the context of virtual hosts, the ServerName
# 	# specifies what hostname must appear in the request's Host: header to
# 	# match this virtual host. For the default virtual host (this file) this
# 	# value is not decisive as it is used as a last resort host regardless.
# 	# However, you must set it for any further virtual host explicitly.
# 	#ServerName www.example.com
#
# 	ServerAdmin webmaster@localhost
# 	DocumentRoot /var/www/html
#
# 	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
# 	# error, crit, alert, emerg.
# 	# It is also possible to configure the loglevel for particular
# 	# modules, e.g.
# 	#LogLevel info ssl:warn
#
# 	ErrorLog ${APACHE_LOG_DIR}/error.log
# 	CustomLog ${APACHE_LOG_DIR}/access.log combined
#
# 	# For most configuration files from conf-available/, which are
# 	# enabled or disabled at a global level, it is possible to
# 	# include a line for only one particular virtual host. For example the
# 	# following line enables the CGI configuration for this host only
# 	# after it has been globally disabled with "a2disconf".
# 	#Include conf-available/serve-cgi-bin.conf
# 	ProxyPreserveHost On
#         RewriteEngine on
#         #RewriteLog /var/log/apache2/rewrite.log
#         RewriteMap ipfsmap "txt:/home/cristy/Documents/Work/trujillo/map_file.txt"
#
#
# 	#RewriteRule "^/(.*)" "/${ipfsmap:$1}" [L,NC]
#
# 	RewriteRule "^/(.*)" "http://ipfs.greyh.at/ipfs/${ipfsmap:$1}" [P]
#
# 	ProxyPass / http://ipfs.greyh.at/ipfs/
#         ProxyPassReverse / http://ipfs.greyh.at/ipfs/
# </VirtualHost>
#
# # vim: syntax=apache ts=4 sw=4 sts=4 sr noet

# this tool generates the apache configuration with the use of the mapping between
# system files and ipfs hashes

import os

def get_info():
    hostname = input("[+] Virtual hostname (mypersonalcdn.com): ")
    if hostname=="":
        hostname = "mypersonalcdn.com"

    mapping_path = input("[+] File database mapping (./map_file.txt): ")
    cwd = os.getcwd()
    if mapping_path=="":
        mapping_path = cwd + "/mapping_file.txt"

    ipfs_gateways = []
    i = 0
    gateway = input("[+] IPFS Gateway (Blank to stop): ")
    while gateway != "":
        ipfs_gateways.append(gateway)
        gateway = input("[+] IPFS Gateway (Blank to stop): ")
    if len(ipfs_gateways) == 0:
        ipfs_gateways.append("http://ipfs.greyh.at/ipfs/")


    return {"hostname":hostname, "mapping_path": mapping_path, "gateways": ipfs_gateways}

def generate_configuraion(dict_config):
    config = "<VirtualHost " + dict_config['hostname'] + ":80>\n"
    config += "ServerAdmin webmaster@localhost\n"
    config += "DocumentRoot /var/www/html\n"
    config += "ErrorLog ${APACHE_LOG_DIR}/error.log\n"
    config += "CustomLog ${APACHE_LOG_DIR}/access.log combined\n"
    #enable reverse proxy
    config += "ProxyPreserveHost On\n"
    config += "RewriteEngine on\n"
    config += "RewriteMap ipfsmap '"+dict_config['mapping_path']+"'\n"
    #delegate rewritten url to mod_proxy
    config += 'RewriteRule "^/(.*)" "${ipfsmap:$1}" [P]\n'
    config += "ProxyPass / " + dict_config['gateways'][0] + '\n'
    config += "ProxyPassReverse / " + dict_config['gateways'][0] + '\n'
    config += "</VirtualHost>"
    return config

if __name__ == "__main__":
    print(generate_configuraion(get_info()))
