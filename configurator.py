# TO DO:
# Find way to overwrite common-session with current file in /etc/pam.d/
# Find way to overwrite nsswitch.conf with current file in /etc/nsswitch.conf

import os
import sys
from time import sleep

# checks the euid if the user is root
def check_root() -> bool:
    if os.geteuid() != 0:
        return False
    else:
        return True
    
def check_syntax() -> bool:
    if len(sys.argv) < 3 or len(sys.argv) > 3:
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

# clones gpu burn which stress tests graphics cards
def clone_gpu_burn():
    os.system("git clone https://github.com/wilicc/gpu-burn")
    print("GPU-Burn was cloned in current directory...")
    sleep(5)

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

# components installed when dealing with GPU server
def gpu_server_install():
    #generic_server_install()
    #install_nvidia_drivers()
    #install_cuda_drivers()
    clone_gpu_burn()

# components installed when dealing with a regular server
def generic_server_install():
    install_ssh()

def main():
    # returns true if the checks pass
    is_root = check_root()
    has_correct_syntax = check_syntax()
    
    # check if the boolean returned matches with the correct syntax
    if is_root == True and has_correct_syntax == True:
        selected_option = int(sys.argv[2])

        # depending on which option the user specified, a different path will be taken
        if selected_option == 1:
            print("Commencing Generic Server Install...")
            sleep(10)
            generic_server_install()
            
        elif selected_option == 2:
            print("Commencing GPU Server Install...")
            sleep(10)
            gpu_server_install()

        else:
            print("ERROR: Please select a valid option")
            help()

        print("Please reboot your machine")
    
    elif is_root == False:
        print("ERROR: Did you run with Sudo?")
    
    elif is_root == True and has_correct_syntax == False:
        print("ERROR: Please select an option")
        help()

    else:
        print("ERROR: Please see help menu")
        help()

if __name__ == '__main__':
    main()