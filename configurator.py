import os
import sys
import getopt
from time import sleep

def update():
    print("\nUpgrading System...\n")
    sleep(5)
    os.system("sudo apt update && sudo apt upgrade -y")

def configure_ldap_client():
    print("\nStarting LDAP Setup\n")
    sleep(5)
    os.system("sudo sh -c 'echo -n | openssl s_client -connect kato.vast.uccs.edu:636 | " "sed -ne \'/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p\' > " "/usr/local/share/ca-certificates/ldap_ca_server.crt'")
    os.system("sudo update-ca-certificates")
    os.system("sudo apt install sssd-ldap ldap-utils libsss-sudo")
    os.system("sudo install -m 600 /dev/null /etc/sssd/sssd.conf")
    os.system("sudo cp sssd.conf /etc/sssd/")
    os.system("sudo systemctl restart sssd")
    
def configure_nfs():
    print("\nConfiguring Autofs...\n")
    sleep(5)
    os.system("apt install autofs -y")
    os.system("mv /etc/auto.master /etc/auto.master.old")
    os.system("echo '/net /etc/auto.net' > /etc/auto.master")
    os.system("mkdir /net")
    os.system("ln -s /net /nfs")
    os.system("rm -r /home")
    os.system("ln -s /net/kato/store/home /home")
    print("\nrestarting autofs daemon...\n")
    sleep(5)
    os.system("service autofs reload")
    # add commands to configure nfs

def configure_nullmailer():
    print("\nConfiguring Nullmailer...\n")
    sleep(5)
    os.system("sudo apt install nullmailer mailutils -y")
    os.system("echo sysadmin@vast.uccs.edu > /etc/nullmailer/adminaddr")
    os.system("echo vast.uccs.edu > /etc/nullmailer/defaultdomain")
    os.system("echo mail.vast.uccs.edu > /etc/nullmailer/remotes")
    
    print("Testing the install")
    sleep(5)
    os.system("echo THIS IS A TEST | mail sysadmin@vast.uccs.edu")

def install_sysmon():
    print("\nInstalling sysmon tools")
    sleep(5)
    os.system("sudo apt install smartmontools")


# checks the euid if the user is root
def check_root() -> bool:
    if os.geteuid() != 0:
        return (False)
    else:
        return (True)

# updates the machine and installs the required drivers
def install_nvidia_drivers():
    print("\nPurging nvidia drivers")
    sleep(5)
    os.system("sudo apt remove --purge '^nvidia-.*’")
    os.system("sudo ubuntu-drivers autoinstall")

# installs gcc, g++ and cuda drives
def install_cuda_drivers():
    print("\nInstalling CUDA drivers...\n")
    sleep(5)
    os.system("sudo apt install nvidia-cuda-toolkit -y")


def help():
    print("Usage: configurator.py <switch>")
    print("Switches:")
    print("----------------------")
    print("-h: Displays this message")
    print("-g: GPU Install")
    print("-n: Normal Install")
    print("----------------------")
    print("Normal Install")

    # need to add other parts from ubuntu checklist
    print("----------------------")
    print("GPU Install")

    print("Nividia Drivers")
    print("CUDA Drivers")
    print("GPU-Burn")

# components installed when dealing with GPU server
def gpu_server_install():
    generic_server_install()
    install_nvidia_drivers()
    install_cuda_drivers()

# components installed when dealing with a regular server
def generic_server_install():
    update()
    configure_ldap_client()
    configure_nullmailer()
    configure_nfs()
    install_sysmon()

def main():
    check_sudo = check_root()

    # remove first commandline arg
    if(check_sudo == False):
        print("ERROR: Are you sudo?")
    else:         
        argumentList = sys.argv[1:]

        options = "hgn"
        long_options = ["help", "gpu", "normal"]

        try:
            # Parse arguments
            arguments, values = getopt.getopt(argumentList, options, long_options)


            # checking each argument
            for currentArgument, currentValue in arguments:
        
                if currentArgument in ("-h", "--help"):
                    help()
                
                elif currentArgument in ("-g", "--gpu"):
                    print("GPU Config Selected...")
                    sleep(5)
                    gpu_server_install()

                elif currentArgument in ("-n", "--normal"):
                    print("Normal Config Selected...")
                    sleep(5)
                    generic_server_install()

        except getopt.error as err:
            # output error, and return with an error code
            print(str(err))

if __name__ == '__main__':
    main()