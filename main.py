import sys
sys.path.insert(0, './app')
from dotenv import load_dotenv
load_dotenv(dotenv_path='./config/env')
import app

if __name__ == '__main__':
  print(app.return_ok())
  print(app.return_secret_env())
