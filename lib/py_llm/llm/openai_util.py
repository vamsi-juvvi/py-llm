import os
import logging
import openai
from py_llm.util.jupyter_util import ColabEnv

# Works in both Colab and regular/VSCode
openai.api_key = ColabEnv.colab_keyval_or_env("OPENAI_API_KEY")

#-------------------------------------------------------------------------------------
def get_completion(prompt, tools, model="gpt-4o-mini", temperature=0) -> str:
    """
    Returns the one-shot completion of a simple prompt (no tools)
    as a string response.
    """
    chat_history = [{"role":"user", "content":prompt}]
    response = get_response(chat_history, tools, model, temperature)    
    return response.choices[0].message.content

#-------------------------------------------------------------------------------------
def get_response(chat_history, tools, model="gpt-4o-mini", temperature=0):
    """
    Returns the completion given a chat_history
    """    
    return openai.chat.completions.create(
        model=model,
        messages=chat_history,
        tools=tools,
        temperature=temperature)

#-------------------------------------------------------------------------------------
def chat_history_append_response(chat_history, response):
    msg = response.choices[0].message
    chat_history.append( {
        "role" : msg.role,
        "content" : msg.content
    })

    return chat_history

#-------------------------------------------------------------------------------------
def chat_history_append_user_msg(chat_history, content):    
    chat_history.append( {
        "role" : "user",
        "content" : content
    })

    return chat_history