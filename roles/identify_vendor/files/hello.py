from easysnmp import snmp_get
import os

description = snmp_get(
    'iso.3.6.1.2.1.1.1.0', 
    hostname=os.getenv('HOST'), 
    community=os.getenv('COMMUNITY'), 
    version=2
    )

print(str(description))