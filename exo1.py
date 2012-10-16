"""entete"""
import pdb
import sys
import httplib
Conn = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128)
pdb.set_trace()
Conn.request("GET", "http://www.python.org/index.html")
R1 = Conn.getresponse()
print R1.status, R1.reason
Log = False
if len(sys.argv) > 2:
    Log = True

def func():
    """fonction 1"""
    nom = func("test")
F = open("log.txt", "w")

def logger(F, message):
    """fonction 2"""
    if Log :
        F.write(message)
    logger(F,"statut: %s" %str(R1.status))
