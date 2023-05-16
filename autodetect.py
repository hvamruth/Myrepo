import platform
import subprocess
import sys

def install_python():
    # Check the system's platform
    current_platform = platform.system()

    if current_platform == 'Windows':
        # Download the Python installer for Windows
        url = 'https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe'
        subprocess.run(['powershell', '-Command', "(New-Object System.Net.WebClient).DownloadFile('{}', 'python_installer.exe')".format(url)])

        # Run the Python installer silently
        subprocess.run(['python_installer.exe', '/quiet', 'PrependPath=1'])

        # Clean up the installer file
        subprocess.run(['del', 'python_installer.exe'], shell=True)

    elif current_platform == 'Linux':
        # Check if the system has apt package manager
        if subprocess.run(['which', 'apt-get'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            # Install Python using apt
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3'])

        # Check if the system has yum package manager
        elif subprocess.run(['which', 'yum'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            # Install Python using yum
            subprocess.run(['sudo', 'yum', 'install', '-y', 'python3'])

        else:
            print("Unable to determine package manager. Please install Python manually.")

    elif current_platform == 'Darwin':
        # Check if the system has Homebrew package manager
        if subprocess.run(['which', 'brew'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            # Install Python using Homebrew
            subprocess.run(['brew', 'install', 'python'])

        else:
            print("Homebrew not found. Please install Python manually.")

    else:
        print("Unsupported platform. Please install Python manually.")

def check_python_installed():
    try:
        subprocess.run(['python', '--version'], capture_output=True)
    except FileNotFoundError:
        return False

    return True

if not check_python_installed():
    print("Python not found. Installing...")
    install_python()

# Python is now installed, continue with your code here
print("Python is installed!")
print("Python version:", sys.version)
