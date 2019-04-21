import os

from app import create_app
from dotenv import load_dotenv

# .env
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.environ.get("FLASK_CONFIG") or "default")

if __name__ == "__main__":
    app.run()