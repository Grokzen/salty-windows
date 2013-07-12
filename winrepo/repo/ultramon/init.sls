# TODO: Add jinja support for x86/x64 compability
ultramon-x64:
  3.2.2:
    installer: 'http://www.realtimesoft.com/files/UltraMon_3.2.2_en_x64.msi'
    install_flags: ' ALLUSERS=1 /qb REBOOT=Supress'
    full_name: 'Ultramon 3.2.2 en x64'
    reboot: False
    msiexec: True
    uninstaller: 'salt://win/repo/ultramon/UltraMon_3.2.2_en_x64.msi'
    uninstall_flags: ' /q'

ultramon-x86:
  3.2.2:
    installer: 'http://www.realtimesoft.com/files/UltraMon_3.2.2_en_x32.msi'
    install_flags: ' ALLUSERS=1 /qb REBOOT=Supress'
    full_name: 'Ultramon 3.2.2 en x32'
    reboot: False
    msiexec: True
    uninstaller: 'salt://win/repo/ultramon/UltraMon_3.2.2_en_x32.msi'
    uninstall_flags: ' /q'
