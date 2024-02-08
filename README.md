# messagedog

![Made with https://hotpot.ai/art-generator](./resources/logo.png)

## Raffle bot

### Purpose

The application monitors the chat room of [admiralbulldog](https://www.twitch.tv/admiralbulldog) and
will automatically try to enter or leave raffles,
and answer trivia questions.
It is suggested that points are transferred ocassionally, to avoid suspicion...

### Installation

To execute:

```bash
python app.py
```

Alternatively:

```bash
pip install .
messagedog
```

### Configuration

| Variable          | Description        | Default Value | Best Case                                                                                                       |
| ----------------- | ------------------ | ------------- | --------------------------------------------------------------------------------------------------------------- |
| TWITCH_USER       | Twitch user id     |               | Name of the twitch user to log in as  id.                                                                       |
| TWITCH_PW         | Not needed         |               | Not needed currently, for future use.                                                                           |
| HOST              | HOST to connect to | localhost     | Not needed currently, for future use.                                                                           |
| DATABASE          | Not needed         |               | Not needed currently. However, for future use, a valid database connection string or name for storing messages. |
| TWITCH_AUTH_TOKEN | Twitch auth token  |               | A valid Twitch authentication token obtained from <https://twitchapps.com/tmi/>>.                               |
| TWITCH_CLIENT_ID  | Twitch client id   |               | A valid Twitch client id obtained from <https://dev.twitch.tv/console/apps/create>>.                            |

## WordCloud

This script accepts the a username, and generates a wordcloud of the
user's most common phrases and works over a certain month. It can be invoked with:

```bash
python3 scripts/generate_wordcloud.py <USER>
```
