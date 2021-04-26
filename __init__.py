from mycroft import MycroftSkill, intent_file_handler


class GebaeudePfoertner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pfoertner.gebaeude.intent')
    def handle_pfoertner_gebaeude(self, message):
        self.speak_dialog('pfoertner.gebaeude')


def create_skill():
    return GebaeudePfoertner()

