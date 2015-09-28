__author__ = 'mBAR'
import pykka

class UsersHub(pykka.ThreadingActor):
    connectedUsers =  dict()
    print("UsersHub")
    def handelMessage(self,numberd,message ):

        print  ("ngg")
        if(not (numberd in self.connectedUsers) ):
            print("I dont have " +numberd)
