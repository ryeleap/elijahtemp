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
# current user name (not implemented)
user_name = None


# map from adjectives to nouns for elijah use
adjective_to_noun = {
    "greedy": "greed",
    "hungry": "hunger",
    "needy": "need",
    "sad": "sadness",
    "angry": "anger",
    "happy": "happiness",
    "anxious": "anxiety",
    "lonely": "loneliness",
    "jealous": "jealousy",
    "tired": "fatigue",
    "scared": "fear",
    "afraid": "fear",
    "confused": "confusion",
    "excited": "excitement",
    "bored": "boredom",
    "frustrated": "frustration",
    "disappointed": "disappointment",
    "proud": "pride",
    "ashamed": "shame",
    "embarrassed": "embarrassment",
    "grateful": "gratitude",
    "hopeful": "hope",
    "curious": "curiosity",
    "lonely": "loneliness",
    "angry": "anger",
    "jealous": "jealousy",
    "guilty": "guilt",
    "relaxed": "relaxation",
    "stressed": "stress",
    "worried": "worry",
    "goated": "goatedness"
}


patterns = [
    # sentence name response
    (r"(?:my )?(?:name(?: is|'s)|name) (\w+)\W*$",
     ["Hi {0}, just kidding... I don't really care. What do you want?"]),

    # single word name response
    (r"^(\w+)\W*$",
     ["Hi {0}, just kidding... I don't really care. What do you want?"]),
    
    # want to sentence response
    (r"(?:i )?want (.*)\W*$",
     ["Why do you want {0}?"]),
    
    # want to sentence response (about eliza)
    (r"(?:i )?want you to (.*)\W*$",
     ["Why do you want me to {0}?"]),
    
    # want to reasoning sentence response (with self adjective)
    (r"^(?:because(?: i am| i'm) )(\w+)\W*$",
     ["... Really? That's your reason? Oh well, can you tell me more about your {0}"]),

]

def elijah_response(user_input):
    # standardize in lowercase
    user_input = user_input.lower()

    # check each pattern in order of priority for matches
    for pattern, responses in patterns:
        match = re.match(pattern, user_input)
        if match:
            captured = match.group(1).lower()
            noun = adjective_to_noun.get(captured, captured)
            # respond if match
            response = responses[0].format(noun)
            # replaces refs with actual values ({0} -> riley, in "What is your name?")
            return response


print("ELIJAH: Hi, I'm (allegedly) a psychotherapist. What is your name?")

while True:
    user_input = input("> ")

    if user_input.lower() in ("bye"):
        print("ELIJAH: Goodbye.")
        break

    if(elijah_response(user_input)):
        print("ELIJAH:", elijah_response(user_input))
    else:
        print("What the hell are you talking about.")

        
