from api.parser import MessageParser
from api.exceptions import ValidationException


class MessageValidator:
    """
    MessageValidator class contains validation methods for route message patch.
    Also MessageParser instance can be retrieve from .get_parser() method.
    Of course the message object must be validated first.
    """
    validated = False
    message_content = ["vehicles", "jobs", "matrix"]

    def __init__(self, data):
        self.raw_data = data

    def validate(self):
        """
        Checks if the message is in the correct format
        :return: Boolean : whether is valid
        """
        for content in self.message_content:
            content_value = self.raw_data.get(content)
            if content_value is None:
                raise ValidationException("Message should contain {0} key!".format(content))
            if not isinstance(content_value, list):
                raise ValidationException("{0} should be a list instance!".format(content))
            if not len(content_value):
                raise ValidationException("You must have enter at least one {0}!".format(content))

        location_count = len(self.raw_data.get('matrix'))

        for vehicle in self.raw_data.get('vehicles'):
            if vehicle['start_index'] + 1 > location_count:
                raise ValidationException(
                    "Distance matrix not contain index as {0}".format(str(vehicle['start_index'])))

        for job in self.raw_data.get('jobs'):
            if job['location_index'] + 1 > location_count:
                raise ValidationException("Distance matrix not contain index as {0}".format(str(job['location_index'])))

        self.validated = True
        return True

    def get_parser(self):
        """
        If message data validated, retrieve parser class
        :return: parser class instance : MessageParser
        """
        if self.validated:
            return MessageParser(data=self.raw_data)
        else:
            raise ValidationException("Message not validated. Use .validate() method for validation.")
