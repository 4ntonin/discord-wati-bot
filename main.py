import discord
from modules.ferie import Ferie
from modules.randomfox import get_fox
from modules.meteo import get_temp
from modules.roulette import roulette
from modules.lyrics import get_lyrics
from modules.random_dog import get_dog
import os
from random import randint
import time

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    channel = message.channel
    content = message.content
    if message.author == client.user:
        return

    quoi = ('quoi', 'Quoi', 'QUOI', 'quois', 'koi', 'Koi', 'KOI', 'quoie', 'quoient')
    quoimsg = content.strip("?,.;!: ")
    if quoimsg.endswith(quoi):
        await channel.send('feur')

    hein = ('hein', 'hein?', 'hein ?', 'huns', 'hun', 'Huns', 'Hun')
    if content.endswith(hein):
        await channel.send('deux')

    nword = ('negro', 'nigger', 'negre', 'nègre', 'niggers', 'negros', 'négro', 'négros', 'negres', 'nègres', 'nigga', 'niggas')
    limite = ("???? limite ça", "??? allo ça bug", "euhh ???", "??????????", "euh mon reuf ?", "? c'est raciste ça")
    for i in nword:
        if i in content:
            res = randint(0, len(limite) - 1)
            await channel.send(limite[res])
            break

    juif = ('juif', 'juifs', 'Juif', 'Juifs', 'JUIF', 'JUIFS')
    for i in juif:
        if i in content:
            with open('data\\attentionsolglissant.jpg', 'rb') as attentionsolglissant:
                await channel.send(file=discord.File(attentionsolglissant))
            break

    meteo = ('meteo', 'météo', 'Météo', 'Meteo', 'METEO')
    if content.startswith(meteo):
        try:
            r = content
            city = r[6:]
            name, temp, ressenti, description = get_temp(city)
            await channel.send(f"Il fait actuellement, à {name}, {temp}°C (ressenti {ressenti}°C, {description}).")
        except KeyError:
            await channel.send("Erreur. Essayez une autre ville.")
    elif content.startswith('roulette'):
        r = content
        liste = r[9:]
        try:
            await channel.send(roulette(liste))
        except:
            await channel.send('Error.')
    elif content.startswith(".lyrics"):
        name = content[8:]
        try:
            lyrics1 = get_lyrics(name)
            await channel.send("```\n" + lyrics1 + "\n```")
        except:
            try:
                lyrics1, lyrics2 = get_lyrics(name)
                await channel.send("```\n" + lyrics1 + "\n```")
                await channel.send("```\n" + lyrics2 + "\n```")
            except:
                lyrics1, lyrics2, lyrics3 = get_lyrics(name)
                await channel.send("```\n" + lyrics1 + "\n```")
                await channel.send("```\n" + lyrics2 + "\n```")
                await channel.send("```\n" + lyrics3 + "\n```")
    elif content.startswith("repeat"):
        repeat = content[7:]
        try:
            await message.delete()
            await channel.send(repeat)
        except:
            await channel.send("? je suis pas ton chien en gros")

    rand = randint(1, 100)
    if rand == 1:
        await channel.send(str("👍"))
        time.sleep(2)
        await channel.send("(menfout en gros)")

    if content == "bon toutou":
        dog = get_dog()
        await channel.send(dog)
    elif content == 'réel' or content == 'Réel':
        rand = randint(1, 5)
        if rand == 1:
            await channel.send("mais reste digne akhy")
    elif content == 'renard' or content == 'Renard':
        fox = get_fox()
        await channel.send(fox)
    elif content == ".holiday":
        f = Ferie()
        feries_du_mois = f.get_feries()
        chaine = f"Ce mois-ci, il y a {len(feries_du_mois)} jour(s) férié(s).\n"
        x = 0
        for i in feries_du_mois:
            x += 1
            chaine += str(i[0]) + ' (' + str(i[1]) + ')'
            if x < len(feries_du_mois):
                chaine += ', '
        chaine += '.'
        await channel.send(chaine)
    elif content == ".bonsoirnon":
        await message.delete()
        with open('data\\bonsoirnon.jpg', 'rb') as bonsoirnon:
            await channel.send(file=discord.File(bonsoirnon))
    elif content == ".genant":
        await message.delete()
        with open('data\\normancepetitblagueur.jpg', 'rb') as norman:
            await channel.send(file=discord.File(norman))
    elif content == ".sheesh":
        await message.delete()
        with open('data\\sheesh-earrape.mp3', 'rb') as sheesh:
            await channel.send(file=discord.File(sheesh))


client.run(os.getenv('WATI_BOT_TOKEN'))
