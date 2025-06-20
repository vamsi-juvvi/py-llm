# Utility methods to visually separate output from logs
# displaying HTML and Markdown responses
import os
import logging
import json
from IPython.display import display, HTML, Markdown

#----------------------------------------------------------
#  Include something like this before your python cells
#----------------------------------------------------------
#  # Setup paths to our libs
#  import sys
#  from pathlib import Path
#  
#  sys.path.append(str(Path("../../libs/python/hillops").resolve()))
#  
#  # Import jupyter utils
#  import logging
#  from util import jupyter_util
#  from util.jupyter_util import DisplayHTML as jh
#  from util.jupyter_util import DisplayMarkdown as jm
#  
#  # Init jupyter env
#  jupyter_util.setup_logging(logging.WARN)
#  jupyter_util.ColabEnv.import_api_keys()
#----------------------------------------------------------
def setup_logging(level = logging.DEBUG):
     """
     Supply one of logging.INFO|DEBUG|WARN|ERROR
     """
     from importlib import reload
     import logging
     reload(logging)
     logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', 
                    level=level, 
                    datefmt='%I:%M:%S')


#--------------------------------------------------------------
# Expected to be run in a Jupyter environment (normal or Colab)
#--------------------------------------------------------------
class ColabEnv:
    @staticmethod
    def colab_keyval(key):
     """
     Checks colab for the specified key.
     Note that there is a checkbox in the Colab interface that explicitly 
          gives a notebook permission to access this. This has to be enabled on 
          for each key on a given notebook. Otw, this code will never see it.
     """
     keyval = None
     if 'google.colab' in str(get_ipython()):
          from google.colab import userdata
          logging.debug(f"Trying to fetch {key} from your secrets. Remember to make it available to this notebook")            
     
          if keyval := userdata.get(key):
               logging.debug(f"Found colab secret for {key}")
          else:
               logging.warning(f"Did not find colab secret for {key}")
     
     return keyval

     
    @staticmethod
    def colab_keyval_or_env(key):
         return ColabEnv.colab_keyval(key) or os.environ[key]
         
    @staticmethod
    def import_api_keys(keys):
     """
     Imports the various API keys from cloab's userdata.

     These are stored in colab secrets and you'll need to allow the notebook to access
     the keys explicitly on a key-by-key basis.
     """             
     for k in keys:
          if kv := ColabEnv.colab_keyval(k):               
               os.environ[k] = kv

     

#--------------------------------------------------------------
from enum import StrEnum
class TextAlign (StrEnum):
    DEFAULT = "justify"
    RIGHT = "right"
    LEFT = "left"

class DisplayHTML:
    """
    Collection of jupyter visualization methods
    """
    @staticmethod
    def color_box(txt, title=None, bg="pink", fg="black", align= TextAlign.DEFAULT):
        if title is not None:
            txt = f"<b>{title}</b><br><hr><br>{txt}"

        MARGIN_AMOUNT="100px"
        match align:
            case TextAlign.LEFT:        
                margin = f"margin-right:{MARGIN_AMOUNT};"
            case TextAlign.RIGHT:
                margin = f"margin-left:{MARGIN_AMOUNT};"
            case _:
                margin = ""

        display(HTML(f"<div style='border-radius:15px;padding:15px;{margin}text-align:{str(align)};background-color:{bg};color:{fg};'>{txt}</div>"))    
    
    @staticmethod
    def text(txt, bg=None, fg=None, align=None):
         bg = f"background-color:{bg}" if bg else ''
         fg = f"color:{fg}" if fg else ''
         align = f"text-align:{align}" if align else ''
         display(HTML(f"<p style='{bg};{fg};{align};'>{txt}</p>"))

#--------------------------------------------------------------
class DisplayMarkdown:
     @staticmethod
     def h(title:str, title_level:int|None=None):
          """
          Heading. 
          `title_level` defaults to 1
          """
          title_level = title_level if title_level else 1
          title_hashtrain = eval(f"\"#\"*{title_level}") if title_level > 1 else "#"
          DisplayMarkdown.md(f"{title_hashtrain} {title}")

     @staticmethod
     def json(jsn, indent=4):
          """
          Display JSON.
          If String      → displayed as is
          If Json object → Displayed with the optional indent
                           Optional indent defaults to 4
          """          
          DisplayMarkdown.md(
               DisplayMarkdown.json_fmt(jsn, indent)
          )
     
     @staticmethod
     def hr():
          """
          like the <hr> of HTML
          Draws a separator using the "----" Md
          """
          DisplayMarkdown.md("----")

     @staticmethod            
     def code(code_block_str:str, code_lang:str|None=None):
          """
          Display Markdown code
          code_lang defaults to empty which will simply produce a ```...``` block
          """          
          DisplayMarkdown.md(
               DisplayMarkdown.code_fmt(code_block_str, code_lang)
          )

     @staticmethod
     def md(markdown_text:str):
          """
          Display markdown formatted text
          """
          display(Markdown(markdown_text))

     @staticmethod
     def code_fmt(code_block:str, code_lang:str|None=""):
          return f"```{code_lang}\n{code_block}\n```"
     
     @staticmethod
     def json_fmt(jsn, indent=4):
          if not isinstance(jsn, str):               
               jsn = json.dumps(jsn, indent=indent)               

          return DisplayMarkdown.code_fmt(jsn, "json")
     