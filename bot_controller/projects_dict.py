def get_topic_dict(
    name: str,
    description: str,
    telegram_link: str,
    github_link: str,
    members: str,
) -> dict:
    """
    Returns a dictionary representing a topic.

    Args:
        name (str): The name of the topic.
        description (str): The description of the topic.
        telegram_link (str): The Telegram link of the topic.
        github_link (str): The GitHub link of the topic.
        members (str): The members of the topic.

    Returns:
        dict: The dictionary representing the topic.
    """
    topic_dict = {
        "name": name,
        "description": description,
        "telegram_link": telegram_link,
        "github_link": github_link,
        "members": members,
    }
    return topic_dict


projects = [
    get_topic_dict(
        "Talleres robótica",
        "Deseño de robot segueliñas en Rust para participar na OSWHDem 2024.",
        "https://t.me/c/1321437470/18057",
        "https://github.com/aindustriosa/RustyBugA",
        "Jorge, Pablo, David, Héctor",
    ),
    get_topic_dict(
        "Home Assistant",
        "Home assistant para Aindustriosa",
        "https://t.me/c/1321437470/17292",
        "-",
        "Sergio, Juan, Juan Carlos",
    ),
    get_topic_dict(
        "Multi Room Room Sound",
        "Proxecto para facer un sistema de son multiroom",
        "https://t.me/c/1321437470/17685",
        "-",
        "Jorge, Pablo, David, Héctor",
    ),
    get_topic_dict(
        "Branding",
        "Queremos dotar á asociación dunha “imaxe de marca” que faga que os socios, os patrocinadores e todas as persoas que entren teñan claro quen somos e que facemos.",
        "https://t.me/c/1321437470/18689",
        "-",
        "Bernardo, María, Manuel, Miguel, Jorge, Patricia, Luís",
    ),
    get_topic_dict(
        "electroCarro",
        "-",
        "https://t.me/c/1321437470/17263",
        "-",
        "Nacho, Dani",
    ),
    get_topic_dict(
        "FNQ2.eNemo",
        "-",
        "https://t.me/c/1321437470/17269",
        "-",
        "Nacho",
    ),
]
