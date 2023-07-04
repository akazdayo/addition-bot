import discord
from discord import app_commands
import re

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()  # スラッシュコマンドを同期


@tree.command(name="addition", description="足し算をします。")
async def default_command(interaction: discord.Interaction, formula: str):
    numbers = re.findall("\d+", formula)
    numbers = [int(i) for i in numbers]
    if len(numbers) > 1:
        answer = sum(numbers)
    else:
        answer = "エラーが発生しました。"
    await interaction.response.send_message(f"{formula} = {answer}")  # 返信


client.run("トークンの記入")
