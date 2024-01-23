@echo off
echo Ouverture de PowerShell...


@REM Executé install-script\stableDiffusionInstall.cmd
@REM start powershell -Command "& {Start-Process cmd -ArgumentList '/k .\install-scripts\stableDiffusionInstall.cmd' -PassThru -WindowStyle Normal; Start-Sleep -Seconds 5; Stop-Process -Name cmd -Force}"


start /wait "" .\install-scripts\stableDiffusionInstall.cmd


@REM start powershell -Command "& {Start-Process cmd -ArgumentList '/k echo Hello from CMD' -PassThru -WindowStyle Normal; Start-Sleep -Seconds 5; Stop-Process -Name cmd -Force}"

echo Script terminé.










@REM start : ouvrir une nouvelle fenêtre PowerShell
@REM -NoExit : empêche la fermeture automatique de la fenêtre PowerShell après l'exécution de la commande
@REM -Command :  spécifier la commande ou les commandes PowerShell à exécuter
@REM Start-Process : ouvrir une nouvelle fenêtre CMD avec l'argument /k
@REM -WindowStyle Normal : afficher la fenêtre CMD
@REM -PassThru : récupérer l'objet Process représentant la nouvelle fenêtre CMD
@REM Start-Sleep : créer une pause
@REM Stop-Process : fermer la fenêtre CMD en cours d'exe ; -Name pour spécifier le nom du process à arrêter, -Force pour effectuer l'arrêt du processus sans demander de confirmation à l'utilisateur
