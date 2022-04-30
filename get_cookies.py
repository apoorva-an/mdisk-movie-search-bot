# (c) @Magic121

from core.login import mdisk_login

PDisk_DB = {}


async def get_cookies(username: str, password: str) -> str:
    if not MDisk_DB:
        user_id, cookies = await mdisk_login(username, password)
        Mdisk_DB["cookies"] = cookies
        Mdisk_DB["user_id"] = user_id
        Mdisk_DB["username"] = username
        MDisk_DB["password"] = password

    return MDisk_DB["cookies"]


async def set_cookies(data: dict):
    MDisk_DB["username"] = data["username"]
    MDisk_DB["password"] = data["password"]
    MDisk_DB["user_id"] = data["user_id"]
    MDisk_DB["cookies"] = data["cookies"]
