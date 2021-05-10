from mycroft import MycroftSkill, intent_file_handler


class SickFeeling(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('feeling.sick.intent')
    def handle_feeling_sick(self, message):
#         f = message.data.get('f')
          f='OK Rohit'

        self.speak_dialog('feeling.sick', data={
            'f': f
        })


def create_skill():
    return SickFeeling()

