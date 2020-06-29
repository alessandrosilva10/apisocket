from datetime import time

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.db import transaction

from . import models


class NoteConsumer(WebsocketConsumer):
    @transaction.atomic()
    def connect(self):
        self.room_group_name = 'notes'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    @transaction.atomic()
    def disconnect(self, close_code):
        # time.sleep(60000)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    @transaction.atomic()
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        title = text_data_json['title']
        content = text_data_json['content']
        id = text_data_json['id']

        note = models.Note.objects.get(pk=id)
        note.title = title
        note.content = content
        note.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'add_note',
                'title': title,
                'content': content,
                'id': id
            }
        )

    @transaction.atomic()
    def add_note(self, event):
        title = event['title']
        content = event['content']
        id = event['id']
        self.send(text_data=json.dumps({
            'title': title,
            'content': content,
            'id': id
        }))
