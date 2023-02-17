from pathlib import Path

from dotenv import load_dotenv

import {{cookiecutter.package_name}}

PROJECT_BASE = Path({{cookiecutter.package_name}}.__file__).parent
DOTENV_FILE_PATH = PROJECT_BASE / '.env.prod'

load_dotenv(DOTENV_FILE_PATH)
