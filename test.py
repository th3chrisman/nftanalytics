#!/usr/bin/python

import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'cliquin',
    'password': '',
    'host': '35.193.3.52',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}


cnxn = mysql.connector.connect(**config)
