from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
<b>Hey</b><b> {}</b>

🌲 <code>This is a Force subscribe bot to force users to join a specific channel before sending messages in a group</code>

💡 <code>Use Help Button To Know How to Use Me</code>

🚴‍♂️ <b>Maintained By</b><b> : @NaysaBots</b>
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001505616678` or `/forcesubscribe -1001375849192`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

✨ **Available Commands** ✨

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram force subscribing bot by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/ForceSubscribeBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
