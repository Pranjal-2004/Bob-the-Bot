import rasa.shared.utils.io as io
from rasa_sdk.events import SlotSet
from bardapi import BardCookies
from rasa_sdk import Action

cookie_dict = {
    
    "__Secure-1PSIDTS": "USE YOUR API KEY FROM BARD",
    "__Secure-1PSID": "USE API KEY"

}




bard = BardCookies(cookie_dict=cookie_dict)



class ActionBardFallback(Action):
    def name(self) -> str:
        return "bard_call"
    
    def run(self, dispatcher, tracker, domain):
        request = " ".join(tracker.latest_message['text'].split()[1:])
        response = bard.get_answer(request)['content']
        dispatcher.utter_message(text=response)
        # return [SlotSet("request", request), SlotSet("response", response)]



# class ActionMotivate(Action):
#     def name(self):
#         return "action_motivate"

#     def run(self, dispatcher, tracker, domain):
#         quote = random.choice(motivational_quotes)
#         dispatcher.utter_message(quote)
