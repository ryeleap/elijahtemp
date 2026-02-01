import re

patterns = [
    (r'my name is (\w+)\W*$', 
     ["Hi {0}, what can I do for you today?"]),
    
]

def elijah_response(user_input):
    user_input = user_input.lower()

    for pattern, responses in patterns:
        match = re.match(pattern, user_input)
        if match:
            response = responses[0]
            return response.format(*match.groups())

print("ELIJAH: Hi, I'm a psychotherapist. What is your name?")

while True:
    user_input = input("> ")

    if user_input.lower() in ("bye"):
        print("ELIJAH: Goodbye.")
        break

    print("ELIJAH:", elijah_response(user_input))
