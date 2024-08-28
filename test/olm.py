
from ollama import AsyncClient
import ollama
import asyncio

# async def gen(prompt):
#     async with AsyncClient() as client:
#         async for part in await client.generate(model="phi3", prompt=prompt, stream=True):
#             print(part['response'], end=" ", flush=True)

# asyncio.run(gen("Hi"))


# import ollama as olm
# from string import Template
# import asyncio

async def gen(prompt):
    async for part in await AsyncClient().generate(model="phi3",prompt=prompt):
        print(part['response'], end=" ",flush=True)

asyncio.run(gen("Hi"))
# for part in ollama.generate(model="phi3",prompt="hi")["response"]:
#     print(part,end=" ", flush=True)
# res = ollama.generate(model="phi3",prompt="hi")
# print(res['response'])

# PROMPT_TEMPLATE = Template(
#     """Fix all typos and casing and punctuation in this text, but preserve all new line characters:

# $text

# Return only the corrected text, don't include a preamble.
# """
# )
# prompt = PROMPT_TEMPLATE.substitute(text="wrote an pyhtn cade")

# fix = ollama.generate(model="phi3",prompt=prompt)
# print(fix)