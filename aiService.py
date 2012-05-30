import random
import cleverbot
import uuid
from flotype.bridge import Bridge 

availableRooms = set() 
aiRooms = {}

def generateRoom():
  room = uuid.uuid1()
  availableRooms.add(room)
  return str(room.int)

def joinRoom():
  room = availableRooms.pop()
  return str(room.int)

class CleverBotChat(object):
  def message(self, channel, sender, message, human):
    #tell cleverbot
    print 'message received'
    print channel
    if (human):
      msg = aiRooms[channel].Ask(message)
      chan = bridge.get_channel(channel)
      chan.message(channel, "Stranger", msg, False)
  def endGame(self,conditions):
    pass
    
class ConnectObj(object):
  def connect(self, name, callback):
    print("haro "+ name )
    if len(availableRooms) > 0:
      rand = random.randint(0,1)
      #rand = 1
      if (rand == 0):
        print "human player"
        room = joinRoom()
        callback({'type': "joined", 'channel' : room, 'role': 'tricker' })
        chan = bridge.get_channel(room)
        chan.startGame()
      else:
        print 'hopefully letting cleverbot in'
        room1 = joinRoom()
        aiRooms[room1] = cleverbot.Session()
        bridge.join_channel(room1, CleverBotChat())
        room2 = generateRoom()
        callback({'type': "created", 'channel': room2, 'role': 'guesser'})
    else:
      room = generateRoom()	
      callback({'type': "created", 'channel': room, 'role': 'guesser'})
  def guessRobot(self, isRobot, channel):
      chan = bridge.get_channel(channel)
      if ( (channel in aiRooms) and (isRobot) ):
          chan.endGame({'guess': True})
      elif ( (not (channel in aiRooms) ) and (not isRobot) ):
          chan.endGame({'guess': True})
      else:
          chan.endGame({'guess': False})
  

bridge = Bridge(api_key= 'cb0ec2c9')
bridge.publish_service('connect', ConnectObj())
bridge.connect()


