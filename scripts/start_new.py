import re
from typing import List, Tuple
from rich.console import Console
from definitions import *

cns = Console()

def mkdir(path: str) -> bool:
  if not os.path.exists(path):
    os.mkdir(path)
    return True
  else:
    return False
  
  
def new_rs(name: str, url: str | None):
  path = os.path.join(PROBLEMS_DIR, name)
  mkdir(path)
  os.system(f'cargo init --name {name} --lib --quiet --vcs none {path}')
  lib_path = os.path.join(path, 'src', 'lib.rs')
  
  with open(lib_path, "w") as f:
    f.write(DEF_RS_FILE(url))
    


def new_ts(name: str, url: str | None):
  pass

def new_py(name: str, url: str | None):
  path = os.path.join(PROBLEMS_DIR, name)
  mkdir(path)
  
  main_path = os.path.join(path, 'main.py')
  
  with open(main_path, "w") as f:
    f.write(DEF_PY_FILE(url))

def menu(options: List[Tuple[str, str]]) -> str | None:
  for (i, [s, n]) in enumerate(options):
    cns.print(f'[bold][grey70][{i + 1}][/][/] [white][normal]{s}[/][/]')
  
  selection = input()
  
  try:
    selection = int(selection) - 1
    
    if selection < 0 or selection > len(options) - 1:
      raise
    
    return options[selection][1]
  except:
    cns.print('[red]invalid option try again!')
    return None

def start():
  
  cns.line()
  cns.print('[bold]Starting a new Problem![/]', justify="center")
  
  # getting problem name
  while True:
    cns.print('[italic]problem name[/]: ', end='')
    name = input().strip().lower().replace(' ', '_')
    path = os.path.join(PROBLEMS_DIR, name)
    
    if not bool(re.match('^[a-z0-9_]*$', name)):
      cns.print(f'[red]{name} is not a valid problem name[/]', new_line_start=True)
    elif os.path.exists(os.path.join(PROBLEMS_DIR, name)):
      cns.print(f'[red]{name} already exists[/] [blue]@[/] {path} ', new_line_start=True)
    else:
      break
  
  # TODO make sure its valid url
  cns.print('[italic]problem url[/] [dim](default: none)[/]: ', end='')
  url = input()
  url = None if url == '' else url

  cns.print('[italic]select desired language:[/]')

  language = None
  
  while True:
    language = menu([
      ('🐍 [green]pyhton[/]', 'py'),
      ('🦀 [orange1]rust[/]', 'rs'),
      ('🌀 [blue]typescript[/]', 'ts'),
    ])
    
    if language != None:
      break
  
  match language:
    case 'ts':
      raise 'typescript not supported yet sorry :('
    case 'rs':
      new_rs(name, url)
    case 'py':
      new_py(name, url)
    case _:
      cns.print(f'lang {language} not suported')

  cns.print(f'\n[bold][green]files genreated succefully![/][/] [blue]@[/] {path} ')
  
  
start()