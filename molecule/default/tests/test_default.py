import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_papertrail_conf_file(host):
    f = host.file('/etc/log_files.yml')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_papertrail_files_to_log(host):
    f = host.file('/etc/log_files.yml')

    assert f.contains('/var/log/dmesg')


def test_papertrail_files_to_exclude(host):
    f = host.file('/etc/log_files.yml')

    assert f.contains(r'/var/log/\*.old')


def test_papertrail_exclude_patterns(host):
    f = host.file('/etc/log_files.yml')

    assert f.contains('this is a test')


def test_papertrail_service(host):
    s = host.service('remote_syslog')

    assert s.is_enabled
    assert s.is_running
