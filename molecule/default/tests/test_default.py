def pkg_is_installed(host):
    package = host.package('td-agent-bit')

    assert package.is_installed

def test_service_is_running(host):
    service = host.service('td-agent-bit')

    assert service.is_running
    assert service.is_enabled
