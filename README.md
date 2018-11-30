# Datadog Raspberry Pi Speed test
Datadog check which checks download / upload speeds every 5 minutes.

#### Installation
- Install datadog on RPI
  - https://docs.datadoghq.com/developers/faq/deploying-the-agent-on-raspberrypi/
  - Optionally, enable systemd service
  - Copy `datadog.service` to `/etc/systemd/system/datadog.service`
  - Enable and start service:
    ```
    systemctl daemon-reload
    systemctl enable datadog.service
    service datadog start
    ```
- Install pip requirements  
`/root/.datadog-agent/venv/bin/pip install speedtest-cli`
- Copy directories from this repo to  
`/root/.datadog-agent/agent/`
- Restart datadog agent  
`service datadog restart`
