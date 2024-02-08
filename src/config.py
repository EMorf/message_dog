import os
from typing_extensions import Self
class Config:
    def __init__(self : Self) -> None:
        """Constructor for the Config class, responsible for ingesting configuration variables from the environment
        """        
        self.user = os.environ.get("TWITCH_USER", "")           # Twitch user id
        self.pwd  = os.environ.get("TWITCH_PW", "")             # not needed
        self.host = os.environ.get('HOST', "localhost")         # HOST to connect to, default is localhost
        self.db   = os.environ.get("DATABASE", "")              # not needed currently, plan is to store messages here
        self.oath = os.environ.get("TWITCH_AUTH_TOKEN", "")     # twitch auth token, get here https://twitchapps.com/tmi/
        self.clientid = os.environ.get("TWITCH_CLIENT_ID", "")  # twitch client id, get here  https://dev.twitch.tv/console/apps/create
        self.botlist = ['admiralbullbot', self.user]            # list of other bots in channel, user is added here for testing
