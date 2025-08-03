from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://jpcdn.it/img/small/8873a0259822e61d4bf3172fe56011e5.png")
START_IMG = getenv("START_IMG", "https://jpcdn.it/img/small/978de18142b816854249ca6cc2bbaba2.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/chihiroSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Espada_Org")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7942723471").split()))


FAILED = "https://jpcdn.it/img/small/9039661b6b6aab3193a132a5b7a0723c.jpg"
