from fbchat import Client, log
from fbchat.models import *
import serial
import sys

ser = serial.Serial('serial_port', 9600)

class NotificationClient(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)

        # send 'stop' to yourself in messanger to stop program from running
        if author_id == self.uid:
            if message_object.text == 'stop':
                sys.exit()

        if author_id == self.track_id:
            ser.write('1'.encode('utf-8'))
    
    def onMarkedSeen(self, threads, **kwargs):
        if threads[0][0] == self.track_id:
            ser.write('0'.encode('utf-8'))
        

client = NotificationClient('username', 'password') # your login info
users = client.searchForUsers('user_you_want_to_listen')
client.track_id = users[0].uid

client.listen()
