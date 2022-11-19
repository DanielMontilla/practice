import os
import subprocess
from rich.text import Text
from rich.padding import Padding
from rich.panel import Panel
from rich.console import Console

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
PROBLEMS_DIR = os.path.join(ROOT_DIR, 'problems')
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')
CHOICES = ['python 🐍', 'rust 🦀', 'typescript 🌀']
AUTHOR = 'Daniel Montilla'
GIT_LINK = 'https://github.com/DanielMontilla'

PROBLEM_NAME_ID = '$PROB$'
URL_ID = '$URL$'
AUTHOR_ID = '$AUTH$'
GIT_ID = '$GIT$'
NO_URL_TEXT = '[TODO: add problem url]'

cns = Console()

# 🔧 UTILITY
def mkdir(path: str, at=PROBLEMS_DIR) -> str:
  res = os.path.join(at, path)
  if not os.path.exists(res):
    os.mkdir(res)
  return res

def format_name(name: str) -> str:
  return name.strip().lower().replace(' ', '_')

def get_template_content(ext: str, name: str, url: str | None, author: str=AUTHOR, git_link: str=GIT_LINK) -> str:
  with open(os.path.join(TEMPLATE_DIR, f'[sample].{ext}')) as f:
    return f.read().replace(
      PROBLEM_NAME_ID, name
    ).replace(
      URL_ID, url if url else NO_URL_TEXT
    ).replace(
      AUTHOR_ID, author
    ).replace(
      GIT_ID, git_link
    )

# 🏁 CREATION ENTRY POINTS
def create_rs(name: str, url: str | None, prob_dir: str) -> str:
  subprocess.run([
    'cargo',
    'init',
    '--name', format_name(name),
    '--lib',
    '--quiet',
    '--vcs', 'none',
    prob_dir
  ])
  
  file_conent = get_template_content('rs', name, url)
  file_path = os.path.join(prob_dir, 'src', 'lib.rs')
  
  with open(file_path, 'w') as f:
    f.write(file_conent)
  
  return 'cargo test'
  
def create_ts(name: str, url: str | None, prob_dir: str) -> str:
  file_conent = get_template_content('ts', name, url)
  file_path = os.path.join(prob_dir, 'main.ts')
  
  with open(file_path, 'w') as f:
    f.write(file_conent)

  return 'deno test'

def create_py(name: str, url: str | None, prob_dir: str) -> str:
  file_content = get_template_content('py', name, url)
  file_path = os.path.join(prob_dir, 'main.py')
  
  with open(file_path, 'w') as f:
    f.write(file_content)
    
  return 'python main.py'

def setup(name: str, url: str | None, lang: str):
  subprocess.run(["clear"])
  prob_dir = mkdir(format_name(name))
  try:
    test_command: str = None
    color: str = None
    match lang:
      case 'python 🐍':
        test_command = create_py(name, url, prob_dir)
        color = 'dark_sea_green4'
      case 'rust 🦀':
        test_command = create_rs(name, url, prob_dir)
        color = 'dark_orange3'
      case 'typescript 🌀':
        test_command = create_ts(name, url, prob_dir)
        color = 'slate_blue1'
      case _:
        raise
    
    cns.print( # Success text!
      '\n' + 
      '[bold][spring_green3]successfully generated problem setup [/][/]' +
      '[italic]with[/] ' + f'[{color}][bold]{lang[:-2]}[/][/]!' + '\n' +
      f'[dark_magenta]@[/] [white on grey23]{prob_dir}[/]' + '\n' * 2 +
      f'test solution by running `[grey11 on grey58][italic][bold]{test_command}[/][/][/]`',
      justify='center'
    )
    
  except:
    # TODO: print error
    cns.print(
      '\n' +
      '[red][bold]something went wrong!' +
      '\n',
      justify='center'
    )