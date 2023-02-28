# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted


class ActionMathOperation(Action):

    def name(self) -> Text:
        return "action_math_operation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        operation = tracker.get_slot("operation")
        operand1 = float(tracker.get_slot("operand1"))
        operand2 = float(tracker.get_slot("operand2"))

        if operation == "add":
            result = operand1 + operand2
        elif operation == "subtract":
            result = operand1 - operand2
        elif operation == "multiply":
            result = operand1 * operand2
        elif operation == "divide":
            result = operand1 / operand2
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't understand that operation.")
            return []

        result = round(result, 2)
        dispatcher.utter_message(template="utter_math_result", operation=operation, operand1=operand1, operand2=operand2, result=result)
        return [SlotSet("operation", None), SlotSet("operand1", None), SlotSet("operand2", None)]


class ActionMoreOperations(Action):

    def name(self) -> Text:
        return "action_more_operations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_confirm_more_operations")
        return [SlotSet("operation", None), SlotSet("operand1", None), SlotSet("operand2", None)]

