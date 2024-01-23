# Projet IA

Ce projet vise à créer un framework sur Github réutilisable par d'autres développeurs, pour utiliser Stable diffusions et Llama2 afin de les utiliser pour générer un titre, une image et une histoire en fonction d'un prompt.
Nous devions créer une API pour qu'un développeur puisse l'intégrer dans son application.
Nous avons créé une librairie python qu'on peut exploiter.

> ATTENTION : Ce projet ne fonctionne que sur Windows

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système:

### Python

- **Windows:**
  Vous pouvez installer Python sur Windows en suivant les instructions fournies [ici](https://kinsta.com/fr/base-de-connaissances/installer-python/#windows-1).

- Autre prochainement

### Git

- **Windows:**
  Vous pouvez installer Git pour Windows en suivant les instructions disponibles [ici](https://gitforwindows.org/).

- Autre prochainement

### Anti-virus

- Assurez-vous que votre antivirus n'interfère pas avec l'exécution du projet.
- Exemple pour AVG : désactiver l'antivirus
  - Menu > Paramètre > Protection basique > désactiver et Protection complète > agent contre l'accès distant à désactiver

### Visual Studio C++

- Installez Visual Studio avec le "Desktop development with C++". Vous pouvez télécharger Visual Studio [ici](https://visualstudio.microsoft.com/fr/vs/community/).

## Installation

Suivez les étapes ci-dessous pour installer le projet:

### Instructions

1. Clonez ce dépôt en utilisant la commande:
   ```bash
   git clone https://github.com/nom-utilisateur/projet-ia.git
   ```

2. Naviguez vers le répertoire du projet:
   ```bash
   cd projet-ia
   ```

3. Exécutez le script d'installation:

```
  .\install.cmd
```

4. Télécharger les modèles et les loras.
   cf voir partie Model

### Model

1. Téléchargez le modèle de votre choix des IA à partir de [HuggingFace](https://huggingface.co).

**Llama2**
[llama-2-7b-chat.Q4_K_M](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf)
[Liste Llama2](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)

2. Extrayez le contenu du modèle dans le répertoire du projet.

## Lancement

Pour lancer le projet, utilisez la commande suivante:

1. Placez-vous à la racine du dépôt.
2. Effectuez les commandes suivantes, une par une:

```
cmd.exe
%cd%\Miniconda3\Scripts\activate.bat
conda activate ia-env
cd stable-diffusion-webui
.\webui.bat --api --no-half-vae --no-half --port=5555
```

## Exemple d'utilisation

Voici un exemple d'utilisation basique du projet:

## Dépendances nécessaires

Le projet dépend des bibliothèques suivantes:

### Llama 2

### Stable Diffusion

## Auteurs

- Florian GRASSER
- Elise MARQUE
- Pierre HEN
- Nathan MEHL

## License

Ce projet est sous licence ??????????. Consultez le fichier LICENSE pour plus de détails.
