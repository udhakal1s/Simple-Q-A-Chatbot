#simple chatbot progrma
#In this program chatbot reply back to human 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Initilize your chatbot
chatterbot = ChatBot("Chatbot Terminal")

# Using English language data to train chatbot
trainer = ChatterBotCorpusTrainer(chatterbot)
trainer.train("chatterbot.corpus.english")

#print statement
print("Start taking with chat bot or press ctrl + c to end the conversion")

while True:
    
    try:
        human = input("Human Response: ") #this is the human question and response
        chatbotreply = chatterbot.get_response(human) #AI response back
        print("Chatbot Response:", chatbotreply)
    except (KeyboardInterrupt, EOFError):
        print("\nTalk to you later") #when you end the conversation
        break
