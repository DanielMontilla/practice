from definitions import setup, CHOICES
from questionary import text, select
import subprocess
import re

subprocess.run(["clear"])

name = text(
  'What\'s the name of the problem?:',
  validate=lambda name: True if re.match('^[a-zA-Z0-9 ]*$', name) != None and len(name) > 0 else 'invalid name' 
).ask()

url = text('Problem\'s url (none):').ask()
url = url if url != '' else None

lang: str = select(
  'Which languaje would you like to use?:',
  pointer='👉',
  use_jk_keys=True,
  instruction=False,
  choices=CHOICES
).ask()

setup(name, url, lang)