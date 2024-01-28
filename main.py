import discord
from discord.ext import commands, tasks
import asyncio
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents.default()
intents.presences = True  # Presences must be enabled to receive member activities

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yaptık: {bot.user.name}')

    # Oyun durumunu güncelleme görevini başlat
    update_game_status.start()

@tasks.loop(seconds=60)  # Her 60 saniyede bir çalışacak şekilde ayarlanabilir
async def update_game_status():
    await bot.change_presence(activity=discord.Streaming(name='F', type=discord.ActivityType.streaming, url='https://www.twitch.tv/monstercat'))

# Bot'u çalıştır
bot.run("MTIwMTE3NDg4NzY2Mjg3ODc4MA.GPlBly.FKVK_qWEUQjL8rSOysbESY0p-uy-e8x4ehhVqk")
