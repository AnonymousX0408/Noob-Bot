from bot.config import Telegram

WelcomeText = \
"""
Hi **%(first_name)s**, Just A Simple Bot By @ProCoderZBots
"""

SupportedEmojisText = \
"""
**I currently support following emojis:**
""" + '\n'.join(' '.join(Telegram.EMOJIS[i:i+5]) for i in range(0, len(Telegram.EMOJIS), 5))
