import sys

import config
import dao
import ipmi

cmd = sys.argv[1]
ip = sys.argv[2]

if cmd is None:
    print "usage: control.py <command> <ip>"
    sys.exit(0)

config = Config().get_config("business.json")
dao = DAO()

logline = join(" ", sys.argv)
dao.put_log(time.now() + " " + logline )
if cmd == "install":
    ipmi()
elif cmd == "images":
    print(dao.get_images())
else:
    print("Command not supported")
