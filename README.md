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
   git clone https://github.com/Florianne10/project-ia.git
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
   Pour ça regarder la partie "Modèles" ci-dessous.

   > ATTENTION: Pour le script test.py, le modèle `llama-2-7b-chat.Q4_K_M.gguf` doit être à la racine du projet, ce model est indispensable pour test.py

### Model

#### LLAMA 2

1. Téléchargez le modèle de votre choix des IA à partir de .

   Le modèle qui est utilisé dans le script test.py est le suivant :
   [llama-2-7b-chat.Q4_K_M](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf)

   Vous pouvez aussi trouver d'autres version de ce modèle ici :
   [Lise models Llama2 7b](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)

   Vous pouvez aussi trouver d'autres modèles ici :
   [HuggingFace](https://huggingface.co)

   > Attention à ne prendre que des modèles qui ont l'extension .gguf

2. Une fois le modèle téléchargé, placez le à la racine du projet.

#### STABLE DIFFUSION

##### Téléchargement des Lora

1. Téléchargez les Lora de votre choix pour Stable Diffusion

   Vous pouvez trouver les Lora ici :

   - [HuggingFace](https://huggingface.co)
   - [Civitai](https://civitai.com)

2. Une fois les Lora téléchargés, placez les dans le dossier `stable-diffusion-webui\models\Lora`
3. Pour utiliser des loras avec `ai_prompt_lib` rien de plus simple:

   ```python
   prompt = StableDiffusion("Tintin at the beach", loras={"Tintin": 1, "Tintin_v1": 1})

   lora = Lora("nom_du_lora")
   ```

   > Les clés du dictionnaire sont les noms des loras et les valeurs sont les poids des loras

##### Téléchargement des modèles

> Actuellement, le projet ne supporte que l'ajout de Lora pour Stable Diffusion, l'ajout de modèle sera disponible dans une prochaine version

## Lancement

Pour lancer le projet, utilisez la commande suivante:

1. Lancer le serveur stable diffusion

   Allez à la racine du dépot dans un terminal et lancez les commandes suivantes:

   ```shell
   cmd.exe
   %UserProfile%\Miniconda3LLMFF\Scripts\activate.bat
   conda activate ia-env
   cd stable-diffusion-webui
   .\webui.bat --api --no-half-vae --no-half --nowebui --port=5555
   ```

   Vous gardez ce terminal ouvert durant toute l'utilisation du projet

   > ATTENTION, si vous n'avez pas de carte graphique ou que votre carte graphique n'est pas compatible avec CUDA, vous devez remplacer `--skip-torch-cuda-test`

2. Lancer un script d'un projet qui utilise ai_prompt_lib
   Ouvrez un terminal (cmd ou powershell) et lancez les commandes suivantes (depuis la racine du dépot):

   ```shell
   .\.venv\Scripts\activate
   python test.py
   ```

   A la fin de l'exécution du script, vous trouverez une image, output.png, et un fichier texte, output.txt, représentant une histoire et son illustration.

   > Si vous souhaitez lancer votre propre script ils suffit de remplacer `test.py` par le nom de votre script

## Exemple de génération d'histoire

Pour voir des exemples de génération d'histoire, vous pouvez regarder le dossier `examples` qui contient des reusltats de génération d'histoire.

## Documentation

Pour générer la documentation:

```
doxygen Doxyfile
```

## Auteurs

- Florian GRASSER
- Elise MARQUE
- Pierre HEN
- Nathan MEHL

## License

Ce projet est sous licence ??????????. Consultez le fichier LICENSE pour plus de détails.
