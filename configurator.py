import os

# checks the euid if the user is root
def check_root() -> bool:
    if os.geteuid() != 0:
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

def main():
    is_root = check_root()
    if is_root == True:  
        install_nvidia_drivers()
        install_cuda_drivers()
        install_ssh()
        print("Please reboot your machine")
    else:
        print("Please run this script with sudo")

if __name__ == '__main__':
    main()