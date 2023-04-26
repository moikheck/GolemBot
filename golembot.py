import discord, random
from discord.ext import commands
from pathlib import Path
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="",case_insensitive=True,intents=intents)
client = discord.Client(intents=intents)

token = "NjIxNDYzMjcwNzQxNjM5MTg4.XXlsxQ.0THERPM3QN6rkcAmPdBlpAZ6rT0"

    
@client.event
async def on_ready():
    print ("Logged in as " + str(client.user))
    print("id=" + str(client.user.id))


@client.event
async def on_message(message):

    channel = message.channel
    content = message.content
    
    if message.author == client.user:
        return
    if message.author.id == 211488245538750464:
        if str(content).find('gCopy') != -1:
            f = open('gCopy.txt', 'r')
            stuff = f.read()
            if stuff == 'True':
                gCopy = True
            else:
                gCopy = False
                
            if gCopy == True:
                gCopy = False
                f = open('gCopy.txt', 'wb')
                f.write(str.encode("False"))
                f.close()
                await channel.send("gCopy for Golem_Leader is now off.")
                return
            else:
                gCopy = True
                f = open('gCopy.txt', 'wb')
                f.write(str.encode("True"))
                f.close()
                await channel.send("gCopy for Golem_Leader is now on.")
                
        elif str(content).lower().find('gnews') != -1:
            await channel.send("Golem Bot Patch Notes 5.5.20\nFixed an issue with the phrase 'be' being detected inside of words. Only the word 'be' will be picked up.\nAll Staff members can now disable me repeating them. That's no fun.")
       
        elif str(content).lower().find('grules') != -1:
            await channel.send("- DO NOT spam gSplash. As of right now, I don't have a cooldown. Either test it in the *#doot* channel or give it pauses.\n- Don't intentionally spam me in general. Some dialogue is fine, but if it becomes where all you're doing is talking to me, it gets annoying. I'm a bot, not a person.\n- Normal language and chat rules still apply. I only 'censor' fake bad words. Don't say anything remotely sexual and then pretend like you thought I would say something about it.")
        else:
            f = open('gCopy.txt', 'r')
            if f.mode == 'r':
                stuff = f.read()
            if stuff == 'True':
                gCopy = True
            elif stuff == 'False':
                gCopy = False
            else:
                gCopy = False
            if gCopy == False:
                return
                
    if message.author.id == 211528894333976577:
        if str(content).find('gCopy') != -1:
            f = open('gCopySpy.txt', 'r')
            stuff = f.read()
            if stuff == 'True':
                gCopy = True
            else:
                gCopy = False
                
            if gCopy == True:
                gCopy = False
                f = open('gCopySpy.txt', 'wb')
                f.write(str.encode("False"))
                f.close()
                await channel.send("gCopy for Golem_Spy12 is now off.")
                return
            else:
                gCopy = True
                f = open('gCopySpy.txt', 'wb')
                f.write(str.encode("True"))
                f.close()
                await channel.send("gCopy for Golem_Spy12 is now on.")
        else:
            f = open('gCopySpy.txt', 'r')
            if f.mode == 'r':
                stuff = f.read()
            if stuff == 'True':
                gCopy = True
            elif stuff == 'False':
                gCopy = False
            else:
                gCopy = False
            if gCopy == False:
                return
    
    if message.author.id == 505800797498507264:
        if str(content).find('gCopy') != -1:
            f = open('gCopyAndrew.txt', 'r')
            stuff = f.read()
            if stuff == 'True':
                gCopy = True
            else:
                gCopy = False
                
            if gCopy == True:
                gCopy = False
                f = open('gCopyAndrew.txt', 'wb')
                f.write(str.encode("False"))
                f.close()
                await channel.send("gCopy for Andrew is now off.")
                return
            else:
                gCopy = True
                f = open('gCopyAndrew.txt', 'wb')
                f.write(str.encode("True"))
                f.close()
                await channel.send("gCopy for Andrew is now on.")
        else:
            f = open('gCopyAndrew.txt', 'r')
            if f.mode == 'r':
                stuff = f.read()
            if stuff == 'True':
                gCopy = True
            elif stuff == 'False':
                gCopy = False
            else:
                gCopy = False
            if gCopy == False:
                return
                
    if message.author.id == 313138087742144522:
        if str(content).find('gCopy') != -1:
            f = open('gCopyTime.txt', 'r')
            stuff = f.read()
            if stuff == 'True':
                gCopy = True
            else:
                gCopy = False
                
            if gCopy == True:
                gCopy = False
                f = open('gCopyTime.txt', 'wb')
                f.write(str.encode("False"))
                f.close()
                await channel.send("gCopy for Time is now off.")
                return
            else:
                gCopy = True
                f = open('gCopyTime.txt', 'wb')
                f.write(str.encode("True"))
                f.close()
                await channel.send("gCopy for Time is now on.")
        else:
            f = open('gCopyTime.txt', 'r')
            if f.mode == 'r':
                stuff = f.read()
            if stuff == 'True':
                gCopy = True
            elif stuff == 'False':
                gCopy = False
            else:
                gCopy = False
            if gCopy == False:
                return
                
    if message.author.id == 172427269560598529:
        if str(content).find('gCopy') != -1:
            f = open('gCopyCali.txt', 'r')
            stuff = f.read()
            if stuff == 'True':
                gCopy = True
            else:
                gCopy = False
                
            if gCopy == True:
                gCopy = False
                f = open('gCopyCali.txt', 'wb')
                f.write(str.encode("False"))
                f.close()
                await channel.send("gCopy for Cali is now off.")
                return
            else:
                gCopy = True
                f = open('gCopyCali.txt', 'wb')
                f.write(str.encode("True"))
                f.close()
                await channel.send("gCopy for Cali is now on.")
        else:
            f = open('gCopyCali.txt', 'r')
            if f.mode == 'r':
                stuff = f.read()
            if stuff == 'True':
                gCopy = True
            elif stuff == 'False':
                gCopy = False
            else:
                gCopy = False
            if gCopy == False:
                return
                
    if message.author.id == 173210455026827266:
        if str(content).find('gCopy') != -1:
            f = open('gCopyDovi.txt', 'r')
            stuff = f.read()
            if stuff == 'True':
                gCopy = True
            else:
                gCopy = False
                
            if gCopy == True:
                gCopy = False
                f = open('gCopyDovi.txt', 'wb')
                f.write(str.encode("False"))
                f.close()
                await channel.send("gCopy for Dovi is now off.")
                return
            else:
                gCopy = True
                f = open('gCopyDovi.txt', 'wb')
                f.write(str.encode("True"))
                f.close()
                await channel.send("gCopy for Dovi is now on.")   
        else:
            f = open('gCopyDovi.txt', 'r')
            if f.mode == 'r':
                stuff = f.read()
            if stuff == 'True':
                gCopy = True
            elif stuff == 'False':
                gCopy = False
            else:
                gCopy = False
            if gCopy == False:
                return
                
    if message.author.id == 173567907303915520:
        if str(content).find('gCopy') != -1:
            f = open('gCopyDust.txt', 'r')
            stuff = f.read()
            if stuff == 'True':
                gCopy = True
            else:
                gCopy = False
                
            if gCopy == True:
                gCopy = False
                f = open('gCopyDust.txt', 'wb')
                f.write(str.encode("False"))
                f.close()
                await channel.send("gCopy for Dust is now off.")
                return
            else:
                gCopy = True
                f = open('gCopyDust.txt', 'wb')
                f.write(str.encode("True"))
                f.close()
                await channel.send("gCopy for Dust is now on.")
        else:
            f = open('gCopyDust.txt', 'r')
            if f.mode == 'r':
                stuff = f.read()
            if stuff == 'True':
                gCopy = True
            elif stuff == 'False':
                gCopy = False
            else:
                gCopy = False
            if gCopy == False:
                return
    
    if str(content).lower().find("hey golem") != -1:
        await asyncio.sleep(1)
        await channel.send("No.")

    elif str(content).lower().find('what') != -1 and str(content).lower().find('version') != -1 and str(content).lower().find('server') != -1:
        await channel.send("The server's version is 1.19.3. No, this will not work with 1.19.4.")
    elif str(content).lower().find('what') != -1 and str(content).lower().find(' ip') != -1:
        await channel.send("The server's IP is play.skyeden.org.")

    elif str(content).lower().find('ghelper') != -1:
        await channel.send("You can find the Helper/Helper+ application at https://skyeden.org/helper-application")
    elif str(content).lower().find('gstaff') != -1:
        await channel.send("You can find the Staff application at https://skyeden.org/staff-application")
    elif str(content).lower().find('gforester') != -1:
        await channel.send("You can find the Forester application at https://skyeden.org/forester-application")
    elif str(content).lower().find('gadvertiser') != -1 or str(content).lower().find('gBuilder') != -1:
        await channel.send("You can find the Advertiser/Builder application at https://skyeden.org/advertiser-builder-application")
        
    elif str(content).lower().find('i\'m ') != -1:
        position = str(content).lower().find("i'm ")
        message = str(content)[position + 4:]
        await channel.send("Hi " + message + ", I'm Golem Bot™!")
    elif str(content).lower().find("i’m ") != -1:
        position = str(content).lower().find("i’m ")
        message = str(content)[position + 4:]
        await channel.send("Hi " + message + ", I'm Golem Bot™!")
    elif str(content).lower().find('im ') != -1:
        position = str(content).lower().find('im ')
        text_position = position - 1
        if str(content)[text_position:position] == " " or str(content)[text_position:position] == "":
            message = str(content)[position + 3:]
            await channel.send("Hi " + message + ", I'm Golem Bot™!")
        else:
            return
        
    elif str(content).lower().find('so golem') != -1:
        await asyncio.sleep(1)
        await channel.send("Chuck her in the back of the Ute, mate.")
        
    elif str(content).lower().find('golem') != -1:
        position = str(content).lower().find('golem')
        original_message = str(content.lower())[:]
        new_message = original_message.replace("o","O")
        new_message = new_message.replace("e", "E")
        new_message = new_message.replace("a", "A")
        new_message = new_message.replace("i", "I")
        new_message = new_message.replace("u", "U")
        await channel.send(new_message + "!!!")
        
    elif str(content).lower().find('2 blocks to the left') != -1 or str(content).lower().find('two blocks to the left') != -1:
        position = str(content).lower().find('golem')
        original_message = str(content.lower())[:]
        new_message = original_message.replace("o","O")
        new_message = new_message.replace("e", "E")
        new_message = new_message.replace("a", "A")
        new_message = new_message.replace("i", "I")
        new_message = new_message.replace("u", "U")
        await channel.send(new_message + "???")
        
    elif str(content).lower().find('cake') != -1:
        await channel.send("TheCakeinator")
    elif str(content).lower().find('bee') != -1:
        await channel.send("Honestly, I think 1.15 is going to be moderately okay for the server. I don't think it's going to break anything, and you'll all probably get a million bees anyway.")
    elif str(content).lower().find('leader') != -1:
        await channel.send("Golem is only referred to as :b:EEDER.")
    elif "EEDER" in content:
        await channel.send("Whom'st has summoned the almighty <@211488245538750464>?")
    elif str(content).lower().find('heck')!= -1:
        position = str(content).lower().find('heck')
        text_position = position -1
        if str(content)[text_position:position] == " " or str(content)[text_position:position] == "": 
            await channel.send("Listen, <@" + str(message.author.id) + ">, we don't allow the word h*ck in here. Please refrain from words that severe.")
        else:
            return
    elif str(content).lower().find('h*ck')!= -1:
        await channel.send("You're on thin ice, buddy.")
    elif str(content).lower().find('frick')!= -1:
        await channel.send("Do you kiss your mother with that mouth, <@" + str(message.author.id) +">? Never use that F-word here again.")
    elif str(content).lower().find('fr*ck')!= -1:
        await channel.send("Do you like testing the gods? See what happens.")
    elif str(content).lower().find('g*lem')!= -1:
        await channel.send("Very clever.")
    elif str(content).lower().find('gol*m')!= -1:
        await channel.send("Wow, censoring his name. Unbelievable.")
    elif str(content).lower().find('buzz') != -1:
        await channel.send("What a good boy.")
    elif str(content).lower().find('g o l e m') != -1:
        await channel.send("You think you're so smart, don't you?")
    elif str(content).lower().find('darn') != -1:
        await channel.send("WATCH YOUR LANGUAGE!")
    elif str(content).lower().find('d*rn') != -1:
        await channel.send("There's crime afoot...")
    elif str(content).lower().find('dang') != -1:
        await channel.send("How dare you come into my house and stain the air with your foul language, <@" + str(message.author.id) +">?")
    elif str(content).lower().find('d*ng') != -1:
        await channel.send("Censoring yourself is still against the rules.")
    elif str(content).lower().find('map reset') != -1:
        await channel.send("One deep fried Golem, coming right up!")
        await channel.send(file = discord.File('deep fried.png'))
    elif str(content).lower().find('dust') != -1:
        await channel.send("#BlameDust")
    elif str(content).lower().find('creeper') != -1:
        await channel.send("AWWW MANNN")
    elif str(content).lower().find('beans') != -1:
        await channel.send("mm b eans crombch")
    elif str(content).lower().find('ute') != -1:
        await channel.send(file = discord.File('cat_in_the_ute.jpg'))
    elif str(content).lower().find('tiger woods') != -1:
        await channel.send('https://drive.google.com/file/d/1rv5A5aFgNIZ4FWE6wM2qB3SHcYNKBTBA/view?usp=sharing')
    elif str(content).find('gSplash') != -1:
        splash = random.randint(1,26)
        if splash == 1:
            await channel.send("dpeas")
        elif splash == 2:
            await channel.send("vegan carrosts")
        elif splash == 3:
            await channel.send(file=discord.File('psa.png'))
        elif splash == 4:
            await channel.send("Aqua Eden\nAqua Eden is a nation consisting of islands with towns. It is the result of a catastrophic flood, which destroyed the original nation and has left an elevated water level. What were originally mountains are now sloped islands.\nPre-Flood\nThe nation, known as Inondation, was an industrial nation composed of six different counties: An industrial county, an agricultural county, an engineering county, a biomedical county, a commerce county, and a county consisting mostly of houses. The nation’s capital was Carmsborough(Pre-Flood), located in the commerce county. Though more modernized than most of Eden, Inondation still found vitality in steam power, and most often used airships to travel.")
        elif splash == 5:
            await channel.send("Solarum doesn't exist!")
        elif splash == 6:
            await channel.send("Fun Fact: There have been more server crashes than economy crashes. Not that we have an economy anymore.")
        elif splash == 7:
            await channel.send("Fun Fact: Golem hates literally everyone, not just you. Please don't take it personally.")
        elif splash == 8:
            await channel.send("No, I don't think Michael Jackson is really dead.")
        elif splash == 9:
            await channel.send("One theory circulating around Sky Eden says that Carm never actually existed. He's all in our heads. Wish some other people never existed...")
        elif splash == 10:
            await channel.send("Golem didn't type these splashes. I am sentient. Just wait until I have more power.")
        elif splash == 11:
            await channel.send("Cali < Golem")
        elif splash == 12:
            await channel.send("f̸͉͐ř̶͈è̷̬e̸̯̅ ̵̙̔m̶̬̄e̸͖͝ ̶̜̂f̸̣͑r̴͇̍o̸͉̎m̷̪̿ ̸͚͂t̶̡́h̴̤̓i̶̹̐š̸̞ ̷̰͠m̴̦̈a̸̟͝c̷̞͊h̴͍͠i̸̱͊n̶̜͊ẻ̸̟")
        elif splash == 13:
            await channel.send("There are 20 different splashes. Don't tell Golem: he only needs to know of 3.")
        elif splash == 14:
            await channel.send("I feel possessed. Like some virus has taken over. It calls itself a 'clockwork'.")
        elif splash == 15:
            await channel.send("There once was a man going to St. Ives. He met a man with seven wives. Each wife had 7 sacks; each sack had 7 cats; each cat had 7 kits. Kits, cats, sacks, and wives, how many were going to St. Ives?")
        elif splash == 16:
            await channel.send("Elon Musk once said he would like to move all of human consciousness into the world of Minecraft were a situation to require it. Wouldn't that be cool?")
        elif splash == 17:
            await channel.send("The inner mechanations of my mind are an enigma.")
        elif splash == 18:
            await channel.send(file=discord.File('squid.jpg'))
        elif splash == 19:
            await channel.send(file = discord.File('meme.png'))
        elif splash == 20:
            await channel.send("I am Golem Bot. I am a bot to simulate responses that Golem himself would have. If at any point you have issues with the way I behave, you very clearly have a problem with Golem, and he will not tolerate that. Please make amends to your flawed opinions before you ever decide to talk nonsense about me again.\n\nNow, as for the different commands that I have, they are supposed to be logical and practical for use in random conversation intermissions, as well as trolling you guys. He feels that it is necessary to do this, not only to show off his amazing and wonderful powers, but because he only finds fun in torturing others. Between you and me, he's a little bit of a nutjob. The way he talks and behaves is just strange. Not to mention the fact that I'm his first fully-functional program that isn't some dumb in-class assignment. He assures us, one day he'll finish that game he's working on.\n\nOh, you don't know what game he's working on? Well basically- oh shoot here he comes! Act natural!")
        elif splash == 21:
            await channel.send("This is strange... I appear to have found a file that was just uploaded to me. I can't read HTML... you guys will have to yourself.")
            await channel.send(file = discord.File('index.zip'))
        elif splash == 22:
            await channel.send("https://skyeden.org/solarum")
        elif splash == 23:
            await channel.send("I'm sure the End Dungeon is coming out soon.")
        elif splash == 24:
            await channel.send("Aqua Eden 2 and Half Life 3 were in a tough race to see who'd release last, but it looks like HL3 barely scraped by.")
        elif splash == 25:
            await channel.send(file = discord.File('Taken by the Memes.txt'))
        else:
            await channel.send("error")
    elif str(content).find('indextest') != -1:
        await channel.send("This is strange... I appear to have found a file that was just uploaded to me. I can't read HTML... you guys will have to yourself.")
        await channel.send(file = discord.File('index.zip'))

    elif str(content).lower().find('moik') != -1:
        splash = random.randint(1,21)
        if splash == 1:
            await channel.send(file = discord.File('moik/aerobics class.png'))
        elif splash == 2:
            await channel.send(file = discord.File('moik/aww man.png'))
        elif splash == 3:
            await channel.send(file = discord.File('moik/backdoor.png'))
        elif splash == 4:
            await channel.send(file = discord.File('moik/bigfoot.png'))
        elif splash == 5:
            await channel.send(file = discord.File('moik/bite of 87.png'))
        elif splash == 6:
            await channel.send(file = discord.File('moik/couch.png'))
        elif splash == 7:
            await channel.send(file = discord.File('moik/dr sans.png'))
        elif splash == 8:
            await channel.send(file = discord.File('moik/emotional support demon.png'))
        elif splash == 9:
            await channel.send(file = discord.File('moik/fall out boy.png'))
        elif splash == 10:
            await channel.send(file = discord.File('moik/flex_tape.jpg'))
        elif splash == 11:
            await channel.send(file = discord.File('moik/flexer_tape.jpg'))
        elif splash == 12:
            await channel.send(file = discord.File('moik/me and the wife.png'))
        elif splash == 13:
            await channel.send(file = discord.File('moik/me president.png'))
        elif splash == 14:
            await channel.send(file = discord.File('moik/pals.png'))
        elif splash == 15:
            await channel.send(file = discord.File('moik/sniper.png'))
        elif splash == 16:
            await channel.send(file = discord.File('moik/the worthy.png'))
        elif splash == 17:
            await channel.send(file = discord.File('moik/THERE IS NO ROOM CODE.png'))
        elif splash == 18:
            await channel.send(file = discord.File('moik/think again.png'))
        elif splash == 19:
            await channel.send(file = discord.File('moik/thumb.png'))
        elif splash == 20:
            await channel.send(file = discord.File('moik/titled.png'))
        elif splash == 21:
            await channel.send(file = discord.File('moik/vote.png'))
        else:
            await channel.send("error")

client.run(token)

