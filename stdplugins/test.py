from telethon import events
import asyncio
import os
import sys

@borg.on(events.NewMessage(pattern=r"\.t", outgoing=True))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Nihal ❤️ Priyanka")
