import discord
import ferie
from randomfox import get_fox
from meteo import get_temp
from roulette import roulette
from lyrics import get_lyrics
from random_dog import get_dog
import os
from random import randint
import time

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ".holiday":
        f = ferie.Ferie()
        feries_du_mois = f.get_feries()
        chaine = f"Ce mois-ci, il y a {len(feries_du_mois)} jour(s) férié(s).\n"
        x = 0
        for i in feries_du_mois:
            x += 1
            chaine += str(i[0]) + ' (' + str(i[1]) + ')'
            if x < len(feries_du_mois):
                chaine += ', '
        chaine += '.'
        await message.channel.send(chaine)

    quoi = ('quoi', 'Quoi', 'QUOI', 'quois', 'koi', 'Koi', 'KOI', 'quoie', 'quoient')
    quoimsg = message.content.strip("?,.;!: ")
    if quoimsg.endswith(quoi):
        await message.channel.send('feur')

    hein = ('hein', 'hein?', 'hein ?', 'huns', 'hun', 'Huns', 'Hun')
    if message.content.endswith(hein):
        await message.channel.send('deux')

    nword = ('negro', 'nigger', 'negre', 'nègre', 'niggers', 'negros', 'négro', 'négros', 'negres', 'nègres', 'nigga', 'niggas')
    limite = ('???? limite ça', '??? allo ça bug', 'euhh ???', '??????????', 'euh mon reuf ?')
    for i in nword:
        if i in message.content:
            res = randint(0, len(limite)-1)
            await message.channel.send(limite[res])
            break

    if message.content == 'renard' or message.content == 'Renard':
        fox = get_fox()
        await message.channel.send(fox)

    meteo = ('meteo', 'météo', 'Météo', 'Meteo', 'METEO')
    if message.content.startswith(meteo):
        try:
            r = message.content
            city = r[6:]
            name, temp, ressenti, description = get_temp(city)
            await message.channel.send(f"Il fait actuellement, à {name}, {temp}°C (ressenti {ressenti}°C, {description}).")
        except KeyError:
            await message.channel.send("Erreur. Essayez une autre ville.")

    if message.content.startswith('roulette'):
        r = message.content
        liste = r[9:]
        try:
            await message.channel.send(roulette(liste))
        except:
            await message.channel.send('Error.')

    if message.content == 'réel' or message.content == 'Réel':
        rand = randint(1, 5)
        if rand == 1:
            await message.channel.send("mais reste digne akhy")

    if message.content.startswith(".lyrics"):
        name = message.content[8:]
        try:
            lyrics1, lyrics2, lyrics3 = get_lyrics(name)
            await message.channel.send("```\n" + lyrics1 + "\n```")
            await message.channel.send("```\n" + lyrics2 + "\n```")
            await message.channel.send("```\n" + lyrics3 + "\n```")
        except:
            try:
                lyrics1, lyrics2 = get_lyrics(name)
                await message.channel.send("```\n" + lyrics1 + "\n```")
                await message.channel.send("```\n" + lyrics2 + "\n```")
            except:
                lyrics1 = get_lyrics(name)
                await message.channel.send("```\n" + lyrics1 + "\n```")

    if message.content.startswith('repeat'):
        repeat = message.content[7:]
        await message.delete()
        await message.channel.send(repeat)

    rand = randint(1, 100)
    if rand == 1:
        await message.channel.send(str("👍"))
        time.sleep(2)
        await message.channel.send("(menfout en gros)")

    if message.content == "bon toutou":
        dog = get_dog()
        await message.channel.send(dog)


client.run(os.getenv('WATI_BOT_TOKEN'))
