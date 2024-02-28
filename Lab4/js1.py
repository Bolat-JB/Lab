import json

with open('sample-data.json') as k:
    f = json.loads(k)

interf = []

for item in f.get('imdata', []):
    if 'l1PhysIf' in item:
        interface = item['l1PhysIf']['attributes']
        interface_dn = interface.get('dn', '')
        interface_descr = interface.get('descr', '')
        interface_speed = interface.get('speed', 'inherit')
        interface_mtu = interface.get('mtu', '')
        interf.append((interface_dn, interface_descr, interface_speed, interface_mtu))


print("Interface Status")

for interface in interf:
    print("{:<50} {:<20} {:<8} {:<8}".format(*interface))
