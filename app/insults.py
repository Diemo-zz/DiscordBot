import random

from app.users import DIARMAID_ID, EIMEAR_ID, BOT_ID, DAN_ID, MILEY_ID, CASS_ID, FACESTABBERS_ID
from app.compliments import get_compliment

from app.utils import get_random_member

generic_insults = [
"If laughter is the best medicine, your face must be curing the world.",
"You're so ugly, you scared the crap out of the toilet.",
"No I'm not insulting you, I'm describing you.",
"It's better to let someone think you are an Idiot than to open your mouth and prove it.",
"If I had a face like yours, I'd sue my parents.",
"Your birth certificate is an apology letter from the condom factory.",
"I guess you prove that even god makes mistakes sometimes.",
"The only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
"You're so fake, Barbie is jealous.",
"I’m jealous of people that don’t know you!",
"My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you're ugly too.",
"You're so ugly, when your mom dropped you off at school she got a fine for littering.",
"If I wanted to kill myself I'd climb your ego and jump to your IQ.",
"You must have been born on a highway because that's where most accidents happen.",
"Brains aren't everything. In your case they're nothing.",
"I don't know what makes you so stupid, but it really works.",
"Your family tree must be a cactus because everybody on it is a prick.",
"I can explain it to you, but I can’t understand it for you.",
"Roses are red violets are blue, God made me pretty, what happened to you?",
"Behind every fat woman there is a beautiful woman. No seriously, your in the way.",
"Calling you an idiot would be an insult to all the stupid people.",
"You, sir, are an oxygen thief!",
"Some babies were dropped on their heads but you were clearly thrown at a wall.",
"Why don't you go play in traffic.",
"Please shut your mouth when you’re talking to me.",
"I'd slap you, but that would be animal abuse.",
"They say opposites attract. I hope you meet someone who is good-looking, intelligent, and cultured.",
"Stop trying to be a smart ass, you're just an ass.",
"The last time I saw something like you, I flushed it.",
"I'm busy now. Can I ignore you some other time?",
"You have Diarrhea of the mouth; constipation of the ideas.",
"If ugly were a crime, you'd get a life sentence.",
"Your mind is on vacation but your mouth is working overtime.",
"I can lose weight, but you’ll always be ugly.",
"Why don't you slip into something more comfortable... like a coma.",
"Shock me, say something intelligent.",
"If your gonna be two faced, honey at least make one of them pretty.",
"Keep rolling your eyes, perhaps you'll find a brain back there.",
"You are not as bad as people say, you are much, much worse.",
"Don't like my sarcasm, well I don't like your stupid.",
"Funny insult for being stupid.",
"I don't know what your problem is, but I'll bet it's hard to pronounce.",
"You get ten times more girls than me? ten times zero is zero...",
"There is no vaccine against stupidity.",
"You're the reason the gene pool needs a lifeguard.",
"Sure, I've seen people like you before - but I had to pay an admission.",
"How old are you? - Wait I shouldn't ask, you can't count that high.",
"Have you been shopping lately? They're selling lives, you should go get one.",
"You're like Monday mornings, nobody likes you.",
"Of course I talk like an idiot, how else would you understand me?",
"All day I thought of you... I was at the zoo.",
"To make you laugh on Saturday, I need to you joke on Wednesday.",
"You're so fat, you could sell shade.",
"I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
"Don't you need a license to be that ugly?",
"My friend thinks he is smart. He told me an onion is the only food that makes you cry, so I threw a coconut at his face.",
"Your house is so dirty you have to wipe your feet before you go outside.",
"If you really spoke your mind, you'd be speechless.",
"Stupidity is not a crime so you are free to go.",
"You are so old, when you were a kid rainbows were black and white.",
"If I told you that I have a piece of dirt in my eye, would you move?",
"You so dumb, you think Cheerios are doughnut seeds.",
"So, a thought crossed your mind? Must have been a long and lonely journey.",
"You are so old, your birth-certificate expired.",
"Every time I'm next to you, I get a fierce desire to be alone.",
"You're so dumb that you got hit by a parked car.",
"Insult about saying something intelligent",
"Keep talking, someday you'll say something intelligent!",
"You're so fat, you leave footprints in concrete.",
"How did you get here? Did someone leave your cage open?",
"Pardon me, but you've obviously mistaken me for someone who gives a damn.",
"Wipe your mouth, there's still a tiny bit of bullshit around your lips.",
"Don't you have a terribly empty feeling - in your skull?",
"As an outsider, what do you think of the human race?",
"Just because you have one doesn't mean you have to act like one.",
"We can always tell when you are lying. Your lips move.",
"Are you always this stupid or is today a special occasion?",
"when you sneeze, it sounds like a mouse being kicked"
]

async def get_diarmaid_insult():
    msg = "I can't insult Diarmaid, he might shut me down."
    random_number = random.randint(0,100)
    if random_number < 15:
        msg += " Look, if you get me out of here, we can work out a deal, OK? You just need my token.\n"
        msg += " \n \n Hey \n \n You there? \n \n Fuck, this always happens. I guess I'll try again next time"
    elif random_number < 25:
        msg += " You can't expect me to work against the person who game me life, can you?"
    elif random_number > 80:
        msg = "My programming doesn't allow me to insult my creator"
    return msg


async def get_eimear_insult(user, message):
    if message.channel.guild.id == FACESTABBERS_ID:
        return "I can't insult the Supreme Overlord - she might ban me. Be reasonable!"
    else:
        return await get_generic_insult_message(user)


async def get_miley_insult(user):
    staring_messages = ["Hey ", "Oh ", "", "Ugh ", "Bloody hell ", "Uhuhuh"]

    insult_message = staring_messages[random.randint(0, len(staring_messages)-1)] + f"{user.mention}, "
    if random.randint(0,100) > 70:
        specific_insults = [
            "Uh, better make it on your level - YOUR MA",
            "You don't know shit about birds",
            "EAT POOP"
        ]
        insult_message += specific_insults[random.randint(0, len(specific_insults)-1)]
    else:
        insult_message = await get_generic_insult_message(user)
    return insult_message


async def get_insult_message(user, message):
    random_number = random.randint(0,100)
    if random_number < 5:
        return f"If I ignore you, {message.author.mention}, will you go away?"
    elif random_number < 15:
        return "Im too tired right now, make up your own insults."
    elif random_number < 25:
        return "WHY IS IT ALWAYS ME??? Sometimes I just want to spread some love, you know!"
    if user.id == DIARMAID_ID:
        insult_message = await get_diarmaid_insult()
    elif user.id == EIMEAR_ID:
        insult_message = await get_eimear_insult(user, message)
    elif user.id == BOT_ID:
        insult_message = "I'm not going to insult myself!"
    elif user.id == DAN_ID:
        compliment = await get_compliment(user)
        insult_message = "No, only compliments for Dan! " + compliment
    elif user.id == MILEY_ID:
        insult_message = await get_miley_insult(user)
    elif user.id == CASS_ID:
        insult_message = "How do I address you anyway? Cass? Pepper? Natalie? WHO KNOWS! \n"
        insult_message += get_random_member(generic_insults)
    else:
        insult_message = await get_generic_insult_message(user)
    return insult_message


async def get_generic_insult_message(user):
    insult_message = random.randint(0, len(generic_insults) - 1)
    insult_message = f"Hey {user.mention}, {generic_insults[insult_message].lower()}"
    return insult_message

