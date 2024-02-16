import os
import json
from crewai import Agent, Task, Crew, Process
from langchain.tools import tool

import pickle

from thinkgpt.summarize import SummarizeMixin, SummarizeChain

from langchain.llms import Ollama
# ollama_llm = Ollama(model="zephyr")
# ollama_llm = Ollama(model="openhermes") # decent at coming up with comments
# ollama_llm = Ollama(model="openchat") # 
# ollama_llm = Ollama(model="orca2") # 
# ollama_llm = Ollama(model="mixtral") # biggest and slowest, usually pretty reliable

with open("D:/Unity Projects/Narramancer/Assets/Narramancer/Scripts/Nodes/AndNode.cs", 'r') as f:
   nodeScript = f.read()

print(nodeScript)

programmer = Agent(
  role='Unity Developer',
  goal='Analyze and summarize a C# script',
  backstory="""You are an expert Unity Developer and programmer with extensive experience writing C# and other programming languages. You have a knack for writing documentation.""",
  verbose=True,
  allow_delegation=False,
  llm = Ollama(model="openchat") 
)

document = Task(
  description=
  f"""The full text of the given script is as follows: \n{nodeScript}\n\n""" +
  """Describe the purpose of the given Node.""",
  agent=programmer,
)

crew = Crew(
  agents=[ programmer],
  tasks=[document],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

result = crew.kickoff()

print("######################")
print(result)
