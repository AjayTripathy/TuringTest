import cleverbot
import uuid
from flotype.bridge import Bridge 

availableRooms = set() 

def generateRoom():
  room = uuid.uuid1()
  availableRooms.add(room)
  return str(room.int)

def joinRoom():
  room = availableRooms.pop()
  return room
    
class ConnectObj(object):
  def connect(self, name, callback):
    print("haro "+ name )
    if len(availableRooms) > 0:
      room = joinRoom()
      callback({'type': "joined", 'channel' : room})
    else:
      room = generateRoom()	
      callback({'type': "created", 'channel': room})
  

bridge = Bridge(api_key= 'cb0ec2c9')
bridge.publish_service('connect', ConnectObj())
bridge.connect()


