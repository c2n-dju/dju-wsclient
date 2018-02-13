import json
import os
import requests
from datetime import datetime


def getjson(server, path):
    a = requests.get(os.environ[server] + path)
    if not a.ok:
        a.raise_for_status()
    return a.json()


j = getjson("WSS", "structure_restapi/")
kkk = {'cle', 'id', 'perss', 'sousstrasc', 'sousstrdesc', 'titre'}
for x in j:
    assert(set(x.keys()) == kkk)

def sornone(s):
    if s == None:
        return ""
    else:
        return s




class C2N_Structure_Pers:
    def __init__(self, p):
        role = p['role']
        assert(role.keys() == {'rolepersonnec2n'})
        self.din = datetime.strptime(p['din'], '%Y-%m-%d')
        self.dout = datetime.strptime(p['dout'], '%Y-%m-%d')
        self.email = p['email']
        self.nom = p['nom']
        self.numerotel = sornone(p['numerotel'])
        self.prenom = p['prenom']
        self.quotite = p['quotite']
        self.role = role['rolepersonnec2n']
        self.statut = p['statut']


class C2N_Structure:
    def __init__(self, s):
        self.cle = int(s["cle"])
        self.id = s["id"]
        self.perss = list(map(lambda x:C2N_Structure_Pers(x), s["perss"]))
        self.sousstrasc = list(set(map(lambda x:x["idstructurec2n1"], s["sousstrasc"])))
        self.sousstrdesc = list(set(map(lambda x:x["idstructurec2n2"], s["sousstrdesc"])))
        self.titre = s["titre"]

c2n_structure = list(map(lambda x: C2N_Structure(x), j))

iofid = dict()
ioftitre = dict()
iofpers = dict()

for (i,s) in enumerate(c2n_structure):
    iofid[s.id] = i
    ioftitre[s.titre] = i
    for p in s.perss:
        np = p.nom + " " + p.prenom
        quot = p.quotite
        if np in iofpers:
            iofpers[np].append((i, quot))
        else:
            iofpers[np] = [(i, quot)]

list(map(lambda y:(y.titre, sorted(list(map(lambda x:c2n_structure[iofid[x]].titre, y.sousstrdesc)))), c2n_structure))

ll = 0
for np in iofpers.keys():
    l = len(np)
    if l > ll:
        ll = l
for np in sorted(iofpers.keys()):
    l = len(np)
    print(np + ' ' * (ll - l + 1) + ', '.join(sorted(map(lambda x:c2n_structure[x[0]].titre + ' (' + str(x[1]) + ')', iofpers[np]))))

ll = 0
for n in ioftitre.keys():
    l = len(n)
    if l > ll:
        ll = l
for n in sorted(ioftitre.keys()):
    l = len(n)
    print(n +  ' ' * (ll - l + 1) + ', '. join(sorted(map(lambda x:c2n_structure[iofid[x]].titre, c2n_structure[ioftitre[n]].sousstrdesc))))



for n in sorted(ioftitre.keys()):
    l = len(n)
    print(n + ' ' *  (ll - l + 1) + ', '.join(sorted(map(lambda x:c2n_structure[iofid[x]].titre, c2n_structure[ioftitre[n]].sousstrasc))))


for n in sorted(ioftitre.keys()):
    l = len(n)
    print('\n' + n + ' ' * (ll - l + 1) + ('\n' +  ' ' * (ll+1)).join(sorted(map(lambda x: x.nom + ' ' + x.prenom + ' (' + x.role + ', ' + str(x.quotite) + ', ' +  x.statut + ')', c2n_structure[ioftitre[n]].perss))))

a = requests.get(os.environ['WOSS'] + 'tablepublis', auth=(os.environ['LDAP_LOGIN'], os.environ['LDAP_PASSWORD']))












