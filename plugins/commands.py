"""
RadioPlayerV2, Telegram Voice Chat Userbot
Copyright (C) 2021  Asm Safone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "π **Hey [{}](tg://user?id={})**,\n\nI'm **Radio Player Bot** \n\nI Can Play Radio/Stream Music In Channels & Groups 24x7 Nonstop. \n\nMade By π€ @DARK_ANGEL_1234!"
HELP = """π·οΈ **Need Help?** π€·ββοΈ

π·οΈ **Common Commands**:
\u2022 `/play` reply to an audio to play or queue it
\u2022 `/help` shows help for commands
\u2022 `/playlist` shows the playlist
\u2022 `/current` shows playing time of current track
\u2022 `/song` [song name] download the song as audio

π·οΈ **Admin Commands**:
\u2022 `/skip` [n] skip current or n where n >= 2
\u2022 `/join` join voice chat of current group
\u2022 `/leave` leave current voice chat
\u2022 `/vc` check which VC is joined
\u2022 `/stop` stop playing music
\u2022 `/radio` start radio stream
\u2022 `/stopradio` stop radio stream
\u2022 `/replay` play from the beginning
\u2022 `/clean` remove unused RAW PCM files
\u2022 `/pause` pause playing music
\u2022 `/resume` resume playing music
\u2022 `/mute` mute the VC userbot
\u2022 `/unmute` unmute the VC userbot
\u2022 `/restart` restart the bot\n\n**π£οΈAny Doubt @Mo_Tech_Group**
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('β‘οΈMasterβ‘οΈ', url='https://t.me/DARK_ANGEL_1234'),
        InlineKeyboardButton('Help βοΈ', callback_data='help'),
    ],
    [
        InlineKeyboardButton('π£οΈAny Doubt', url='https://t.me/Mo_Tech_Group'),
        InlineKeyboardButton('Bot Updatesπ', url='https://telegram.me/Mo_Tech_YT'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
