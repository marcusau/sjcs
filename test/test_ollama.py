
import sys
from pathlib import Path
from ollama import Client,AsyncClient
from dataclasses import dataclass
import asyncio

sys.path.append(str(Path(__file__).parent.parent))
from config import config,model_para

client = Client(host=config.base_url)


msg={ 'role': 'user','content': 'how to deal with the trough of life?'}

##### completion
# chat_completion = client.chat(
#      messages=[msg],
#      model=config.model_name,
#      options=model_para)

# print(chat_completion['message']['content'])


#### stream ####
async def async_chat():
  for part in client.chat(model=config.model_name,options=model_para, messages=[msg], stream=True):
    print(part['message']['content'], end='', flush=True)
  
asyncio.run(async_chat())