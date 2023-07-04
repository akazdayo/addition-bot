import discord
from discord import app_commands
import re

# デフォルトの意図を設定します。
intents = discord.Intents.default()

# Discordクライアントを作成します。
client = discord.Client(intents=intents)

# コマンドツリーを作成します。
tree = app_commands.CommandTree(client)


# 起動イベントを定義します。
@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()  # スラッシュコマンドを同期


# 足し算のコマンドを定義します。
@tree.command(name="addition", description="足し算をします。")
async def default_command(interaction: discord.Interaction, formula: str):
    # 式から数字を抽出します。
    numbers = re.findall("\d+", formula)

    # 数字を整数に変換します。
    numbers = [int(i) for i in numbers]

    # 数字の長さが 1 以上の場合、足し算をします。
    if len(numbers) > 1:
        answer = sum(numbers)
    else:
        answer = "エラーが発生しました。"

    # 結果を返信します。
    await interaction.response.send_message(f"{formula} = {answer}")


# Discordクライアントを実行します。
client.run("MTAyMzg1MzE0NzY0NDUwNjIwMw.GCwgmE.heMFayfFND2QWTQhLyusvSeGHtml4EuPWICmPs")
