import os
import sys

# checks the euid if the user is root
def check_root() -> bool:
    if os.geteuid() != 0:
        return False
    else:
        return True
def check_syntax() -> bool:
    if len(sys.argv) < 3 or len(sys.argv) > 3
        return False
    else:
        return True

# updates the machine and installs the required drivers
def install_nvidia_drivers():
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system("sudo ubuntu-drivers autoinstall")

# installs gcc, g++ and cuda drives
def install_cuda_drivers():
    os.system("sudo apt install gcc g++")
    os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb")
    os.system("sudo dpkg -i cuda-keyring_1.1-1_all.deb")
    os.system("sudo apt update")
    os.system("sudo apt install cuda -y")

# install ssh
def install_ssh():
    os.system("sudo apt install openssh-server")
    os.system("sudo systemctl enable ssh")

def help():
    print("Usage: configurator.py -o <Install Type>")
    print("Install Types:")
    print("----------------------")
    print("1. Generic Install")
    print("2. GPU install")
    print("----------------------")
    print("Generic Install")
    print("SSH")
    # need to add other parts from ubuntu checklist
    print("----------------------")
    print("GPU Install")
    print("SSH")
    print("Nividia Drivers")
    print("CUDA Drivers")
    print("GPU-Burn")
    # need to add other parts from ubuntu checklist

def main():
    is_root = check_root()
    has_correct_syntax = check_syntax()
    
    if is_root == True and has_correct_syntax == True
        install_nvidia_drivers()
        install_cuda_drivers()
        install_ssh()
        print("Please reboot your machine")
    
    else if is_root == False and has_correct_syntax == True:
        print("ERROR: Did you run with Sudo?")
    
    else if is_root == True and has_correct_syntax == False:
        print("ERROR: Please select an option")
        help()

if __name__ == '__main__':
    main()