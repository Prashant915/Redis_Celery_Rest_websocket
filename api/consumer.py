from channels.consumer import SyncConsumer,AsyncConsumer

#sync consumer
class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("Websocket Connect")

    def websocket_received(self,event):
        print("Websocket Received")
    
    def websocket_disconnect(self,event):
        print("Websocket Disconnect")

#async consumer
class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Websocket Connect")

    async def websocket_received(self,event):
        print("Websocket Received")
    
    async def websocket_disconnect(self,event):
        print("Websocket Disconnect")