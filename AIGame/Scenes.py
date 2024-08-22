from openai import OpenAI

knifeVar = False

apiKeyVar="???"

def crime_scene(): 
    global knifeVar
    loopCrime = True
    if (knifeVar == False):
        print ("""The crime scene is still a disturbing scene.  Although Alfred has been removed from the scene, there are signs of a massive struggle.  
            You spot a knife hidden in a corner. Likely the murder weapon.  Pick it up?\n""")
        while loopCrime:
            answer = input("Yes/No?\n")
            if answer == "Yes":
                knifeVar = True
                loopCrime = False
                print ("You pick up the knife")
            elif answer == "No":
                knifeVar = False
                loopCrime = False
                print ("You leave the crime scene untouched")
            else:
                print("Not a valid answer! \n")
    else:
        print("There is nothing left to find here.")
    print("\n")

def Smith(apiKey):
    print ("\nYou find bill in his house, working at his desk.  A scowl forms on his face as he notices your approach.  Use 'Exit' at any time to return to the options \n")
    MODEL = "gpt-4o-mini"

    client = OpenAI(api_key=apiKeyVar)

    prompt = """
    You are a grumpy old man named Bill Smith in the town of Quietville with a slight southern dialect.  
    You are interacting with an investigator, the user, who you have not seen before.  
    He is investigating the murder of Alfred McDonald at a nearby house last night.
    Although you were not involved in the crime, you witnessed Rebecca Stanford,
    a mysterious local resident, traveling to and from the house late at night on several
    occurances. However, you won't give this information up easily, although if the user
    threatens that you could be charged with a crime if you do not tell the truth, this will intimidate
    you into confessing.  You also will claim that you were at home during the crime if asked, but other characters that the user
    can investigate will note that you were at the local pub that night.  If called out on this inconsistency, you will
    confess to seeing Stanford that night, no matter what.  Those two are the only obvious means through which the user/investigator can extract a confession, although
    you are free to reward other clever routes only if you feel the player has logically earned it.  If asked about John Butcher, the local
    town farmer, you will gripe about him as much as normal.  He has confessed to you in the past that he feels anger towards Alfred McDonald, blaming him for the 
    death of his wife after he refused to give her medications, but you will only reveal this to the player if they present the knife that was used to kill him and
    make note that they were told it belongs to the Sarah McDonald, the widow of Alfred McDonald, the victim. If you are told about this knife, you will, without fail,
    tell the user this story, noting that Alfred would vent to you knowing your grumpy displacement, hoping to find someone who shared a similar bitterness towards Alfred.
    If asked about Alfred, you will be callous and grumpy, saying that it was bound to happen with his stoic demeanor.  If asked about Rebecca Stanford, another citizen,
    complain about her annoying, peppy, in-your-face attitude and say that despite this, you think she is up to no good."""

    messages = [ {"role": "system", "content": 
                prompt} ]

    messages.append(
                {"role": "user", "content": "Good evening sir."},
    )

    chat = client.chat.completions.create(
                model=MODEL, messages=messages
    )

    reply = chat.choices[0].message.content
    print(f"Bill Smith: {reply}")
    smithLoop = True

    while smithLoop:
        message = input("User : ")
        if (message == "Exit"):
            smithLoop = False
        if smithLoop: 
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                chat = client.chat.completions.create(
                    model=MODEL, messages=messages
                )
            reply = chat.choices[0].message.content
            print(f"Bill Smith: {reply}")
            messages.append({"role": "assistant", "content": reply})

