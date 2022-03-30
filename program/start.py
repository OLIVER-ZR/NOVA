from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    ASSISTANT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **مرحبا عزيزي ↤ {message.from_user.mention()} !**\n
🤖 **[𝐒𝐄𝐋𝐕𝐀 𝐌𝐔𝐒𝐈𝐂 🎶](https://t.me/SO_SELVA) **
**⌯ انا بوت  استطيع تشغيل الموسيقي والفيديو في محادثتك الصوتية**

⌯ تعلم طريقة تشغيلي واوامر التحكم بي عن طريق  » 📚 اوامر التشغيل !

⌯ لتعلم طريقة تشغيلي بمجموعتك اضغط علي » ❓طريقة التفعيل !
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌯ 𝐒𝐄𝐋𝐕𝐀 𝐌𝐔𝐒𝐈𝐂 🎶 ⌯",
                        url=f"https://t.me/SO_SELVA",
                    )
                ],
                [InlineKeyboardButton("⌯  ❓ طريقة التفعيل ⌯", callback_data="cbhowtouse")],
                [InlineKeyboardButton("⌯  الاوامر بالعربي ⌯", callback_data="cbvamp")],                 
                [
                    InlineKeyboardButton("⌯ 📚 اوامر التشغيل ⌯ ", callback_data="cbcmds"),
                    InlineKeyboardButton("⌯ الــمــطــور ⌯", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "⌯ جروب البوت ⌯", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "⌯ قناة البوت ⌯", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⌯ اضافه البوت اللي مجموعتك ⌯", url="https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", "لسورس", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("• تيمو •", url=f"https://t.me/tt_t_4"),
                InlineKeyboardButton("• ليدو •", url=f"https://t.me/J0KER7x"),
            ],
                [       
                    InlineKeyboardButton(
                        "⌯ 𝐒𝐄𝐋𝐕𝐀 𝐌𝐔𝐒𝐈𝐂 🎶 ⌯", url=f"https://t.me/SO_SELVA"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "⌯ اضافه البوت اللي مجموعتك ⌯", url="https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ]
        ]
    ) 

    alive = f"**⌯ اهلا بك يا  {message.from_user.mention()}   \n ⌯ في سورس سيلفا ميوزك 🎵 الجمدان ❤️ \n ⌯ لو عايز تنصيب بوت ميوزك بأسعار حلوة  كلمنا  من هنا ⬇️ ** "

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["لمطور", "طور"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10bfc5e7d6ab441832a65.jpg",
        caption=f"""**⌯ مطورين سورس سيلفا ميوزك 🎵**""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓆩 آݪــمــبــرمــج تيمو 𓆪", url=f"https://t.me/tt_t_4"),
            ],
            [
                InlineKeyboardButton("𓆩 آݪــمــبــرمــج ݪــيدو 𓆪", url=f"https://t.me/J0KER7x"),
            ],
            [
                InlineKeyboardButton("⌯ اضافه البوت اللي مجموعتك ⌯", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(command(["ping", "ينج", "يست", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime","لوقت", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "**شكرا  لإضافتي إلى مجموعتك 🖤**\n**[𝐒𝐄𝐋𝐕𝐀 𝐌𝐔𝐒𝐈𝐂 🎶](https://t.me/SO_SELVA) **\n"
                "قم بترقيتي كمسؤول عن المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⌯ قناة البوت ⌯", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("⌯ جروب البوت ⌯", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("⌯ 𝐒𝐄𝐋𝐕𝐀 𝐌𝐔𝐒𝐈𝐂 🎶 ⌯", url=f"https://t.me/SO_SELVA"),
                        ],
                        [
                            InlineKeyboardButton(
                        "⌯ اضافه البوت اللي مجموعتك ⌯",
                        url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
