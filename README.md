# py-llm

A short series on developing tool-calling from scratch in python.  I had used these as an exercise in exploring tool-calling and moving the logic into a rust code-base. The sections below show
 - Medium articles
 - development branches on the [py-llm](https://github.com/vamsi-juvvi/py-llm) repo that backs the articles
 - All images inside the medium articles were built using [plantuml]https://plantuml.com/)  except for the timelines which were built using [mermaid](https://mermaid.js.org/)
   - I use both plantuml and mermaid via their vscode extensions and use them inline in my markdown docs till I need to export the docs. When exporting, I use the extension functionality to export the images to png and then insert links in the markdown.
   - I run a local plantuml server via docker on one of my WSL distros and point the vscode extension to that URL instead of the public plantuml server.

## Part 1 - Better dev tooling via Jupyter utils 
 - The medum article [Developing LLM Tool-calling - 1 - Structure and Utilities](https://medium.com/@juvvij/llm-tool-calling-1-code-structure-and-jupyter-utilities-26ff52f80a59)
 - The code is developed under the [py-llm @ jupyter_utils](https://github.com/vamsi-juvvi/py-llm/tree/jupyter_utils) branch and merged to main.

## Part 2 - Importing libs, OpenAI Utils and Colab Secrets
 - The medum article [Developing LLM Tool-calling - 2 - Importing libs, OpenAI Utils and Colab Secrets](https://medium.com/@juvvij/llm-tool-calling-2-importing-libs-openai-utils-and-colab-secrets-252b5635dd20)
 - The code is developed under the [py-llm @ 2_lib_use_openai_and_colab](https://github.com/vamsi-juvvi/py-llm/tree/2_lib_use_openai_and_colab) branch and merged to main. 

## Part 3 - Foundations of LLM tool calling

- The medum article [LLM Tool-calling — 3 — Developing LLM tools](https://medium.com/@juvvij/llm-tool-calling-3-developing-llm-tools-13008f4341a6)
 - The code is developed under the [py-llm @ 3_llm_tools_and_support](https://github.com/vamsi-juvvi/py-llm/tree/3_llm_tools_and_support) branch and merged to main. 

## Part 4 - ReAct loops

- The medum article LLM Tool-calling — 4 — Developing the ReAct loop](https://medium.com/@juvvij/llm-tool-calling-4-developing-the-react-loop-438f6b9dad7b)
 - The code is developed under the [py-llm @ 4_tools_react](https://github.com/vamsi-juvvi/py-llm/tree/4_tools_react) branch and merged to main. 
