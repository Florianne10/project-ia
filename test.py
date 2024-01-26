
from ai_prompt_lib.StableDiffusion import StableDiffusion
from ai_prompt_lib.Llama2 import Llama2

import asyncio


# /// GET USER INPUTS
topic = input("Enter a Story topic (In ENGLISH): ")

print("__PARAMETERS FOR PICTURE GENERATION__")

negativePrompt = input("Enter a negative prompt (In ENGLISH, press enter to skip): ").strip()

style = input("Enter a style (Concept art, Cyberpunk, Cartoon, Horror) or press enter to skip: ").strip()

loras = {}

while True:
    lora = input("Enter a lora name (press enter if you don't want to add more loras): ").strip()
    if (lora == ""):
        break
    
    while True:
        try:
            loraWeight = float(input("Enter a weight for this lora (0.0 to 1.0): ").strip())
            if (loraWeight < 0.0 or loraWeight > 1.0):
                raise ValueError
            break
        except ValueError:
            print("Invalid weight. Try again.")
    loras[lora] = loraWeight

    print("Curent loras: " + str(loras))

# /// GENERATE STORY
print("Generating story...")

promptStory = Llama2("Generate a SHORT story about \"" + topic + "\". Tell the story:")



print("Generation done")

# /// GENERATE PICTURE PROMPT

print("\n////Generation stable diffusion prompt...")

stableDiffusionPrompt = Llama2("Write a short prompt to illustrate this story with a picture generation IA. Describe details of the story characters: " + promptStory.get_response() + "\n\nPrompt: ")



print("Generation done")

# /// SAVE STORY

story = "______Story______\n"  + promptStory.prompt + "\n" + promptStory.get_response()

# Save story
with open("output.txt", "w") as text_file:
    text_file.write(story)

Llama2.close_model()

# /// GENERATE PICTURE

async def generation():
    """!Generate a response from the model."""
    stableDiffusionPromptStr = (style != "" and "(" + style + " style)" or "") +stableDiffusionPrompt.get_response()
    
    prompt = StableDiffusion(stableDiffusionPromptStr, quality=20, negative_prompt=negativePrompt, loras=loras)#, loras={"Tintin": 1, "Tintin_v1": 1})
    
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

    print()

try:
    asyncio.run(generation())
except Exception as e:
    pass

