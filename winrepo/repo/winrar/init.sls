# This downloads english language. Winrar supports many languages.
winrar-x64:
  4.20.0:
    installer: 'http://www.rarlab.com/rar/winrar-x64-420.exe'
    install_flags: ' /S'
    full_name: 'WinRAR 4.20 (64-bit)'
    reboot: False
    msiexec: False
    uninstaller: '%ProgramFiles%/winrar/uninstall.exe'
    uninstall_flags: ' /S'
winrar-x86:
  4.20.0:
    installer: http://www.rarlab.com/rar/wrar420.exe
    install_flags: ' /S'
    full_name: 'WinRAR 4.20 (32-bit)'
    reboot: False
    msiexec: False
    uninstaller: '%ProgramFiles%/winrar/uninstall.exe'
    uninstall_flags: ' /S'