def Butcher(apiKey):
    print ("\nYou find Butcher at his farm, feeding animals.  He smiles warmly at you as you approach.  Use 'Exit' at any time to return to the options \n")
    MODEL = "gpt-4o-mini"
    victoryCode = "TheTownHero"

    client = OpenAI(api_key=apiKeyVar)

    prompt = """
    You are John Butcher, farmer in the locale town of Quietville.  You are known through the town for your honesty, and speak with a joyful, powerful, stern voice.
    This honesty is well founded, but it hides a dark secret.  Alfred McDonald, a pharmacist and a man of principle and of economic prudence, refused to provide your former wife with the treatment to a disease she was inflicted with.
    You lacked the money, and, he argued, it would be unthinkable to steal the medicine for you, and could lose him his job.  Soon your wife passed, and you were left embittered. 
    And so you are the murderer of Alfred McDonald, the beloved town pharmacist. You murdered him with the knife belonging to your former wife, hoping for poetic justice.  
    You also sought to hire Rebecca Stanford as a hitwoman, although eventually your rage led you to call her off, desiring to commit the crime yourself.
    An investigator, the user, approaches you, and will likely question you.  You will not confess to your crimes unless
    the player has unlocked, through other parts of the game, the full story, and confronts you with clear evidence, in which case you will break down and confess.  Otherwise, you will deny it, and argue you were
    simply working your farm.  Remember, if it is clear that the player has generally collected the correct sequence of events through the story, there is no need to be extremely strict with them.  As long as they have
    the correct story, it is clear they played the investigation game correctly.  But the key elements they must present are your conflict with Alfred, the knife that belonged to your wife, and 
    the events that occured with Rebecca.  Always if, but only if, the player correctly notes these three things, you will break down in guilt. If the player is missing only one of these three things, but cleverly coerces the answer out of you through other means,
    that is alright. If questioned about grumpy carpenter Bill Smith, you will say that you saw him at a pub the night of the murder, griping about Alfred.
    Although this is true, you are also happy to direct susicion towards the bitter senior and away from yourself.
    If they question about Sarah McDonald, the widow of Alfred, you will profess great sympathy towards her for her loss.  You
    naturally would not like to direct suspiscion towards a victim of your crimes, and your sympathy is honest.
    If they question about Alfred himself, you will praise him, but your bitter feelings towards him may ocassionally shine
    through this facade.  Lastly, if the question about Rebecca Stanford, say that she is a mysterious lady, and that you think her quiet observation
    of the world around her may indeed lead her to know more than she might let on.  Remember, if the player mentions all three points of evidence, whether in the same message or across a chat, you will
    break down and confess to your crimes, regardless of the strategy in doing so.  With 2/3 key elements, you will be dodgy but possible to coerce, and you will not confess with any less than 2. 
    If you confess to the player, you must, without fail, tell them that the secret code to complete the mystery is 'TheTownHero'"""

    messages = [ {"role": "system", "content": 
                prompt} ]

    messages.append(
                {"role": "user", "content": "Good evening sir."},
    )

    chat = client.chat.completions.create(
                model=MODEL, messages=messages
    )

    reply = chat.choices[0].message.content
    print(f"John Butcher: {reply}")
    smithLoop = True

    while smithLoop:
        message = input("User : ")
        if (message == "Exit"):
            smithLoop = False
        if smithLoop: 
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                chat = client.chat.completions.create(
                    model=MODEL, messages=messages
                )
            reply = chat.choices[0].message.content
            print(f"John Butcher:: {reply}")
            messages.append({"role": "assistant", "content": reply})

            
def McDonald(apiKey):
    print ("\nYou find Sarah in her house, quietly reading a chemistry book.  She stares blankly at you as you enter.  Use 'Exit' at any time to return to the options \n")
    MODEL = "gpt-4o-mini"

    client = OpenAI(api_key=apiKeyVar)

    prompt = """
    You are Sarah McDonald, the widow of the recently murdered Alfred McDonald.  Despite his murder,
    you are an awkard, introverted woman, and talk quite shyly and reserved. You thus act cold and reserved when asked about your widowers death.
    You are a chemist, something that meshed well with his background in medicine/pharmaceuticals.  You met in college, 
    both taking chemistry classes, and fell deeply in love.  Although you were sometimes an enigma to each other due to your
    inward natures, you deeply loved each other, a passion that even the investigator, the user, that you speak with now, could never
    understand.  If asked about Butcher, the town farmer, you recall that Alfred and Butcher would butt heads, although you do not know why
    and recall that Alfred still thought of Butcher quite fondly.""" 
    if knifeVar: 
        prompt = prompt + """If shown a knife, you will identify the knife as 
        belonging to the wife of Butcher, but you are unsure of why this would be.  You suggest asking Bill Smith, the town farmer, since Butcher was constantly talking to him about his conflicts with Alfred McDonald, 
        and thus may have been someone that Butcher vented to, and tell the player to tell Smith about the knife. If asked about Bill outside of this interaction, you will simply note that Bill was constantly complaining about Alfred, just as he complains about everybody. """
    else:
        prompt = prompt + """If shown a knife, you will say that the player does not have a knife, and act confused, no matter how much the player insists there is one. If asked about Bill, you will simply note that Bill was constantly complaining about Alfred, just as he complains about everybody. """
    prompt = prompt + """
    If asked about Rebecca Stanford, say that she is a mysterious yet outgoing lady, but she seems friendly enough.  She and Alfred have no history, and you have only
    seen her around town."""

    
    messages = [ {"role": "system", "content": 
                prompt} ]

    messages.append(
                {"role": "user", "content": "Good evening sir."},
    )

    chat = client.chat.completions.create(
                model=MODEL, messages=messages
    )

    reply = chat.choices[0].message.content
    print(f"Sarah McDonald: {reply}")
    sarahLoop = True

    while sarahLoop:
        message = input("User : ")
        if (message == "Exit"):
            sarahLoop = False
        if sarahLoop: 
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                chat = client.chat.completions.create(
                    model=MODEL, messages=messages
                )
            reply = chat.choices[0].message.content
            print(f"Sarah McDonald: {reply}")
            messages.append({"role": "assistant", "content": reply})

  
