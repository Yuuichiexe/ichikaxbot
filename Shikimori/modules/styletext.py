"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.modules.helper_funcs.alternate import typing_action
from telegram import ParseMode

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
bubblefont = [
    "ⓐ",
    "ⓑ",
    "ⓒ",
    "ⓓ",
    "ⓔ",
    "ⓕ",
    "ⓖ",
    "ⓗ",
    "ⓘ",
    "ⓙ",
    "ⓚ",
    "ⓛ",
    "ⓜ",
    "ⓝ",
    "ⓞ",
    "ⓟ",
    "ⓠ",
    "ⓡ",
    "ⓢ",
    "ⓣ",
    "ⓤ",
    "ⓥ",
    "ⓦ",
    "ⓧ",
    "ⓨ",
    "ⓩ",
]
fbubblefont = [
    "🅐",
    "🅑",
    "🅒",
    "🅓",
    "🅔",
    "🅕",
    "🅖",
    "🅗",
    "🅘",
    "🅙",
    "🅚",
    "🅛",
    "🅜",
    "🅝",
    "🅞",
    "🅟",
    "🅠",
    "🅡",
    "🅢",
    "🅣",
    "🅤",
    "🅥",
    "🅦",
    "🅧",
    "🅨",
    "🅩",
]
squarefont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
fsquarefont = [
    "🅰",
    "🅱",
    "🅲",
    "🅳",
    "🅴",
    "🅵",
    "🅶",
    "🅷",
    "🅸",
    "🅹",
    "🅺",
    "🅻",
    "🅼",
    "🅽",
    "🅾",
    "🅿",
    "🆀",
    "🆁",
    "🆂",
    "🆃",
    "🆄",
    "🆅",
    "🆆",
    "🆇",
    "🆈",
    "🆉",
]
bluefont = [
    "🇦 ",
    "🇧 ",
    "🇨 ",
    "🇩 ",
    "🇪 ",
    "🇫 ",
    "🇬 ",
    "🇭 ",
    "🇮 ",
    "🇯 ",
    "🇰 ",
    "🇱 ",
    "🇲 ",
    "🇳 ",
    "🇴 ",
    "🇵 ",
    "🇶 ",
    "🇷 ",
    "🇸 ",
    "🇹 ",
    "🇺 ",
    "🇻 ",
    "🇼 ",
    "🇽 ",
    "🇾 ",
    "🇿 ",
]
latinfont = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "ℯ",
    "𝒻",
    "ℊ",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "ℴ",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]
linedfont = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]


@typing_action
def weebify(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def bubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/bubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def fbubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fbubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fbubblecharacter = fbubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fbubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def square(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/square <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            squarecharacter = squarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, squarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def fsquare(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fsquare <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fsquarecharacter = fsquarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fsquarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def blue(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/blue <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bluecharacter = bluefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bluecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def latin(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/latin <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            latincharacter = latinfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, latincharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def lined(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/lined <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            linedcharacter = linedfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linedcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)

__mod_name__ = "𝐒ᴛʏʟᴇᴛᴇxᴛ"

__help__ = """
 ❍ `/weebify` <text>: returns a weebified text
 ❍ `/bubble` <text>: bubble your text!
 ❍ `/fbuble` <text>: bubble-filled your text!
 ❍ `/square1` <text>: square your text!
 ❍ `/fsquare` <text>: square-filled your text!
 ❍ `/blue` <text>: bluify your text!
 ❍ `/latin` <text>: latinify your text!
 ❍ `/lined` <text>: lined your text!
 """

WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify, run_async=True)
BUBBLE_HANDLER = DisableAbleCommandHandler("bubble", bubble, run_async=True)
FBUBBLE_HANDLER = DisableAbleCommandHandler("fbubble", fbubble, run_async=True)
SQUARE_HANDLER = DisableAbleCommandHandler("square", square, run_async=True)
FSQUARE_HANDLER = DisableAbleCommandHandler("fsquare", fsquare, run_async=True)
BLUE_HANDLER = DisableAbleCommandHandler("blue", blue, run_async=True)
LATIN_HANDLER = DisableAbleCommandHandler("latin", latin, run_async=True)
LINED_HANDLER = DisableAbleCommandHandler("lined", lined, run_async=True)

dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(BUBBLE_HANDLER)
dispatcher.add_handler(FBUBBLE_HANDLER)
dispatcher.add_handler(SQUARE_HANDLER)
dispatcher.add_handler(FSQUARE_HANDLER)
dispatcher.add_handler(BLUE_HANDLER)
dispatcher.add_handler(LATIN_HANDLER)
dispatcher.add_handler(LINED_HANDLER)

__command_list__ = ["weebify"]
__command_list__ = ["bubble"]
__command_list__ = ["fbubble"]
__command_list__ = ["square"]
__command_list__ = ["fsquare"]
__command_list__ = ["blue"]
__command_list__ = ["latin"]
__command_list__ = ["lined"]
__handlers__ = [WEEBIFY_HANDLER]
__handlers__ = [BUBBLE_HANDLER]
__handlers__ = [FBUBBLE_HANDLER]
__handlers__ = [SQUARE_HANDLER]
__handlers__ = [FSQUARE_HANDLER]
__handlers__ = [BLUE_HANDLER]
__handlers__ = [LATIN_HANDLER]
__handlers__ = [LINED_HANDLER]
