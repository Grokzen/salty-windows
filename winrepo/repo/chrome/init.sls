chrome:
  26.0.1440.64:
    installer: 'salt://win/repo/chrome/GoogleChromeStandaloneEnterprise.msi'
    install_flags: ' /quiet /norestart'
    full_name: Google Chrome
    reboot: False
    msiexec: False
    uninstaller: '%ProgramFiles(x86)%/google/chrome/application/26.0.1410.64/installer/setup.exe'
    uninstall_flags: ' --uninstall --multi-install --chrome --system-level --force-uninstall'
