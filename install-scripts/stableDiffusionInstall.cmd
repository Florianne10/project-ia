@REM git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git stable-diffusion-webui


curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S /D=%cd%\Miniconda3
del miniconda.exe


call %cd%\Miniconda3\Scripts\activate.bat
conda clean -ay
conda create -n ia-env python=3.10.6 anaconda -y
conda activate ia-env

@REM cd stable-diffusion-webui
@REM .\webui.bat --api --no-half-vae --no-half --nowebui --exit


exit