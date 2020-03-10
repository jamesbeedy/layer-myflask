from charms.reactive import when
from charmhelpers.core.hookenv import status_set, open_port


@when('snap.installed.myflask')
def set_available():
    open_port(8080)
    status_set("active", "MYFLASK RUNNING ON 8080")
