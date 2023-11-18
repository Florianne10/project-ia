# Projet IA

## Installation

Instructions :

## Lancement

## Exemple d'utilisation

## Dépendances nécessaires

### Llama 2

### Stable Diffusion

## Auteurs

## License

pip install fire
pip install fairscale
pip install sentencepiece

https://www.nvidia.com/Download/index.aspx
sur linux : sudo apt-get install nvidia-driver-515

Disable Secure Boot:
Access UEFI/BIOS settings:

Restart your computer and enter the UEFI/BIOS settings. You usually do this by pressing a key (like Del, F2, or F10) during the boot process. The exact key depends on your computer's manufacturer.
Locate Secure Boot settings:

Once in the UEFI/BIOS settings, look for an option related to "Secure Boot." It may be under the "Boot" or "Security" section.
Disable Secure Boot:

Disable Secure Boot. Save the changes and exit the UEFI/BIOS.
Restart:

Restart your computer.

Install driver :
sudo apt install nvidia-driver-470

nvidia-smi

pip install torch torchvision torchaudio -U

Pour mettre à jour votre pilote NVIDIA sous Linux, vous pouvez utiliser la commande ubuntu-drivers. Voici les étapes générales :

Ouvrez un terminal.

Installez le paquet ubuntu-drivers si ce n'est pas déjà fait :

sudo apt-get update
sudo apt-get install ubuntu-drivers-common

Affichez les pilotes recommandés :

ubuntu-drivers devices
Installez le pilote recommandé :

sudo ubuntu-drivers autoinstall
Redémarrez votre système :

sudo reboot

nvidia-smi --gpu-reset
