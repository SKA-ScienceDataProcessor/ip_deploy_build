### IP Deploy Build

A script to control the Integration Prototype nodes and to re-install them

The main use is:
 
    python control.py <command> <last IP quad>

The install command installs a target node with an Ubuntu 16.04 LTS image. 

The on, off, or cycle commands control the power via a wrapper around IPMI. 

Logging is provided by the DAO file. At present, this is provided by Redis, a lightweight data structure store. 

#### Dependencies

ipmitool must be installed on the host machine.
pyredis

If you get an error that it can find /dev/ipmi0 or /dev/ipmidev/0, it needs adding to the kernel.
Run the following as sudo:
modprobe ipmi_devintf
modprobe ipmi_si

[Redis] (redis.io)

#### License
See the license file
