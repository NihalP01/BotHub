"""COMMAND : ./calling"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "/calling":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @testing_userbot ,`Please Connect me to Nihal Buragohain`",
            "`User Authorised.`",
            "`Calling Nihal Buragohain (@NihalP01) At +91700XXXXXXX`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Nihal: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @testing_userbot",
            "`Nihal: OMG!!! I Am FAN Of You Sir...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Nihal: Please Don't Thank Sur, Telegram Is Your's. Just Gimme A Call When You Be Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Nihal: Yes Sur, There are too many Idiots In Telegram \nI Am Not Able To Shut their mouth. If Possible, Please make them.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fuck their ass.`",
            "`Nihal: Sure Sur \nTC Bye Bye \nPKMKB :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 22])
