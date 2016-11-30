from nose.tools import assert_true, assert_false, eq_

from ipmi import lom_ipmi

def test_arg_power_options():
    ipmi = lom_ipmi()
    assert_true(ipmi._check_power("on"),True)

def test_false_arg_power_options():
    ipmi = lom_ipmi()
    assert_false(ipmi._check_power("restart"),True)

def test_arg_ip_exists():
    ipmi = lom_ipmi()
    assert_true(ipmi._check_ip("5"),True)

def test_arg_ip_does_not_exist():
    ipmi = lom_ipmi()
    assert_false(ipmi._check_ip(""),True)

def test_arg_ip_not_too_long():
    ipmi = lom_ipmi()
    assert_false(ipmi._check_ip("12345"),True)

def test_auth():
    ipmi =lom_ipmi().connection_auth("user", "pass")
    eq_(ipmi.user, "user")
    eq_(ipmi.passwd, "pass")

def test_build_command():
    ipmi =lom_ipmi().connection_auth("user", "pass").host("134").command("on")
    cmd_to_string = ' '.join(ipmi.build_command())
    eq_("ipmitools -v -I lanplus -H 134 -U user -P pass chassis power on", cmd_to_string)
