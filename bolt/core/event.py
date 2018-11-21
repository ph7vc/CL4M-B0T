"""
    Description:
        Class to handle event observers

    Contributors:
        - Patrick Hennessy
"""

import logging
from bolt.discord.events import Events


class Event():
    def __init__(self):
        pass

    @classmethod
    def from_message(cls, message):
        event = cls.to_object(message["d"])
        event.name = getattr(Events, message["t"])
        event.sequence = message["s"]

        return event

    @classmethod
    def to_object(cls, item):
        def convert(item):
            if isinstance(item, dict):
                return type('Event', (), {k: convert(v) for k, v in item.items()})
            if isinstance(item, list):
                def yield_convert(item):
                    for index, value in enumerate(item):
                        yield convert(value)
                return list(yield_convert(item))
            else:
                return item

        return convert(item)


class EventManager():
    def __init__(self):
        self.subscriptions = {}
        self.logger = logging.getLogger(__name__)

    def unsubscribe(self, event_id, callback):
        if event_id in self.subscriptions.keys():
            self.logger.debug(f'Removing {callback} from {event_id}')

            self.subscriptions[event_id].remove(callback)

    def subscribe(self, event_id, callback):
        self.logger.debug(f'Adding {callback} to {event_id}')

        if event_id not in self.subscriptions.keys():
            self.subscriptions[event_id] = [callback]
        else:
            self.subscriptions[event_id].append(callback)
