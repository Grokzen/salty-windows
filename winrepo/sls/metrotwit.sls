# Copy file from master to slave
downloadCert:
  file.managed:
    - name: c:/salt/var/cache/salt/minion/files/base/win/repo/MetrotwitCert.cer
    - source: "salt://win/repo/metrotwit/MetrotwitCert.cer"

installCert:
  cmd.wait:
    - name: 'certutil -addstore "TrustedPublisher" "c:/salt/var/cache/salt/minion/files/base/win/repo/MetrotwitCert.cer"'
    - watch:
      - file: downloadCert
      
metrotwit:
  pkg.installed:
    - require:
      - cmd: installCert

