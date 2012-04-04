#!/usr/bin/python
from Fchat import Fchat
from Deck import Deck

class Pokerbot(object):
    """
    A Poker bot for fchat
    """
    cname = "Poker Bot https://github.com/jippen/Fchat-poker"
    cversion = "0.1"

    #Set this to 0 to not reconnect, or the seconds to wait until reconnecting 
    reconnect = 60
    deck = Deck()

    def __init__(self):
        self.FC = Fchat()

    def loadConfigFile(self,filename):
        self.FC.loadConfigFile(filename)

    def addHandlers(self):
        #Add our additional handlers to fchat.
        #There may be a more elegant way to do this.
        #I have not found it.
        self.FC.handle_FRL = self.handle_FRL
        self.FC.handle_PRI = self.handle_PRI
        self.FC.handle_CIU = self.handle_CIU

    ###########################################################################
    ### handlers for bot behavior                                           ###
    ###########################################################################
    def handle_FRL(self,data):
        #If I am on the Friends list, I'm a possible admin user!
        self.adminUsers = data['characters']
    
    def handle_PRI(self,data):
        if data['character'] in self.adminUsers:
            self.adminCommand(data['character'],data['message'])
        else:
            self.normalCommand(data['character'],data['message'])
    
    def handle_CIU(self,data):
        #I was invited to a room
        if data['sender'] in self.adminUsers:
            self.FC.send('JCH',{'channel': data['channel']} )

    ###########################################################################
    ### Most bot logic goes here                                            ###
    ###########################################################################
    def adminCommand(self,character,command):
        if command == "!deal":
            c = self.deck.deal()
            hand = character + u': ' + ' '.join(c)
            self.FC.send_PRI(character,hand)
        else:
            r  ="\n"
            r +="Admin Help file\n"
            r +=self.cname + "\n"
            r +="!deal - Deals a hand\n"
            self.FC.send_PRI(character,r)

    def normalCommand(self,character,command):
        message = "Sorry, you are not an admin, I cannot help you."
        self.FC.send_PRI(character,message)

if __name__ == "__main__":
    bot = Pokerbot()
    bot.loadConfigFile('Pokerbot.conf')
    bot.addHandlers()
    bot.FC.connect()
