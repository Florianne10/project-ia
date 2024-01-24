import asyncio
from llama_cpp import Llama


class Llama2:
    MODEL = Llama(model_path="./llama-2-7b-chat.Q4_K_M.gguf", verbose=False)
    # model = None
    def __init__(self, prompt: str, max_tokens: int = 1000) -> None:
        self.prompt = prompt
        self.max_tokens = max_tokens

        self.response = None

        # asyncio.create_task(self.generate_response())
        self.generate_response()

    # @staticmethod
    # def set_model(modelPath):
    #     Llama2.model = Llama(model_path=modelPath, verbose=False)


    def generation_done(self) -> bool:
        return self.response is not None

    def generate_response(self):
        self.response = Llama2.MODEL(self.prompt, max_tokens=self.max_tokens,)
        print(self.response)
        print(type(self.response))

    def get_response(self) -> str:
        if not self.response:
            return ""

        return self.response["choices"][0]["text"]
    
    @staticmethod
    def load_model(modelPath):
        Llama2.close_model()
        Llama2.MODEL = Llama(model_path=modelPath, verbose=False)

    @staticmethod
    def close_model():
        del Llama2.MODEL