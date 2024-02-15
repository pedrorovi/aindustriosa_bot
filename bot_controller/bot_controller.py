import telebot
from .projects_dict import projects


class BotController:
    """
    This class represents a bot controller.
    """

    def __init__(self, bot_token: str | None = None):
        if not bot_token:
            raise ValueError("Bot token is not set in environment variables")
        self.bot = telebot.TeleBot(bot_token)

        self.commands = {
            "/start": "Starts the bot and sends a welcome message",
            "/help": "Provides help information",
            "/meetup": "Sends the meetup link",
            "/projects": "Sends the actual projects of the association and links to Telegram topics and GitHub",
            "/tools": "Sends the actual tools of the association",
        }

        self.tools = {
            "Electrónica": "Fuente de alimentación, osciloscopio, multímetro, estación de soldadura, microcontroladores.",
            "Impresión 3D": "Resina, ender, prusa.",
            "Láser": "-",
            "CNC": "-",
        }

        self.projects_str = "\n\n".join(
            f"Name: {project['name']}\nDescription: {project['description']}\nGitHub: {project['github_link']}\nTelegram: {project['telegram_link']}\nMembers: {project['members']}"
            for project in projects
        )

    def start(self):
        """
        Starts the bot and sets up message handlers.

        The bot will respond to the "/start" and "/help" commands by sending a welcome message.
        It will also echo back any other messages it receives.

        """

        @self.bot.message_handler(commands=["start"])
        def send_welcome(message):
            self.bot.reply_to(message, "Howdy, how are you doing?")

        @self.bot.message_handler(commands=["help"])
        def send_commands(message):
            commands_str = "\n".join(
                f"{cmd}: {desc}" for cmd, desc in self.commands.items()
            )
            self.bot.reply_to(message, commands_str)

        @self.bot.message_handler(commands=["meetup"])
        def send_meetup_link(message):
            link = "https://www.meetup.com/es-ES/aindustriosa/"
            self.bot.reply_to(message, f"Here is the link to the meetup: {link}")

        @self.bot.message_handler(commands=["projects"])
        def send_projects(message):
            self.bot.reply_to(message, self.projects_str)

        @self.bot.message_handler(commands=["tools"])
        def send_tools(message):
            tools_str = "\n\n".join(f"{cmd}: {desc}" for cmd, desc in self.tools.items())
            self.bot.reply_to(message, tools_str)

        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            self.bot.reply_to(message, message.text)

        self.bot.infinity_polling()
