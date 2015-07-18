import json
import time

class TrapEvent(object):

    EVENT_SEVERITY = {"CRITICAL": 2, "WARNING": 1, "OK": 0}

    def __init__(self, name, output, status, handlers, 
                 environment=None, servicetag=None, mail_to=None):
        self.name = name
        self.output = output
        self.status = status
        self.handlers = handlers
        self.executed = int(time.time())
        self.environment = environment
        self.servicetag = servicetag
        self.mail_to = mail_to

    def to_json(self):
        return json.dumps({'name': self.name,
                           'output': self.output,
                           'status': self.status,
                           'handlers': self.handlers,
                           'executed': self.executed,
                           'environment': self.environment,
                           'servicetag': self.servicetag,
                           'mail_to': self.mail_to})

    def __repr__(self):
        return "<TrapEvent name:'%s' >" % (self.name)
