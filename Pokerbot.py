#!/usr/bin/python
from Fchat import Fchat

class Pokerbot(object):
    """
    A Poker bot for fchat
    """
    cname = "Poker Bot https://github.com/jippen/Fchat-poker"
    cversion = "0.1"

    #Set this to 0 to not reconnect, or the seconds to wait until reconnecting 
    reconnect = 60
    
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
        
    ###########################################################################
    ### Most bot logic goes here                                            ###
    ###########################################################################
    def adminCommand(self,character,command):
        r  ="\n"
        r +="Admin Help file\n"
        r +=self.cname + "\n"
        
        self.FC.send_PRI(character,r)

    def normalCommand(self,character,command):
        message = "Sorry, you are not an admin, I cannot help you."
        self.FC.send_PRI(character,message)

if __name__ == "__main__":
    bot = Pokerbot()
    bot.loadConfigFile('Pokerbot.conf')
    bot.addHandlers()
    bot.FC.connect()
