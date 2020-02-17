"""use cmd .Avinash
aaahaaa you can edit this 😉"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "Avinash":

        await event.edit(input_str)

        animation_chars = [

            "👑Avinash👑👑👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️◼️👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️◼️◼️️👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️◼️◼️◼️👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "‎◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Avinash👑👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Avinash👑👑Avinash👑◼️◼️\n◼️👑Avinash👑👑Avinash👑👑Avinash👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Avinash👑👑Avinash👑◼️◼️\n◼️👑Avinash👑👑Avinash👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Avinash👑👑Avinash👑◼️◼️\n◼️👑Avinash👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Avinash👑👑Avinash👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑Avinash👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            "👑 Avinash 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
