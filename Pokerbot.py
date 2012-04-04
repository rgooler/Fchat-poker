#!/usr/bin/python
# vim: set fileencoding=utf-8 :

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
        self.FC.handle_MSG = self.handle_MSG

    ###########################################################################
    ### handlers for bot behavior                                           ###
    ###########################################################################
    def handle_FRL(self,data):
        #If I am on the Friends list, I'm a possible admin user!
        self.adminUsers = data['characters']
    
    def handle_PRI(self,data):
        if data['character'] in self.adminUsers:
            self.adminPMCommand(data['character'],data['message'])
        else:
            self.normalPMCommand(data['character'],data['message'])
    
    def handle_CIU(self,data):
        #I was invited to a room
        #Is it a public or private channel? Who cares! Try both
        self.FC.send('JCH',{'channel': data['name']} )
        self.FC.send('JCH',{'channel': data['channel']} )

    def handle_MSG(self,data):
        #I got a message from a room
        if data['message'] == '!deal':
            print "Got deal command"
            print "channel|",data['channel']
            print "character|",data['character']
            self.commandCRdeal(data['channel'],data['character'])

    ###########################################################################
    ### Most bot logic goes here                                            ###
    ###########################################################################
    def adminPMCommand(self,character,command):
        #Parse commands for admins
        if command == '!deal':
            self.commandPMdeal(character)
        elif command.startswith('join'):
            self.FC.send('JCH',{'channel': command.lstrip('join ')} )
        else:
            self.adminPMHelp(character)

    def adminPMHelp(self,character):
        # Help docs for admins
        r  ="\n"
        r +="Admin Help file\n"
        r +=self.cname + "\n"
        r +="Invite me to a room to start playing\n"
        r +="!deal - Deals a hand\n"
        r +="join <room> - Join the channel <room>\n"
        self.FC.send_PRI(character,r)

    def normalPMCommand(self,character,command):
        #Parse commands for normalers
        if command == '!deal':
            self.commandPMdeal(character)
        else:
            self.normalPMHelp(character)

    def normalPMHelp(self,character):
        # Help docs for normalers
        r  ="\n"
        r +="Help file\n"
        r +=self.cname + "\n"
        r +="Invite me to a room to start playing\n"
        r +="Available commands in both rooms and PMs\n"
        r +="!deal - Deals a hand\n"
        self.FC.send_PRI(character,r)


    def command__deal(self):
        #Deal a hand of cards
        c = self.deck.deal()
        hand = c[0]+' '+c[1]+' '+c[2]+' '+c[3]+' '+c[4]
        return hand

    def commandPMdeal(self,character):
        # Deal cards as requested in a PM
        hand = self.command__deal()
        msg = '{"message":"'+hand+'","recipient":"'+character+'"}'
        self.FC.send_raw('PRI',msg)

    def commandCRdeal(self,room,character):
        # Deal cards as requested from a ChatRoom
        hand = character + ': ' + self.command__deal()
        msg = '{"message":"'+hand+'","channel":"'+room+'"}'
        self.FC.send_raw('MSG',msg)

if __name__ == "__main__":
    bot = Pokerbot()
    bot.loadConfigFile('Pokerbot.conf')
    bot.addHandlers()
    bot.FC.connect()
