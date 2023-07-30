import json
from channels.generic.websocket import AsyncWebsocketConsumer


class StoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Lógica de autenticação e autorização, se necessário
        print('Conectado')
        await self.accept()

    async def disconnect(self, close_code):
        # Lógica de desconexão, se necessário
        print('Desconectado')
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Aqui você pode lidar com as ações enviadas pelo cliente via WebSocket
        print(data)
        print('Received WebSocket message:', text_data)
        action = data.get('action')

        if action == 'join_story':
            # Lógica para processar a solicitação do cliente e enviar os dados da história
            story_id = data.get('story_id')
            # ... (obter os dados da história e personagens conectados)

            # Exemplo: enviar os dados da história de volta ao cliente
            response_data = {
                'action': 'join_story',
                'story_id': story_id,
                'story_data': {...},  # Dados da história aqui
                # Lista de personagens conectados aqui
                'connected_characters': [...],
            }
            await self.send(text_data=json.dumps(response_data))