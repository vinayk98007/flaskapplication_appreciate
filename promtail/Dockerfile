FROM grafana/promtail:2.9.1
COPY promtail-config.yml /etc/promtail/config.yml
ENTRYPOINT ["/usr/bin/promtail", "-config.file=/etc/promtail/config.yml"]
