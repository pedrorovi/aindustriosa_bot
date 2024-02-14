from bot_controller.bot_controller import BotController
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv(".env")
    bot_token = os.getenv("BOT_TOKEN")

    controller = BotController(bot_token)
    controller.start()
