import os

def install_nvidia_drivers():
    os.system("apt update && apt upgrade -y")
    os.system("ubuntu-drivers autoinstall")

def install_cuda_drivers():
    os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb")
    os.system("sudo dpkg -i cuda-keyring_1.1-1_all.deb")
    os.system("apt update")
    os.system("apt install cuda -y")

def install_ssh():
    os.system("sudo apt install openssh-server")
    os.system("sudo systemctl enable ssh")

def install_gpu_burn():
    os.system("sudo apt install g++")
    os.system("git clone https://github.com/wilicc/gpu-burn.git")
    os.system("cd gpu-burn && make")

def main():
    install_nvidia_drivers()
    install_cuda_drivers()
    install_ssh()
    install_gpu_burn()
    print("Please reboot your machine")

if __name__ == '__main__':
    main()