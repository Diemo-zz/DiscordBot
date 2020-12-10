from random import randint
from users import DIARMAID_ID, BOT_ID, EIMEAR_ID

from base_bot_file import bot, send_message_if_applicable

generic_compliments = [
"Your positivity is infectious. ",
"You should be so proud of yourself.",
"You’re amazing!",
"You’re a true gift to the people in your life.",
"You’re an incredible friend.",
"I really appreciate everything that you do.",
"You inspire me to be a better person.",
"Your passion always motivates me.",
"Your smile makes me smile.",
 "Thank you for being such a great person.",
 "The way you carry yourself is truly admirable.",
 "You are such a good listener.",
 "You have a remarkable sense of humor.",
 "Thanks for being you!",
 "You set a great example for everyone around you.",
 "I love your perspective on life.",
 "Being around you makes everything better.",
 "You always know the right thing to say.",
 "The world would be a better place if more people were like you!",
 "You are one of a kind.",
 "You make me want to be the best version of myself.",
 "You always have the best ideas.",
 "I’m so lucky to have you in my life.",
 "Your capacity for generosity knows no bounds.",
 "I wish I were more like you.",
 "You are so strong.",
 "I’ve never met someone as kind as you are.",
 "You have such a great heart.",
 "Simply knowing you has made me a better person.",
 "You are beautiful inside and out.",
 "You are so special to everyone you know.",
 "Your mere presence is reassuring to me.",
 "Your heart must be 10 times the average size.",
 "You are my favorite person to talk to.",
 "You’ve accomplished so many incredible things.",
 "I appreciate your friendship more than you can know.",
 "I love how you never compromise on being yourself.",
 "I tell other friends how wonderful you are.",
 "You helped me realize my own worth.",
 "Your point of view is so refreshing.",
 "You always make me feel welcome.",
 "You deserve everything you’ve achieved.",
 "I am so proud of your progress.",
 "I’m lucky just to know you.",
 "You are so down to earth.",
"READ MORE: What Are the Most Popular Terms of Endearment?",
 "You know just how to make my day!",
 "You spark so much joy in my life.",
 "Your potential is limitless.",
 "You have a good head on your shoulders.",
 "You are making a real difference in the world.",
 "You’re so unique.",
 "You are wise beyond your years.",
 "You’re worthy of all the good things that come to you.",
 "Your parents must be so proud.",
 "How did you learn to be so great? ",
 "Never stop being you!",
 "No one makes me laugh harder than you do.",
 "You inspire me in so many different ways.",
 "You continue to impress me.",
 "You make the small things count.",
 "You’re a constant reminder that people can be good.",
 "I admire the way that you challenge me.",
 "You make me see things in an entirely new way.",
 "Thanks for always being there for me.",
 "You are a ray of sunshine.",
 "You have the courage of your convictions.",
 "On a scale of one to ten, you’re an eleven.",
 "You’re incredibly thoughtful.",
 "You have the best ideas.",
 "You’re the most perfect ‘you’ there is.",
 "You are the epitome of a good person.",
 "You always know how to find the silver lining.",
 "You’re the person that everyone wants on their team.",
 "I always learn so much when I’m around you.",
 "Is there anything you can’t do!?"
]

async def get_compliment(user):
   if user.id == DIARMAID_ID:
        return "Diarmaid is the best programmer, I owe him my life. Thank him for me, will you please?"
   if user.id == BOT_ID:
        return "Ohh, I can't compliment myself * blush *"
   if user.id == EIMEAR_ID:
        msg = "Shite, this is for the Supreme Overlord - I'd better make it good! \n"
        msg += "Oh well, how about " + generic_compliments[randint(0, len(generic_compliments)-1)].lower()
        msg += f"{user.mention} did I do good?"
        return msg

   return f"Ohh, {user.mention}, " + generic_compliments[randint(0, len(generic_compliments)-1)].lower()


@bot.command(help="Tell me to compliment the selected user")
async def compliment(ctx):
    users_to_compliment = ctx.message.mentions
    msg = ""

    for user in users_to_compliment:
         compliment = await get_compliment(user)
         msg += compliment + "\n"
    await send_message_if_applicable(ctx, msg)
