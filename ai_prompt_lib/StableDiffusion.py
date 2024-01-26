import requests
import io
import base64
from PIL import Image
import asyncio
import aiohttp

"""Global variables for StableDiffusion."""
port = 5555

LOCAL_STABLE_DIFFUSION_URL = "http://127.0.0.1:" + str(port)

class StableDiffusion:
    """!A class for generating responses from StableDiffusion."""
    def __init__(self, prompt:str, quality : int = 20, negative_prompt : str = "", loras : dict[str, float] = {}) -> None:
        """The constructor for StableDiffusion class.
        Parameters:
            prompt (str): The prompt to generate a response from.
            quality (int): The quality of the generation.
            negative_prompt (str): The negative prompt to use.
            loras (dict[str, float]): The loras to use.
        Returns:
            None
        """
        loras_str = "".join(map(lambda x: f'<lora:{x[0]}:{x[1]}>', loras.items()))

        self.prompt = prompt + loras_str

        self.quality = quality

        self.negative_prompt = negative_prompt

        self.started = False

        self.json_response = None
        self.image = None

      
        asyncio.create_task(self.generate_image())

    @staticmethod
    def server_is_running():
        """Check if the server is running."""
        try:
            response = requests.get(url=f'{LOCAL_STABLE_DIFFUSION_URL}/sdapi/v1/progress')
            return True
        except:
            return False
        

    def generation_done(self) -> bool:
        """Check if the generation is done.
        Returns:
            bool: True if the generation is done, False otherwise."""
        return self.json_response != None

    async def generate_image(self):
        """Generate a response from the model."""
        assert(not self.started, "Already generating")
        self.started = True

        while not self.server_is_running():
            await asyncio.sleep(0.5)

        payload = {
            "prompt": self.prompt,
            "negative_prompt": self.negative_prompt,
            "steps": self.quality,
            "sampler_index": "Euler a"
        }

        async with aiohttp.ClientSession() as session:
            response = await session.post(url=f'{LOCAL_STABLE_DIFFUSION_URL}/sdapi/v1/txt2img',
                                json=payload)
            self.json_response = await response.json()

    def get_image(self) -> Image:
        """Return the generated response.
        Returns:
            Image: The generated response."""
        if not self.image:
            self.image = Image.open(io.BytesIO(base64.b64decode(self.json_response['images'][0])))

        return self.image
    
    async def get_progress(self):
        """Return the progress of the generation."""
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(url=f'{LOCAL_STABLE_DIFFUSION_URL}/sdapi/v1/progress')
                return await response.json()
        except:
            return {"progress": "0"}

