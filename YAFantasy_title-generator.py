import random

word_pool = {
    'forms': ['song','anthem','aria','ballad','canticle',
        'carol','chant','chorale','chorus','ditty',
        'hymn','lullaby','melody','number','oldie',
        'opera','piece','poem','psalm','refrain',
        'round','strain','tune','verse',
        'city','castle','tower','oath','promise',
        'tale','dungeon','treasure'
        ],
    'nouns': ['adventure','alchemy','amulets','ancients','angels',
        'armies','armour','arrows','autumn','axes',
        'barbarians','battles','beasts','bishops','blessings',
        'blood','bones','bows','bravery',
        'castles','cauldrons','caves','centaurs','chambers',
        'chariots','charms','claws','cliffs','combat',
        'conjuration','conspiracy','creatures','creeps','crossbows',
        'crowns','cults','curses','cyclopses',
        'darkness','daydreams','dazzle','deformities','demons',
        'destiny','devils','disappearances','digust','dragons',
        'dragonfire','dreams','druids','dungeons','dwarves',
        'eeriness','elves','enchanments','enchantresses','emeralds',
        'escape','evil','eyes',
        'fairies','fangs','fantasy','feasts','feathers',
        'figments','fire','flame','fog','folklore',
        'forests','fortunes','fright','frost',
        'gems','ghouls','giants','gloom','glory',
        'gnomes','goblins','gold','guardians',
        'hallucinations','hearts','herbs','hermits',
        'heroes','hills','horns','horror','horrors',
        'hounds','honor','hunts','hunters',
        'illusions','imagination','imperiums','islands',
        'jaws','jewels','journies',
        'kings','kingdoms','knights',
        'lairs','lakes','landscapes','lanterns','laws',
        'legends','leprechauns','lightning','locks','logic',
        'lords','lore',
        'magic','magical herbs','majesty','masters','mazes',
        'mermaids','messengers','midnight','might','ministry',
        'mirrors','mischief','mist','monsters','moonlight',
        'mountains','muck','mystics','myths','mythology',
        'necromancers','necromancy','nemeses','nightmares',
        'oddities','ogres','oracles','orphans',
        'passages','passageways','peculiarities','poison','portals',
        'power','princes','princesses','prophecies','puzzles',
        'queens','quests','quivers',
        'rainbows','realms','rebels','riddles','rings',
        'saints','sapphires','scars','secrets','seers',
        'shadow','shadows','silver','sin','sins',
        'skulls','slimes','smoke','soothsayers','sorcerers',
        'sorcery','snow','sparks','sparkles','spears',
        'spells','springtime','sprites','stars','stone','storms',
        'summer','summons','sunshine','swords','sworcery',
        'tails','tales','tangles','tentacles','thrones',
        'towers','transformation','trapdoors','traps','treasure',
        'trolls','twilight','twinkles',
        'ugliness','unicorn','unholiness',
        'vallies','vampires','vanishing','valor','venom',
        'viciousness','visions',
        'wands','warlocks','warriors','weirdos','werewolves',
        'whiskers','whimsy','whispers','wickedness','wildness',
        'wilderness','wings','winter','wisdom','wishes',
        'witches','witchcraft','wizards','wizardry','wolves',
        'woods','wrath','wraithes',
        'yams',
        ],
}


### main ###
random.seed(int(input('Enter a random number to begin: ')))
first_noun_index = random.randrange(0,33)
second_noun_index = random.randrange(0,244)
third_noun_index = random.randrange(0,244)

# check first word for vowel
first_noun_listed = list(word_pool['forms'][first_noun_index])

# capitalize proper nouns
first_noun = word_pool['forms'][first_noun_index]
first_noun_capital = first_noun.capitalize()

second_noun = word_pool['nouns'][second_noun_index]
secound_noun_capital = second_noun.capitalize()

third_noun = word_pool['nouns'][third_noun_index]
third_noun_capital = third_noun.capitalize()

# write results to text file
with open('title.txt', 'w') as file:
    file.write('~~~ YA Fantasy Novel Title ~~~\n\n')
    if first_noun_listed[0] in ['a','e','i','o','u']:
        file.write(f'An {first_noun_capital} of {secound_noun_capital} and {third_noun_capital}\n')
    else:
        file.write(f'A {first_noun_capital} of {secound_noun_capital} and {third_noun_capital}\n')
file.close()

# display generator output
print('\n~~~ Title ~~~')
if first_noun_listed[0] in ['a','e','i','o','u']:
    print(f'An {first_noun_capital} of {secound_noun_capital} and {third_noun_capital}\n')
else:
    print(f'A {first_noun_capital} of {secound_noun_capital} and {third_noun_capital}\n')

