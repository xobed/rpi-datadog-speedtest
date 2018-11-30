# the following try/except block will make the custom check compatible with any Agent version
try:
    # first, try to import the base class from old versions of the Agent...
    from checks import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version 6 or later
    from datadog_checks.checks import AgentCheck

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "1.0.0"

class SpeedCheck(AgentCheck):
    def check(self, instance):
        import speedtest

        s = speedtest.Speedtest()
        server = s.get_best_server()
        latency = server['latency']
        down = s.download()
        up = s.upload()

        self.gauge('speedtest.download', down)
        self.gauge('speedtest.upload', up)
        self.gauge('speedtest.ping', latency)
