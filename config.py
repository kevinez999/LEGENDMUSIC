from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_ALFABET", "session")
BOT_TOKEN = getenv("1805888447:AAEmvdnSM7uYrufgad_euRScEFirir59ddU")
BOT_NAME = getenv("BOT_ALFABET")
admins = {}
API_ID = int(getenv("5005292"))
API_HASH = getenv("44877054c7ecea9279d3bb6a8bd84c01")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
