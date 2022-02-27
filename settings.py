import os

import dotenv

dotenv.load_dotenv()


class Settings:
    SERVER = os.getenv('SERVER')