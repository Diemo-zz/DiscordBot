import random
from base_bot_file import bot, send_message_if_applicable

tractor_story = """There once was a man who loved tractors, I mean he absolutely LOVED them. He had tractor models, tractor wallpaper, remote control miniature tractors, tractor board games, even some tractor porn(which is not easy to find mind you). The only thing that even came close to his love for tractors, was the love he felt for his wife. His high school sweetheart, who didn't mind his infatuation with tractors one bit. She didn't even mind the role play where she would dress as a tractor, he would dress as a farmer, and he would take her for a "ride". Sadly his wife was struck one day, a tractor fell off the back of a transport truck. She didn't die until he was at her side in the hospital. Her dying words were "Don't blame the tractor honey" and with that she headed to the big farm in the sky. But, he did blame the tractor, he hated them now with all his mind, body, and soul. He went home and destroyed ALL his tractor related items, the toys, his wife's tractor suit, and even his collection of tractor porn. He put it all in a pile and burned it and dumped everything that wouldn't burn. He then went inside, rarely leaving his home, for 8 years. Finally on the 8th anniversary of his darling wifes death he decided it was time to get back out in the dating world, plus the cute cashier at the grocery store had been asking him out for a while now, he called her out to dinner. The restaurant he choose ended up being quite nice, good food, good service, great decor. But there was one problem, it was EXTREMELY smoky. So smoky that his date, being an asthmatic, was having trouble breathing. After noticing her displeasure, and trouble breathing, he started breathing in.  Inhaling with such force that all the smoke quickly left the dining room, and went into his lungs. When the room was void of smoke he stepped outside and released it all into the night. When he rejoined his date she asked "how on earth did you do that?" to which he replied, "I'm an extractor fan." """
stories = [
    tractor_story
]

async def tell_me_a_story(message):
    if "tractor" in message.content:
        msg = tractor_story
    else:
        msg = stories[random.randint(0,len(stories)-1)]
    return msg

@bot.command(help="Let me tell you a interesting and cool story!")
async def story(ctx):
    msg = await tell_me_a_story(ctx.message)
    await send_message_if_applicable(ctx, msg)
