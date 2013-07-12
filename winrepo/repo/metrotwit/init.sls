# Metrotwit for windows. Will download the tiny installer that will download the latest version during install
metrotwit:
  1.0:
    installer: 'http://www.metrotwit.com/download/MetroTwitSetup.exe'
    install_flags: ''
    full_name: 'MetroTwit for windows'
    reboot: False
    msiexec: False
  0.beta: # This is the beta release. To use, specify version explicit in .sls file
    installer: 'http://www.metrotwit.com/beta/MetroTwitLoop.exe'
    install_flags: ''
    full_name: 'MetroTwit for windows'
    reboot: False
    msiexec: False
