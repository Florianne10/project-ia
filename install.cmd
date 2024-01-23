@echo off

echo Ouverture de PowerShell...

start /wait "" .\install-scripts\stableDiffusionInstall.cmd

call .\.venv\Scripts\activate.bat

call pip install llama-cpp-python
call pip install requests
call pip install aiohttp
call pip install pillow

echo Script termine.
