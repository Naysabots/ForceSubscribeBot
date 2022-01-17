from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
<b>Hey</b><b> {}</b>

❄️ <code>This is a Force subscribe bot to force users to join a specific channel before sending messages in a group</code>

💡 <code>Use Help Button To Know How to Use Me</code>

🚴‍♂️ <b>Maintained By</b><b> : @NaysaBots</b>
    """

    # Home Button
    home_buttons = [
        [
        InlineKeyboardButton('🏯 Home', callback_data='home'),
        InlineKeyboardButton('🚴‍♂️ About', callback_data='about'),
        InlineKeyboardButton('♨️ Close', callback_data='close')
        ]
        ]

    # Rest Buttons
    buttons = [
        [
        InlineKeyboardButton('♻️ Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('♨️ Close', callback_data='close')
        ]
        ]

    # Help Message
    HELP = """

1) Add me as Admin in your group.
 
2) Add me to the particular chat as Admin where you want to force your users to join. It can be any group or channel, public or private.
 
3) Now use /fsub chat_id/username
if your Channel/Group is private then provide chat id .

👥 **For get group chat ID use 👉 /id command in your group**
💡**For channel ID Open your Channel and send message 👉 /id**
 
4) Additional Features: /settings to change settings!
 
 
✨ **Available Commands** ✨
 
/fsub - See current force subscribe chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
 
📝 **Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
 **🤖 Bot :** Force-Sub-Bot\n
 **👲 Developer :** [Tellybots](https://telegram.me/tellybots_4u)\n
 **👥 Channel :** [Tellybots](https://telegram.me/tellybots_4u)\n
 **❄️ Credits :** Everyone in this journey\n
 **🍴 Source :** [Click here](https://t.me/tellybots)\n
 **📝 Language :** [Python3](https://python.org)\n
 **📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
 **🌟 Server :** [Heroku](https://heroku.com)\n
"""
