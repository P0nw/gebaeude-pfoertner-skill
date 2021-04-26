from mycroft import MycroftSkill, intent_file_handler


class GebaeudePfoertner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pfoertner.gebaeude.intent')
    def handle_pfoertner_gebaeude_oeffnen(self, message):
        self.speak_dialog('pfoertner.gebaeude')

    @intent_file_handler('pfoertner.gebaeude.oeffne.intent')
    def handle_pfoertner_gebauede_schliessen(self, message):
        self.speak_dialog("pfoertner.gebaeude.oeffne")

    def stop(self):
        pass

def create_skill():
    return GebaeudePfoertner()

