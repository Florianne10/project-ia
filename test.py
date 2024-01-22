
from ai_prompt_lib.StableDiffusion import StableDiffusion

import asyncio


async def generation():
    prompt = StableDiffusion("""parapente (parapente,mountain,sunset)""", quality=20, loras={"Tintin": 1, "Tintin_v1": 1})
    
    print("Generating...")

    while not prompt.generation_done():
        progress = await prompt.get_progress()

        if ("progress" in progress):
            progressIntPercent = round(float((progress['progress'])) * 100)
            print("Progress: "+ str(progressIntPercent) + "%")
        await asyncio.sleep(0.5)

    print("Generation done")
    prompt.get_image().save('output.png')

asyncio.run(generation())
