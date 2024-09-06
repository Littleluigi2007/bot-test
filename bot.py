import random
import os
import requests
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('image/memes'))
    '''meme atar'''
    with open(f'image/memes/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''dog komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    '''merhaba'''
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 500):
    '''he'''
    await ctx.send("he" * count_heh) 
    
@bot.command()
async def usbformat(ctx):
    '''usb nasil format edilir'''
    await ctx.send(f'ilk once dosya gezsginini acman gerekiyor, sonra format atacagin usbyi sag tikla, sonra bicimlendire bas, sonra istedigin dosya sistemini sectikten sonra baslata bas')
    with open('image/usb/1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def taskmanager(ctx):
    '''task manager nasil acilir'''
    await ctx.send(f'eger bilgisayarda bir program durduysa, ctrl+shift+esc ile task manageri acabilir ve programi zorla kapatabilirsiniz')

@bot.command()
async def indirilenlerim(ctx):
    '''indirdigim seyler nerde'''
    await ctx.send(f'dosya gezginini actiktan sonra indirilenler dosyasi bulunabilir')
    
@bot.command()
async def copbosaltma(ctx):
    '''copumu nasil bosaltabilirim'''
    await ctx.send(f'geri donusume sag tikladiktan sonra cop kutusunu bosalt secegine tikla')
    
@bot.command()
async def kaynakkullanimi(ctx):
    '''bilgisayarim partlari ne kadar kullaniliyor'''
    await ctx.send(f'task manageri actiktan sonra performansa tiklayarak cpu, gpu, ram vb. kaynak kullanimi gorulebilir')
    
@bot.command()
async def supriz(ctx):
    '''dene bakiyim'''
    await ctx.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
@bot.command()
async def yummers(ctx):
    '''yummers'''
    await ctx.send(f'https://tenor.com/view/homelander-the-boys-yummers-gif-730693117818784194')
    
@bot.command()
async def yuckers(ctx):
    '''yuckers'''
    await ctx.send(f'https://tenor.com/view/homelander-n0-the-boys-starr-gif-25749194')
    
    

bot.run("")
