import os 
import requests
from twitchio.ext import commands
from youtubesearchpython.__future__ import VideosSearch
from twitch_songrequest_bot.models import collection


URL = 'localhost:5000/playlist'
class Bot(commands.Bot):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)
    
    async def event_ready(self):
        print(f'Ready | {self.nick}')
        ws = self._ws
        await ws.send_privmsg(os.environ['CHANNEL'], f"/me songrequests available with !sr <music>")

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)


    @commands.command(name='sr')
    async def sr(self, ctx):
        message = ctx.message.content.replace("!sr ", "")
        message += " lyrics"
        videosSearch = VideosSearch(message, limit = 2)
        videosResult = await videosSearch.next()
        link = videosResult["result"][0]["link"]
        filter = {"_id": ctx.author.id, "current_username": ctx.author.name}
        update = { "$push": { "songqueue": f"{link}" } } 
        collection.update_one(filter, update, upsert=True)
        await ctx.send(f'link {link}')

