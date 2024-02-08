import re
import irc.bot
import irc
import unittest


class TestStringMethods(unittest.TestCase):
    """Test class to verify that the logic used to enter/skip raffles is correct."""

    botlist = ["admiralbullbot"]
    bot_username = "tisme"

    def on_pubmsg(self, e):
        """Essentially the same string manipulation logic as in main.py, but stub out the message channels and return booleans instead.
        Effectively a simulation of the main code.

        Args:
            e (Event): event element

        Returns:
            bool: True if the user won points, False otherwise
        """

        if e.source.split("!")[0].lower() in self.botlist:
            text = e.arguments[0].replace(",", "")
            if self.bot_username in text.lower().split(" "):
                print(f"{e.source.split('!')[0].lower()} mentioned: {text}")
                m = re.search(r"won \d+ points?", text)
                if m:
                    print(f"{self.bot_username} {m.group(0)}")
                    return True
        return False

    def test_won_raffle(self):
        """Test a winning raffle event with many users."""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            [
                "/me ChaSiuBao026, euqine21, flash_pma, gacheeb, jellaldeys, NakedSnake336, ojoink, okaybruh322, paidamae, shattertide, tisme, sodium_74, thief_free, toasted_mate, winifel, zeyden3000 won 6250 points each!"
            ],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), True)

    def test_won_raffle_2(self):
        """Yet another winning raffle event, with a few users."""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            [
                "/me tisme, sodium_74, thief_free, toasted_mate, winifel, zeyden3000 won 6250 points each!"
            ],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), True)

    def test_won_raffle_3(self):
        """Yet another winning raffle event with two users."""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me tisme, bro won 6250 points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), True)

    def test_won_raffle_4(self):
        """Yet another winning raffle event with just one (us) user."""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me tisme won 6250 points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), True)

    def test_won_raffle_5(self):
        """Yet another winning raffle event with just one (us) user, but with a comma separator at the start (occurs sometimes)."""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, tisme won 6250 points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), True)

    def test_no_one(self):
        """No one won the raffle"""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, No one won 6250 points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), False)

    def test_not_us(self):
        """Others won, but not us"""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, Some, Idiots, lol won 6250 points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), False)

    def test_almost(self):
        """Almost us, but not quite"""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, tisme! won 6250 points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), False)

    def test_won_but_lost(self):
        """We won a negative raffle, so we lost points..."""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, tisme won -6250 points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), False)

    def test_bugged(self):
        """Bugged message, edge case that might occur"""
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, tisme won a points each!"],
            [
                {"key": "badge-info", "value": "subscriber/15"},
                {"key": "badges", "value": "moderator/1,subscriber/12"},
                {"key": "color", "value": "#FF4500"},
                {"key": "display-name", "value": "AdmiralBullBot"},
                {"key": "emotes", "value": None},
                {"key": "flags", "value": None},
                {"key": "id", "value": "878bbd59-2e0a-4d3c-bf98-690bc4b372f0"},
                {"key": "mod", "value": "1"},
                {"key": "room-id", "value": "30816637"},
                {"key": "subscriber", "value": "1"},
                {"key": "tmi-sent-ts", "value": "1575511270289"},
                {"key": "turbo", "value": "0"},
                {"key": "user-id", "value": "254941918"},
                {"key": "user-type", "value": "mod"},
            ],
        )
        self.assertEqual(self.on_pubmsg(msg), False)
