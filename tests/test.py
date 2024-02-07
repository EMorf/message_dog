import re
import irc.bot
import irc
from .config import Config
import unittest


class TestStringMethods(unittest.TestCase):

    def on_pubmsg(self, e):
        # If a chat message starts with an exclamation point, try to run it as a command
        if e.source.split("!")[0].lower() in config.botlist:
            text = e.arguments[0].replace(",", "")
            if config.user in text.lower().split(" "):
                print("{} mentioned: {}".format(e.source.split("!")[0].lower(), text))
                m = re.search(r"won \d+ points?", text)
                if m:
                    print("{} {}.".format(config.user, m.group(0)))
                    return True
        return False

    def test_true(self):
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            [
                "/me ChaSiuBao026, euqine21, flash_pma, gacheeb, jellaldeys, NakedSnake336, ojoink, okaybruh322, paidamae, shattertide, SikZone, sodium_74, thief_free, toasted_mate, winifel, zeyden3000 won 6250 points each!"
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
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            [
                "/me SikZone, sodium_74, thief_free, toasted_mate, winifel, zeyden3000 won 6250 points each!"
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
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me SikZone, bro won 6250 points each!"],
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
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me SikZone won 6250 points each!"],
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
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, SikZone won 6250 points each!"],
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

    def test_false(self):
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
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, sikzone! won 6250 points each!"],
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
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, sikzone won -6250 points each!"],
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
        msg = irc.client.Event(
            "pubmsg",
            "admiralbullbot!admiralbullbot@admiralbullbot.tmi.twitch.tv",
            "#admiralbulldog",
            ["/me, sikzone won a points each!"],
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


if __name__ == "__main__":
    unittest.main()
