import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
   os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_hosts_file(host):
    f = host.file("etc/hosts")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_installation(host):
    assert host.package("fluent-bit").is_installed

def test_config_file(host):
    config = host.file("/etc/fluent-bit/fluent-bit.conf")
    assert config.exists
    assert config.is_file
    assert config.user == 'root'
    assert config.group == 'root'
    assert config.mode == 0o644

def test_service(host):
    fluent_bit = host.service("fluent-bit")
    assert fluent_bit.is_running
    assert fluent_bit.is_enabled
