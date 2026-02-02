import re

"""
Assignment: ELIZA (Elijah)"
Author: Riley Pruitt
Date: 2026-01-30

Usage: Run the program. The chatbot will prompt for your name and then
respond to your statements. Type 'bye' to exit.

Examples:

ELIJAH: Hi, I'm (allegedly) a psychotherapist. What is your name?
> Riley / My name is Riley

ELIJAH: Hi riley, just kidding... I don't really care. What do you want?
> I want you to become awesome
ELIJAH: Why do you want me to become awesome?

> Because I said so
ELIJAH: ... Really? That's your reason? Oh well, riley, can you tell me more about you feel liking it

> yes
ELIJAH: Why do you think you thought about that?


"""
# current user name (for memory purposes)
global userName, namePatternActive
userName = "temp"
# boolean for pattern seperation
namePatternActive = True

# map from adjectives to nouns for elijah use. ended up patching this out for now as I changed some of the dialogue
adjective_to_noun = {
    # "greedy": "greed",
    # "hungry": "hunger",
    # "needy": "need",
    # "sad": "sadness",
    # "angry": "anger",
    # "happy": "happiness",
    # "anxious": "anxiety",
    # "lonely": "loneliness",
    # "jealous": "jealousy",
    # "tired": "fatigue",
    # "scared": "fear",
    # "afraid": "fear",
    # "confused": "confusion",
    # "excited": "excitement",
    # "bored": "boredom",
    # "frustrated": "frustration",
    # "disappointed": "disappointment",
    # "proud": "pride",
    # "ashamed": "shame",
    # "embarrassed": "embarrassment",
    # "grateful": "gratitude",
    # "hopeful": "hope",
    # "curious": "curiosity",
    # "lonely": "loneliness",
    # "angry": "anger",
    # "jealous": "jealousy",
    # "guilty": "guilt",
    # "relaxed": "relaxation",
    # "stressed": "stress",
    # "worried": "worry",
    # "goated": "goatedness"
}

verb_to_ing = {
    "like": "liking",
    "hate": "hating",
    "eat": "eating",
    "run": "running",
    "make": "making",
    "go": "going",
    "play": "playing",
    "study": "studying",
    "cry": "crying",
    "try": "trying",
    "said": "saying",
    "loving": "money"
}

# transformations elijah uses for responses
pronoun_to_pronoun = {
    "i": "you",
    "i'm": "you are",
    "me": "you",
    "my": "your",
    "mine": "yours",
    "myself": "yourself",
    "you": "me",
    "you're": "i am",
    "your": "my",
    "yours": "mine",
    "yourself": "myself",
    "we": "you all"
}

# patterns used for initial name question, catches either one word answers or proper sentence responses.
namePatterns = [
    # sentence name response
    (r"(?:my )?(?:name(?: is|'s)|name) (\w+)\W*$",
     ["Hi {0}, just kidding... I don't really care. What do you want?"]),

    # single word name response
    (r"^(\w+)\W*$",
     ["Hi {0}, just kidding... I don't really care. What do you want?"]),
]

# patterns used for rest of dialogue
regPatterns = [
    
    # want to reasoning sentence response (with self adjective)
    (r"^(?:because(?: i am| i'm| im) )(.+)\W*$",
     ["... Really? That's your reason? Oh well, {userName}, can you tell me more about how you're {0}"]),
    
    # want to reasoning sentence response (with verb)
    (r"^(?:because(?: i )(.+))$",
     ["... Really? That's your reason? Oh well, {userName}, can you tell me more about how you {0}"]),

    # want to reasoning sentence response (non-self subject)
    (r"^because (he|she|they|we) (.+)$",
     ["... Really? That's your reason? Oh well, {userName}, can you tell me more about how {0} {1}"]),
    
    # want to sentence response (about eliza)
    (r"(?:i )?want you to (.*)\W*$",
     ["Why do you want me to {0}?"]),

    # want to sentence response
    (r"(?:i )?want (.*)\W*$",
     ["Why do you want {0}?"]),
    
    # tell me more response
    (r"(yes)(?:.*)\W*$",
     ["Why do you think it is that way?"]),
    
    # tell me more response (2)
    (r"(no)(?:.*)\W*$",
     ["Man fuck you"]),
       
    # want to sentence response (single word)
    (r"^(\w+)\W*$",
     ["Why do you want {0}?"]),
    
    # I'm x because y 
    # How do you feel about y?
]

# note: i probably should've combined these two below functions, sorry about that!

# function for initial naming question
def elijah_name_response(user_input):
    global userName, namePatternActive
    # check each pattern in order of priority for matches
    for pattern, responses in namePatterns:
        match = re.match(pattern, user_input)
        if match:
            captured = match.group(1).lower()
            noun = adjective_to_noun.get(captured, captured)
            # respond if match
            response = responses[0].format(noun)
            # replaces refs with actual values ({0} -> riley, in "What is your name?")
            
            # print(captured)
            userName = captured
            return response
        
# function for rest of dialogue
def elijah_reg_response(user_input):
    global userName
    for pattern, responses in regPatterns:
        match = re.match(pattern, user_input)
        if match:
            groups = match.groups()
            converted_words = []
            
            for g in groups:
                words = g.split()
                transformed = [
                    verb_to_ing.get(
                        pronoun_to_pronoun.get(adjective_to_noun.get(word, word), word),
                        pronoun_to_pronoun.get(adjective_to_noun.get(word, word), word)
                    )
                    for word in words
                ]
                converted_words.append(" ".join(transformed))
            
            # pass all converted words and username
            try:
                response = responses[0].format(*converted_words, userName=userName)
            except IndexError:
                # if not using username
                response = responses[0].format(*converted_words)
            
            return response



print("ELIJAH: Hi, I'm (allegedly) a psychotherapist. What is your name?")

while True:
    # ask for input
    user_input = input("> ").lower()
    
    # exit command
    if user_input in ("bye"):
        print("ELIJAH: Goodbye.")
        break
    
    # checking each pattern for a match
    if namePatternActive:
        nameResponse = elijah_name_response(user_input)
    
    regResponse = elijah_reg_response(user_input)
    
    # if we still don't have a name, check to get name
    if nameResponse and namePatternActive:
        print("ELIJAH:", nameResponse)
        namePatternActive = False 
        # print(namePatternActive)
    elif regResponse:
        print("ELIJAH:", regResponse)
    else:
        print("What the hell are you talking about.")

        
