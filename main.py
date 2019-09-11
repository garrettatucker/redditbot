import praw
from PyDictionary import PyDictionary
import random
#import enchant
reddit = praw.Reddit(client_id='njqqRHMSxoD9hA',
                     client_secret='4Q_hJbXzrl2pqcjLCt9lKsglLAE',
                     username='TheCopperDimes',
                     password='T24ELu5s',
                     user_agent='<console:weird_bot:1.0 (by TheCopperDimes)>')

# dictionary and word check
dictionary = PyDictionary()
#d = enchant.Dict("en_US")

# check if the word is real
#def isWord(word):
#   return d.check(word)


subreddit = reddit.subreddit('Launchcodeproject2019')


keyphrase_1 = '!wordbot'
keyphrase_2 = '!jokebot'
keyphrase_3 = '!postbot'
keyphrase_4 = '!numberbot'




for comment in subreddit.stream.comments():
    if keyphrase_1 in comment.body:
        word = comment.body.replace(keyphrase_1, '')
        try:
            # get meaning as object, get the index of a sentence and reply it
            words = dictionary.meaning(word)
            reply = [item[0] for item in words.values()]
            comment.reply(word + ': '  + reply[0])
            print('posted')
        except:
            print('Some Sort of Error')
    if keyphrase_2 in comment.body:
        joke_list = ['I asked God for a bike, but I know God doesnt work that way so I stole a bike and asked for forgiveness.', 'I hate Russian dolls, theyre so full of themselves.', 'I recently decided to sell my vacuum cleaner as all it was doing was gathering dust.','You can never lose a homing pigeon - if your homing pigeon doesnt come back, what youve lost is a pigeon.']

        try:
            reply = random.choice(joke_list)
            comment.reply(reply)
            print('posted')
        except:
            print('Some Sort of Error')
    if keyphrase_3 in comment.body:
        title = 'This Post is Different for Everyone who Clicks it (Probably).'
        url = 'https://en.wikipedia.org/wiki/Special:Random'
        try:
            comment.reply('Thanks, I almost forgot to post another link!')
            print('posted reply')
            subreddit.submit(title, url=url)
            print ('posted new post')
        except:
            print('Some Sort of Error')

    if keyphrase_4 in comment.body:
        try:
            reply = random.randint(1,21)
            comment.reply(reply)
            print('posted')
        except:
            print('Some Sort of Error')

