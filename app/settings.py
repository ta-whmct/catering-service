import pathlib
import os
from dotenv import load_dotenv

# parser = argparse.ArgumentParser()
# parser.add_argument("--env", required=True)
# args = parser.parse_args()

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# load_dotenv(f"{BASE_DIR}/envs/.{args.env}.env")
load_dotenv(f"{BASE_DIR}/envs/.dev.env")
database_uri = os.getenv("database_uri", "sqlite:///database.sqlite3")
