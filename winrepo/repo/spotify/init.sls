# Download the installer and it will download the latest version
spotify:
  1.0:
    installer: 'http://download.spotify.com/Spotify Installer.exe'
    install_flags: ' /silent'
    full_name: 'Spotify'
    reboot: False
    msiexec: False
    uninstaller: 'c:\Users\%username%\AppData\Roaming\Spotify\spotify.exe'
    uninstall_flags: ' /uninstall /silent'
