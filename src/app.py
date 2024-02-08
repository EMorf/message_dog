import irc.bot
import requests
from src.config import Config
import logging
import re
import time
from trivia_farmer import TriviaAnswer
import random


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, config: Config, channel: str, trivia: TriviaAnswer):
        self.botlist = config.botlist
        self.user = config.user
        self.client_id = config.clientid
        self.token = config.oath
        self.channel = "#" + channel
        self.question = ""
        self.trivia = trivia
        # Get the channel id, we will need this for v5 API calls
        url = "https://api.twitch.tv/kraken/users?login=" + channel
        headers = {
            "Client-ID": self.client_id,
            "Accept": "application/vnd.twitchtv.v5+json",
        }
        r = requests.get(url, headers=headers, timeout=10).json()
        self.channel_id = r["users"][0]["_id"]

        # Create IRC bot connection
        server = "irc.chat.twitch.tv"
        port = 6667
        print("Connecting to " + server + " on port " + str(port) + "...")
        irc.bot.SingleServerIRCBot.__init__(
            self, [(server, port, "oauth:" + self.token)], self.user, self.user
        )

    def on_welcome(self, connection, _):
        print("Joining " + self.channel)

        # You must request specific capabilities before you can use them
        connection.cap("REQ", ":twitch.tv/membership")
        connection.cap("REQ", ":twitch.tv/tags")
        connection.cap("REQ", ":twitch.tv/commands")
        connection.join(self.channel)

    # /me forces ctcp
    # TODO fix bug that forces sikzone to be handled by the first if statement for trivia
    def on_ctcp(self, connection, event):
        # Handle raffle results
        if event.source.split("!")[0].lower() in self.botlist:
            text = event.arguments[1]
            if self.user in text.lower().replace(",", "").split(" "):
                logging.warning(
                    "%s mentioned: %s", event.source.split("!")[0].lower(), text
                )
                m = re.search(r"won \d+ points?", text)
                if m:
                    logging.info("%s %s", self.user, m.group(0))
            elif text[:23] == "PogChamp A new question":
                m = re.findall(r"\".+?\"", text, flags=re.U)
                # Malformed text
                if len(m) != 2:
                    return
                _, question = m
                # Save the question temporarily, so we can extract the answer later
                self.question = question
                response = self.trivia.get_answer(question.strip('"'))
                # Set the below False to True to enable dming of the main bot, to circumvent timeouts
                # Potentially dangerous
                if response != " " and False:
                    time.sleep(random.uniform(4.5, 7))
                    # Around 20% chance of guessing correctly, might have to increase later
                    connection.privmsg(self.channel, response.lower())
            else:
                try:
                    text = text.replace('"', "")
                    m = re.search(r"The answer was .+? (FeelsGoodMan|MingLee)", text)
                    if not m:
                        return
                    ans = m.group(0)
                    for item in ["The answer was", "FeelsGoodMan", "MingLee"]:
                        ans = ans.replace(item, "")
                    ans = ans.strip()
                    self.trivia.set_data(self.question.strip('"'), ans)
                except Exception as ex:
                    logging.warning("%s", ex)
        return

    def on_pubmsg(self, _, event):
        """Handle all public messages in the IRC chat, if it starts with !, then handle it as a command.

        Args:
            c (Connection)
            e (Event)
        """
        # If a chat message starts with an exclamation point, try to run it as a command
        if event.arguments[0][:2] == "!r" or event.arguments[0][:2] == "!m":
            cmd = event.arguments[0].split(" ")[0][1:]
            self.do_command(event, cmd)

        # If the user doing the parsing is detected as being mentioned in the message, it is likely a reply from the main bot that we won points
        # hence, log the message
        if event.source.split("!")[0].lower() in self.botlist:
            text = event.arguments[0].replace(",", "")
            if self.user in text.lower().split(" "):
                logging.warning(
                    "%s mentioned: %s", event.source.split("!")[0].lower(), text
                )

                m = re.search(r"won \d+ points?", text)
                if m:
                    logging.info("%s %s", self.user, m.group(0))

        return

    def do_command(self, e, cmd):
        """Handle specific commands in the channel, command being a string of the format !<command> posted by a user

        Args:
            e (Event): Event data structure
            cmd (_type_): command without the exclamation mark in string form

        Returns:
            bool: True if all handled well, False if exception occured.
        """
        c = self.connection
        # Handle raffle
        if cmd in ["raffle", "multiraffle"] and int(e.tags[7]["value"]):
            try:
                elements = e.arguments[0].split(" ")
                logging.warning(
                    "User %s with role %s %s did a %s for %s points.",
                    e.source.split("!")[0],
                    e.tags[7]["key"],
                    e.tags[7]["value"],
                    elements[0][1:],
                    elements[1],
                )
                # Only join if the raffle is for a positive amount, otherwise the user loses points.
                if int(elements[1]) > 0:
                    time.sleep(0.5)
                    c.privmsg(self.channel, "!join")
                    logging.info("Raffle was entered")
                else:
                    logging.info("Raffle was not entered")
                return True
            except (ValueError, IndexError) as er:
                logging.warning(
                    "Raffle command: %s raised exception: %s", e.arguments[0], er
                )
                return False


def app():
    trivia = TriviaAnswer("stream")
    config = Config()
    bot = TwitchBot(config, "admiralbulldog", trivia)

    logging.basicConfig(
        filename="bot.logs",
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )

    bot.start()


if __name__ == "__main__":
    app()
