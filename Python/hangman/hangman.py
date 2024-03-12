import PySimpleGUI as sg

class Hangman:
        def __init__(self) -> None:
                self._window = sg.Window(
                        title="Hangman", 
                        layout=[[]],
                        finalize=True,
                        margins=(100, 100)
                )
        
        def read_event(self):
                event = self.__window.read()
                event_id = event[0] if even is not None else None
                return event_id
        
        def close(self):
                self._window.close()
