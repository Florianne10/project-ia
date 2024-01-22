import asyncio
from llama_cpp import Llama

class Llama2Generator:
    def __init__(self, model_path: str, prompt: str, max_tokens: int = 100) -> None:
        self.model = Llama(model_path=model_path, verbose=False)
        self.prompt = prompt
        self.max_tokens = max_tokens

        self.response = None

        asyncio.create_task(self.generate_response())

    def generation_done(self) -> bool:
        return self.response is not None

    async def generate_response(self):
        self.response = self.model(self.prompt, max_tokens=self.max_tokens)

    def get_response(self) -> str:
        if not self.response:
            return ""

        return self.response["choices"][0]["text"]