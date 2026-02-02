import re

"""
Regex Cheatsheet for ELIZA

Basic Characters:
-----------------
.       : any character except newline
\w      : word character (letter, digit, underscore)
\W      : non-word character (anything not \w)
\d      : digit
\D      : non-digit
\s      : whitespace (space, tab, newline)
\S      : non-whitespace

Quantifiers:
------------
*       : 0 or more
+       : 1 or more
?       : 0 or 1 (optional)
{n}     : exactly n
{n,}    : n or more
{n,m}   : between n and m

Anchors:
--------
^       : start of string
$       : end of string

Groups:
-------
(...)       : capturing group
(?:...)     : non-capturing group
|           : OR (alternation)

Character Classes:
------------------
[A-Za-z]    : letters only
[A-Za-z0-9] : letters and digits
[^abc]      : anything except a, b, or c

"""
# current user name (memory, not implemented)
global userName, nameActive
nameActive = True

# map from adjectives to nouns for elijah use
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

pronoun_to_pronoun = {
    "i": "you",
    "me": "you",
    "my": "your",
    "mine": "yours",
    "myself": "yourself",
    "you": "me",
    "your": "my",
    "yours": "mine",
    "yourself": "myself"
}

namePatterns = [
    # sentence name response
    (r"(?:my )?(?:name(?: is|'s)|name) (\w+)\W*$",
     ["Hi {0}, just kidding... I don't really care. What do you want?"]),

    # single word name response
    (r"^(\w+)\W*$",
     ["Hi {0}, just kidding... I don't really care. What do you want?"]),
]

regPatterns = [
    # want to sentence response
    (r"(?:i )?want (.*)\W*$",
     ["Why do you want {0}?"]),
    
    # want to sentence response (about eliza)
    (r"(?:i )?want you to (.*)\W*$",
     ["Why do you want me to {0}?"]),
    
    # want to reasoning sentence response (with self adjective)
    (r"^(?:because(?: i am| i'm| im) )(.+)\W*$",
     ["... Really? That's your reason? Oh well, can you tell me more about how you're {0}"]),
    
    # want to reasoning sentence response (with verb)
    (r"^(?:because(?: i )(.+))$",
     ["... Really? That's your reason? Oh well, can you tell me more about how you {0}"]),

    
    # I'm x because y 
    # How do you feel about y?
]

def elijah_name_response(user_input):
    global userName, nameActive
    # check each pattern in order of priority for matches
    for pattern, responses in namePatterns:
        match = re.match(pattern, user_input)
        if match:
            captured = match.group(1).lower()
            noun = adjective_to_noun.get(captured, captured)
            # respond if match
            response = responses[0].format(noun)
            # replaces refs with actual values ({0} -> riley, in "What is your name?")
            
            nameActive = 'True'
            userName = captured
            return response
        
def elijah_reg_response(user_input):
    global userName, nameActive
    # check each pattern in order of priority for matches
    for pattern, responses in regPatterns:
        match = re.match(pattern, user_input)
        if match:
            captured = match.group(1).lower()
            
            words = captured.lower().split()
            
            converted_words = [
                pronoun_to_pronoun.get(adjective_to_noun.get(word, word), word)
                for word in words
            ]

            # for word in converted_words:
                # print(word)
            noun_phrase = " ".join(converted_words)

            # respond if match
            response = responses[0].format(noun_phrase)
            # replaces refs with actual values ({0} -> riley, in "What is your name?")
            return response


print("ELIJAH: Hi, I'm (allegedly) a psychotherapist. What is your name?")

while True:
    user_input = input("> ").lower()
    if user_input in ("bye"):
        print("ELIJAH: Goodbye.")
        break
    
    nameResponse = elijah_name_response(user_input)
    regResponse = elijah_reg_response(user_input)
    
    if nameResponse and nameActive:
        print("ELIJAH:", nameResponse)
        nameActive = 'false'
        # print(nameActive)
    elif regResponse:
        print("ELIJAH:", regResponse)
    else:
        print("What the hell are you talking about.")

        
