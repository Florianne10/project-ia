git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git stable-diffusion-webui


curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S /D=%UserProfile%\Miniconda3LLMFF
del miniconda.exe


call %UserProfile%\Miniconda3LLMFF\Scripts\activate.bat
call conda create -n ia-env python=3.10.6 anaconda -y
call conda activate ia-env

cd stable-diffusion-webui
call .\webui.bat --api --no-half-vae --no-half --nowebui --exit

cd ..

python -m venv .venv

exit