import sys
import irc.bot
import requests
import config
import logging
import re


class TwitchBot(irc.bot.SingleServerIRCBot):
	def __init__(self, username, client_id, token, channel):
		self.client_id = client_id
		self.token = token
		self.channel = '#' + channel

		# Get the channel id, we will need this for v5 API calls
		url = 'https://api.twitch.tv/kraken/users?login=' + channel
		headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
		r = requests.get(url, headers=headers).json()
		self.channel_id = r['users'][0]['_id']

		# Create IRC bot connection
		server = 'irc.chat.twitch.tv'
		port = 6667
		print('Connecting to ' + server + ' on port ' + str(port) + '...')
		irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)
	def on_welcome(self, c, e):
		print('Joining ' + self.channel)

		# You must request specific capabilities before you can use them
		c.cap('REQ', ':twitch.tv/membership')
		c.cap('REQ', ':twitch.tv/tags')
		c.cap('REQ', ':twitch.tv/commands')
		c.join(self.channel)

	def on_pubmsg(self, c, e):
		# If a chat message starts with an exclamation point, try to run it as a command
		if e.arguments[0][:2] == '!r' or e.arguments[0][:2] == '!m':
			cmd = e.arguments[0].split(' ')[0][1:]
			self.do_command(e, cmd)
		if e.source.split("!")[0].lower() in config.botlist:
			text = e.arguments[0].replace(",",'')
			if config.user in text.lower().split(" "):
				m = re.search(r'won \d+ points?', text)
				if m:
					logging.info("{} {}.".format(config.user, m.group(0)))
				else:
					logging.warning("{} mentioned: {}".format(config.user, text))
		return
		
	def do_command(self, e, cmd):
		c = self.connection
		# Handle raffle 
		if (cmd == "raffle" or cmd == "multiraffle") and int(e.tags[7]['value']):
			try:
				elements = e.arguments[0].split(' ')
				logging.warning("User {} with role {}{} did a {} for {} points.".format(e.source.split("!")[0],e.tags[7]['key'], e.tags[7]['value'], elements[0][1:], elements[1])) 
				if int(elements[1]) > 0:
					c.privmsg(self.channel, "!join")
					logging.info("Raffle was entered")
				else:
					logging.info("Raffle was not entered")
				return True
			except (ValueError, IndexError) as er:
				logging.warning("Raffle command: {} raised exception: {}".format(e.arguments[0], er))
				return False

def main():
	bot = TwitchBot(config.user, config.clientid, config.oath, "admiralbulldog")
	logging.basicConfig(filename='bot.logs',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	bot.start()

if __name__ == "__main__":
	main()