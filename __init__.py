from mycroft import MycroftSkill, intent_file_handler
#from gapi import *


class SickFeeling(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('feeling.sick.intent')
    def handle_feeling_sick(self, message):
#         f = gapi.News()[:5]
        f = message.data.get('f')
        name=message.data.get('name')
        
    

        self.speak_dialog('feeling.sick', data={
            'name':name,'f': f
        })


def create_skill():
    return SickFeeling()

