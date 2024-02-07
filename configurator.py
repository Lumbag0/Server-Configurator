import os
from time import sleep

def install_nvidia_drivers():
    os.system("apt update && apt upgrade -y")
    os.system("ubuntu-drivers autoinstall")

def install_cuda_drivers():
    os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb")
    os.system("sudo dpkg -i cuda-keyring_1.1-1_all.deb")
    os.system("apt update")
    os.system("apt install cuda -y")

def main():
    install_nvidia_drivers()
    install_cuda_drivers()
    print("Please reboot your machine")

if __name__ == '__main__':
    main()