#run all of this in replit so you dont have to install webdrivers.
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import warnings
from discord.ext import commands
import discord, os, random, time
import random as ran
warnings.filterwarnings('ignore')
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
def _input(input_text):
	input_element.send_keys(input_text)
	input_element.send_keys(Keys.ENTER)
	time.sleep(4)
	response = driver.find_element_by_id('answer_0').text
	return(response)

conv = False

def str_check(inp):
	censor = False
	censfile = open('poopoo_words.txt', 'r')
	censlist = censfile.readlines()
	cens_list = []
	for i in censlist:
		i_ = i.strip('\n')
		cens_list.append(i_)
	inp = inp.lower()
	for wrd in cens_list:
		msg = inp.replace(" ", "")
		wrd = wrd.replace(" ", "")
		if wrd in msg	:
			censor = True
	if censor == True:	
		print("""

		----------------------------CENSORED----------------------------

		""")
	return censor

#-------------------------------------------------------------------------------------------------------------

#.env for DISCORD_TOKEN
TOKEN = os.environ["DISCORD_TOKEN"]
prefix = "!"
bot = commands.Bot(prefix)
client = discord.Client() 

@bot.event
async def on_ready():
	print("Bot is ready!")

webpage = 'http://p-bot.ru/en/'
page = driver.get(webpage)	
input_element = driver.find_element_by_id('user_request')
input_element.clear()

@bot.event
async def on_message(message):
	global conv
	if conv == True:
		if message.author != bot.user:
			print(message.author, message.content)
#-------------------------------------------------------------	
			msg = message.content		
			if msg[0] != "!" and msg[0] != ">":
				msg_ = message.content
				msg = _input(msg_)
				print("bot: " + msg)
				cens = str_check(msg)
				if cens == True:
					await message.channel.send("__**censored**__")
				else:
					await message.channel.send(msg[6:])
				chatlog = open('chatlog.txt', 'a')
				log = str("[" + str(message.author) + ", " + message.content + "], [" + msg + ", " + str(cens) + "] \n")
				chatlog.writelines(log)
				chatlog.close()
#-------------------------------------------------------------------			
			elif message.content == "!end":
				conv = False
				print("---ENDING---")
	elif conv == False:
		if message.content == "!ping":
			await message.channel.send("pong")
		if message.content == "!start":
			conv = True
			print("---STARTING---")
bot.run(TOKEN)
