import cleverbot
import uuid
from flotype.bridge import Bridge 

availableRooms = set() 

def generateRoom():
  room = uuid.uuid1()
  availableRooms.add(room)

def joinRoom():
  room = availableRooms.pop()
    
class ConnectObj(object):
  def connect(self, name, callback):
    print("haro "+ name )
    if len(availableRooms) > 0:
      joinRoom()
      callback("joined")
    else:
      generateRoom()	
      callback("created")


bridge = Bridge(api_key= 'cb0ec2c9')
bridge.publish_service('connect', ConnectObj())
bridge.connect()


