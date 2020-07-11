# Description: This is a chatbot program

#There are broadly two variants of chatbots: Rule-Based and Self learning.
#Rule-based approach, a bot answers questions based on some rules on which it is trained on
#Self learning bots are the ones that use some Machine Learning-based approach to chat

#import libraries
from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is C.H.A.T.T.Y and I'm a chatbot.",]
    ],
    [
        r"(.*)are you(.*)",
        ["I'm doing very well", "i am great !",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that.Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["GAURAV and BHAVIKA created me using Python's NLTK library ,top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tokyo, Japan',]
    ],
    [
        r"(.*) (raining|rain) (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Basketball",]
    ],

    [
        r"who(.*) (moviestar|actor|actress)?",
        ["chrishemsworth"]
    ],

       [
        r"what (.*) (hobies|like|entertaining)?",
        ["singing,sports,movies etc",]
    ],

    
    [
        r"(quit|bye|goodbye|see you|tata)",
        ["Bye for now. See you soon :) It was nice talking to you. See you soon :)",]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
    
]

#This is a dictionary that contains a set of input values and its corresponding output values. 
#It is an optional dictionary that you can use unless you want to use regular expressions. 
reflections

{'i': 'you',
 'i am': 'you are',
 'i was': 'you were',
 "i'd": 'you would',
 "i'll": 'you will',
 "i'm": 'you are',
 "i've": 'you have',
 'me': 'you',
 'my': 'your',
 'you': 'me',
 'you are': 'I am',
 'you were': 'I was',
 "you'll": 'I will',
 "you've": 'I have',
 'your': 'my',
 'yours': 'mine'}

#Create your own reflections
my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

#default message at the start of chat
print("Hi, I'm Chatty and I chat a lot\nPlease type lowercase English language to start a conversation. Type quit to leave ") 

#Create Chat Bot
chat = Chat(pairs, reflections)

#chat._substitute('i am a programmer') #uncomment this line to see reflections example in action

#Start conversation
chat.converse()
