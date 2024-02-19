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

result = ""

directory = "D:/Unity Projects/Narramancer/Assets/Narramancer/Scripts/Nodes"

excludedNodes = ["AbstractCallMethodOnSpecificTypeRunnableNode", "AbstractCallMethodOnSpecificTypeValueNode", "AbstractDynamicMethodRunnableNode", "AbstractDynamicMethodValueNode", "AbstractInstanceInputChainedRunnableNode", "AbstractInstanceInputNode", "AbstractInstanceInputRunnableNode"]

programmer = Agent(
role='Unity Developer',
goal='Analyze and summarize a C# script',
backstory="""You are an expert Unity Developer and programmer with extensive experience writing C# and other programming languages. You have a knack for writing documentation.""",
    verbose=True,
    allow_delegation=False,
    llm = Ollama(model="openchat") 
    )

for path in os.listdir(directory):
    path = os.path.join(directory, path)

    if not os.path.isfile(path):
        continue
    if path.endswith(".meta"):
        continue

    with open(path, 'r') as f:
        nodeScript = f.read()

    basename = os.path.basename(path)
    filename = os.path.splitext(basename)[0]

    if filename in excludedNodes:
        continue

    document = Task(
    description=
        f"""The full text of the given script is as follows: \n{nodeScript}\n\n""" +
        f"""The class ultimately extends from the Node class, which defines a unit in a flow-based system for game flow and logic called Narramancer. Where the code referes to an instance, it is talking about a NounInstance. Fields with the [SerializeField] field can be considered public. Fields with the [Input] attribute are input ports for the node. Fields with the [Output] attribute are output ports for the node. Do NOT include the description of these attributes in your answer. Your answer must NOT include the description of Narramancer in your answer. Your answer must NOT include any description of other Nodes in your answer. When referring to the developer, use second-person perspective, referring to them as 'you'. Describe the inputs and outputs of the Node and its main purpose. Your answer must start with 'This node '.""",
        agent=programmer,
        )

    crew = Crew(
        agents=[ programmer],
        tasks=[document],
        verbose=2, # You can set it to 1 or 2 to different logging levels
        )

    description = crew.kickoff()

    print("######################")
    print(description)

    section_format = f"""
    <div class="section">
        <h2 id="{filename.lower()}">{filename}</h2>
        <p>{description}</p>
    </div>
    """

    result = result + "\n" + section_format

    with open("./nodes_description_v4.txt", 'w') as f:
        f.write(result)

    break