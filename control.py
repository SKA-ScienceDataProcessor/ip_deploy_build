import sys
from datetime import datetime

from config import Config
from dao import DAO
from ipmi import lom_ipmi


cmd = sys.argv[1]
ip = sys.argv[2]

if cmd is None:
    print "usage: control.py <command> <ip>"
    sys.exit(0)

if ip is None or int(ip) > 255:
    print "usage: control.py <command> <ip>"
    sys.exit(0)

config = Config().get_config("business.json")
if not config:
    print "Could not find config file"
    sys.exit(0)

dao = DAO(config)

logline = " ".join(sys.argv)
dao.put_log(str(datetime.now()) + " " + logline )

if cmd == "install":
    lom_ipmi().connection_auth("user", "pass").host(config, ip).command(cmd)
elif cmd == "images":
    print(dao.get_images())
else:
    print("Command not supported")
