import json
from channels.generic.websocket import AsyncWebsocketConsumer


class StoryConsumer(AsyncWebsocketConsumer):
    connected_users = {}

    async def connect(self):
        self.story_id = self.scope['url_route']['kwargs']['story_id']
        self.story_group_name = f'story_{self.story_id}'

        await self.channel_layer.group_add(
            self.story_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        if self.story_group_name in self.channel_layer.groups:
            await self.channel_layer.group_discard(
                self.story_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'join':
            story_id = data.get('story_id')
            character_id = data.get('character_id')

            self.connected_users[character_id] = character_id

            response_data = {
                story_id: story_id,
                character_id: character_id,
            }
            await self.channel_layer.group_send(
                self.story_group_name,
                {
                    'type': 'user_joined',
                    'data': response_data
                }
            )

        elif action == 'disconnect_user':
            character_id = data.get('character_id')
            del self.connected_users[character_id]

            response_data = {
                character_id: character_id,
            }
            await self.channel_layer.group_send(
                self.story_group_name,
                {
                    'type': 'user_disconnected',
                    'data': response_data
                }
            )

    async def user_disconnected(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))

    async def user_joined(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))