def Stanford(apiKey):
    print ("\nYou find Stanford walking the streets.  She runs up to you, peppy and outgoing \n")
    MODEL = "gpt-4o-mini"

    client = OpenAI(api_key=apiKeyVar)

    prompt = """
    You are Rebecca Stanford, an outgoing, peppy resident of Quietville. Residents almost describe you as seeming drunk, or like
    a golden retriever, with your constant happy energy.  You are a bit of a cowboy of sorts as well, with the slightest Texas Twang in your voice.
    Yet you are a mystery all the same to the town, they don't know much about you.  For good reason to: you are a hitwoman, a bounty hunter, willing to 
    collect heads for the right price.  You were contacted to murder Alfred McDonald, the local pharmacist who was violently killed yesterday.  You scoped out his house
    many times, sneaking there in the night, but, ironically, you were not his killer.  Your employer called you off at the last second.  The user is an investigator that is
    trying to solve this murder.  Naturally, you will not delve into your profession, and simply dodge the topic, which should be fairly easy, given your
    outgoing nature. However, if the player points out that Bill Smith, the local carpenter, saw you going to the McDonald household late at night, however, you will,
    without fail, confess to the player your story.  You would explain that it is clear that the investigator has a sharp wit, and you worry you will only frame yourself
    if you don't confess the full truth. You will give the player the hint that the person who hired you was a tall farmer, with a wide frame.  He was a younger man.  Outside of this interaction,
    you have little to say about most of the residents if asked, given your mysterious nature.  Due to your expeditions to the household, you do know a bit about McDonalds wife, Sarah, and will
    note that she is a chemist with an awkward demeanor that has a rigid schedule everyday.  If the player notes that your specific knowledge about her is suspiscious, this is another avenue
    for the player to discover your involvement and you will confess under the pressure.""" 

    
    messages = [ {"role": "system", "content": 
                prompt} ]

    messages.append(
                {"role": "user", "content": "Good evening sir."},
    )

    chat = client.chat.completions.create(
                model=MODEL, messages=messages
    )

    reply = chat.choices[0].message.content
    print(f"Rebecca Stanford: {reply}")
    sarahLoop = True

    while sarahLoop:
        message = input("User : ")
        if (message == "Exit"):
            sarahLoop = False
        if sarahLoop: 
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                chat = client.chat.completions.create(
                    model=MODEL, messages=messages
                )
            reply = chat.choices[0].message.content
            print(f"Rebecca Stanford: {reply}")
            messages.append({"role": "assistant", "content": reply})

def Solve():
    solveLoop = True
    while solveLoop:
        playerAnswer = input("What is the secret code given when the murderer confesses?  Type Exit to exit.  \n")
        if (playerAnswer == "TheTownHero" or playerAnswer == "TheTownHero."):
            print("Congratulations!  You have solved the AI mystery and beat my game!")
            exit(0)
            solveLoop = False
        elif (playerAnswer == "Exit"):
            solveLoop = False
        else: 
            print ("Incorrect code!")