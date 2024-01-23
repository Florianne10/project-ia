
from ai_prompt_lib.StableDiffusion import StableDiffusion
from ai_prompt_lib.Llama2 import Llama2
import time

import asyncio


print("Loading models...")
# Llama2.set_model("./mistral-7b-v0.1.Q2_K.gguf")


topic = input("Enter a Story topic: ")

print("Generating story...")

promptStory = Llama2("Generate a SHORT story about \"" + topic + "\". Tell the story:")



print("Generation done")
print(promptStory.get_response())

print("\n////Generation stable diffusion prompt...")

stableDiffusionPrompt = Llama2("Write a short prompt to illustrate this story with a picture generation IA. Describe details of the story characters: " + promptStory.get_response() + "\n\nPrompt: ")
# stableDiffusionPrompt = Llama2("Describe in details characters & landspace of this story: " + promptStory.get_response() + "\n\nPrompt: ")



print("Generation done")

print(stableDiffusionPrompt.get_response())

Llama2.close_model()

async def generation():
    prompt = StableDiffusion(stableDiffusionPrompt.get_response(), quality=20)#, loras={"Tintin": 1, "Tintin_v1": 1})
    
    print("Generating picture...")

    while not prompt.generation_done():
        progress = await prompt.get_progress()

        if ("progress" in progress):
            progressIntPercent = round(float((progress['progress'])) * 100)
            print("Progress: "+ str(progressIntPercent) + "%")
        await asyncio.sleep(0.5)

    print("Generation done")
    prompt.get_image().save('output.png')


    print("Done")

    print("______Story______\n"  + promptStory.prompt + "\n" + promptStory.get_response())

try:
    asyncio.run(generation())
except Exception as e:
    pass

