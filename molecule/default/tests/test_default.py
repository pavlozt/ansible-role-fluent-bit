def test_command(host):
    assert host.command('service td-agent-bit status').rc == 0
