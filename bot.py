import discord
from discord import app_commands
from discord.ext import commands
from keep_alive import keep_alive
import responses
import patchgpt
import asyncio

is_private = False


async def send_message(message, user_message):
    await message.response.defer(ephemeral=is_private)
    try:
        response = '> **' + user_message + '** - <@' + \
            str(message.user.id) + '>\n\n'
        response += await responses.handle_response(user_message)
        if len(response) > 1900:
            # Split the response into smaller chunks of no more than 1900 characters each(Discord limit is 2000 per chunk)
            if "```" in response:
                # Split the response if the code block exists
                parts = response.split("```")
                # Send the first message
                await message.followup.send(parts[0])
                # Send the code block in a seperate message
                code_block = parts[1].split("\n")
                formatted_code_block = ""
                for line in code_block:
                    while len(line) > 1900:
                    # Split the line at the 50th character
                        formatted_code_block += line[:1900] + "\n"
                        line = line[1900:]
                    formatted_code_block += line + "\n" # Add the line and seperate with new line

                # Send the code block in a separate message
                if (len(formatted_code_block) > 2000):
                    code_block_chunks = [formatted_code_block[i:i+1900] for i in range(0, len(formatted_code_block), 1900)]
                    for chunk in code_block_chunks:
                        await message.followup.send("```" + chunk + "```")
                else:
                    await message.followup.send("```" + formatted_code_block + "```") 

                # Send the remaining of the response in another message
                
                if len(parts) >= 3:
                    await message.followup.send(parts[2])
            else:
                response_chunks = [response[i:i+1900]
                               for i in range(0, len(response), 1900)]
                for chunk in response_chunks:
                    await message.followup.send(chunk)
        else:
            await message.followup.send(response)
    except Exception as e:
        await message.followup.send("> **Hummmm , encore un erreur , bah au moins je vous aime**")
        print(e)


async def send_message_mp(message, user_message, is_private):
    try:
        messagetoedit = await message.author.send("loading...")
        response = await responses.handle_response(user_message)
        await messagetoedit.edit(
            content = response) if is_private else await messagetoedit.edit(content = response)

    except Exception as e:
        print(e)


intents = discord.Intents.default()
intents.message_content = True


def run_discord_bot():
    TOKEN = ""
    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        await client.tree.sync()
        print(f'{client.user} is now running!')

    keep_alive()

    @client.tree.command(name="chat", description="Parler avec Three")
    async def chat(interaction: discord.Interaction, *, message: str):
        if interaction.user == client.user:
            return
        username = str(interaction.user)
        user_message = message
        channel = str(interaction.channel)
        print(f"{username} said: '{user_message}' ({channel})")
        await send_message(interaction, user_message)

    @client.tree.command(name="private", description="Toggle private access")
    async def private(interaction: discord.Interaction):
        global is_private
        await interaction.response.defer(ephemeral=False)
        if not is_private:
            is_private = not is_private
            print("Switch to private mode")
            await interaction.followup.send(
                "> **Info: Ensuite, la r??ponse sera envoy??e par message priv??. Si vous souhaitez revenir en mode public, utilisez `/public`**"
            )
        else:
            print("You already on private mode!")
            await interaction.followup.send(
                "> **Warn: Vous ??tes d??j?? en mode priv??. Si vous souhaitez passer en mode public, utilisez `/public`**"
            )

    @client.tree.command(name="public", description="Toggle public access")
    async def public(interaction: discord.Interaction):
        global is_private
        await interaction.response.defer(ephemeral=False)
        if is_private:
            is_private = not is_private
            await interaction.followup.send(
                "> **Info: Ensuite, la r??ponse sera envoy??e directement au canal. Si vous souhaitez revenir en mode priv??, utilisez `/private`**"
            )
            print("Switch to public mode")
        else:
            await interaction.followup.send(
                "> **Warn: Vous ??tes d??j?? en mode public. Si vous souhaitez passer en mode priv??, use `/private`**"
            )
            print("You already on public mode!")

    @client.tree.command(name="reset", description="Rendez Three amnesique")
    async def reset(interaction: discord.Interaction):
        #global Global_prompt
        responses.Global_prompt = ""
        #responses.chatbot.reset_chat()
        await interaction.response.defer(ephemeral=False)
        await interaction.followup.send("> **Info: Ah j'ai tout oubli??.**")
        print("The CHAT BOT has been successfully reset")

    @client.tree.command(name="googleit", description="return le premier page google sous forme d image")
    async def googleit(interaction: discord.Interaction, *, message: str):
        username = str(interaction.user)
        user_message = message
        channel = str(interaction.channel)
        await interaction.response.defer(ephemeral=False)

        image = await patchgpt.screenshot(user_message)
        print(image)
        #asyncio.sleep()
        await interaction.followup.send("Voici l image " + image )

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if (channel != "Direct Message with Unknown User"):
            return

        print(f"{username} MP said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message_mp(message, user_message, is_private=True)
        else:
            await send_message_mp(message, user_message, is_private=False)

    client.run(TOKEN)
