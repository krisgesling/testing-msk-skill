from mycroft import MycroftSkill, intent_file_handler


class TestingMsk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('msk.testing.intent')
    def handle_msk_testing(self, message):
        self.speak_dialog('msk.testing')


def create_skill():
    return TestingMsk()

