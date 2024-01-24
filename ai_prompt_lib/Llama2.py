import asyncio
from llama_cpp import Llama


class Llama2:
    """! A class for generating responses from Llama2."""
    MODEL = Llama(model_path="./llama-2-7b-chat.Q4_K_M.gguf", verbose=False)
    # model = None
    def __init__(self, prompt: str, max_tokens: int = 1000) -> None:
        """The constructor for Llama2 class.
        Parameters:
            prompt (str): The prompt to generate a response from.
            max_tokens (int): The maximum number of tokens to generate.
        Returns:
            None
        """
        self.prompt = prompt
        self.max_tokens = max_tokens

        self.response = None

        # asyncio.create_task(self.generate_response())
        self.generate_response()

    # @staticmethod
    # def set_model(modelPath):
    #     Llama2.model = Llama(model_path=modelPath, verbose=False)


    def generation_done(self) -> bool:
        """Check if the generation is done.
        Returns:
            bool: True if the generation is done, False otherwise."""
        return self.response is not None

    def generate_response(self):
        """Generate a response from the model.
        """
        self.response = Llama2.MODEL(self.prompt, max_tokens=self.max_tokens,)
        print(self.response)
        print(type(self.response))

    def get_response(self) -> str:
        """Return the generated response.
        Returns:
            str: The generated response."""
        if not self.response:
            return ""

        return self.response["choices"][0]["text"]
    
    @staticmethod
    def load_model(modelPath):
        """Load the model.
        Parameters:
            modelPath (str): The path to the model.
        """
        Llama2.close_model()
        Llama2.MODEL = Llama(model_path=modelPath, verbose=False)

    @staticmethod
    def close_model():
        """Close the model."""
        del Llama2.MODEL