#!/usr/bin/python
# vim: set fileencoding=utf-8 :

from Fchat import Fchat
from Deck import Deck
import logging
import time
import daemonize

class Pokerbot(object):
    """
    A Poker bot for fchat
    """
    cname = "Poker Bot https://github.com/jippen/Fchat-poker"
    cversion = "0.2"

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
        time.sleep(3)

    def handle_MSG(self,data):
        #I got a message from a room
        if data['message'] == '!deal':
            self.commandCRdeal(data['channel'],data['character'])
            time.sleep(1)
        if data['message'] == '!rules':
            message = """For rolling purposes- !deal

            Literacy is a MUST! If players begin to complain of your literacy, you will be asked once to improve your grammar and spelling, and after that there is a possibility of being kicked.

            Have fun! This is a game meant to have fun! So try to show your teasing side a bit, okay? Unless you don't have fun doing that. Then... just show us something!

            Also, please be courteous and if your intentions are more than just teasing or flirting, take it to another room so as to not interrupt the flow of the game too much!

            1. Five pieces of clothing at a minimum. There is no SET maximum, but it's recommended not to go over eight pieces. One accessory is allowed per person.

            2. The round starts once the dealer says 3, 2, 1 (or some variant of it). Once 1 is said, the players roll. If you roll before hand, your roll will be negated and you must re-roll.

            3. Once the dealer calls the winning hand (PLEASE refrain from calling it before the dealer! Help is appreciated in PMs, but it's confusing on occasion when someone other than the dealer calls the hands!) the person who wins picks one person to remove one piece of clothing. The winner is allowed to suggest a piece of clothing to be removed, but what piece is removed is ultimately the decision of the one removing it.

            4. If it is the last piece of the person called, the one who called it removes it themselves. The naked person is then removed from play, to either sit on the lap of the person who called them, or have them sit on their lap. (Optional)

            5. The game continues until one person is left clothed. Good luck, and have fun!
            """
            self.FC.send('MSG',{'channel':data['channel'],'message': message})
            time.sleep(1)

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

def mainf():
    logging.basicConfig(format="%(asctime)s [%(levelno)s] %(funcName)s - %(message)s",
                        datefmt='%Y-%m-%dT%H:%M:%S%z',
                        filename='Pokerbot.log',
                        filemode='a',
                        level=logging.DEBUG
                        )
    logging.warning("Program Started")

    bot = Pokerbot()
    bot.loadConfigFile('Pokerbot.conf')
    bot.addHandlers()
    bot.FC.connect()


if __name__ == "__main__":
    daemonize.daemonize(mainf,'pokerbot.pid')
