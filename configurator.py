import os

def install_nvidia_drivers():
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system("sudo apt install ubuntu-drivers-common")
    os.system("sudo apt install nvidia-driver-535")

def install_cuda_drivers():
    os.system("sudo apt install gcc")
    os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb")
    os.system("sudo dpkg -i cuda-keyring_1.1-1_all.deb")
    os.system("sudo apt update")
    os.system("sudo apt install cuda -y")

def install_ssh():
    os.system("sudo apt install openssh-server")
    os.system("sudo systemctl enable ssh")


def main():
    install_nvidia_drivers()
    install_cuda_drivers()
    install_ssh()
    print("Please reboot your machine")

if __name__ == '__main__':
    main()