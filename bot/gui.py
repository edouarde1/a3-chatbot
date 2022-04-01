import sys
import tkinter as tk
import botbot
import translate


# Class for the Bot GUI
class BotGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(HomeScreen)
        self.title("Atlantis Explorer")

    # Destroy active window and replace with desired
    def switch_frame(self, frame_class, *args, **kw):
        if self._frame:
            # Delete old frame if it exists
            self._frame.destroy()
        new_frame = frame_class(self,*args, **kw)
        # Set active frame as the new frame & pack it
        self._frame = new_frame
        self._frame.pack()

    # Shut down application
    def quit(self):
        self.destroy()


# Main title screen shown when loading app
# TODO: Potentially increase starting size of this window so it's less awkward
class HomeScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome, Adventurer!").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Start Conversation",
                  command=lambda: master.switch_frame(LanguageScreen)).pack()
        tk.Button(self, text="Exit ",
                  command=lambda: master.quit()).pack()


class LanguageScreen(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Label(self, text="Please pick a language you would like to recieve a response from ?")
        tk.Button(self,text="English",
            command=lambda: master.switch_frame(ChatScreen,"en")).pack()
        tk.Button(self,text="French",
            command=lambda: master.switch_frame(ChatScreen,"fr")).pack()
        tk.Button(self,text="Spanish",
            command=lambda: master.switch_frame(ChatScreen,"es")).pack()
        tk.Button(self, text="Exit ",
                  command=lambda: master.quit()).pack()


# The screen where inputs are entered
# Receives an int to specify response language
class ChatScreen(tk.Frame):        
    # The function which handles user input.
    def retrieve_user_message(self, inputField, lang):
        # Retrieve user input and save it
        userInput = inputField.get("1.0", tk.END)
        # Clear input box
        inputField.delete("1.0", tk.END)
        # Remove unnecessary punctuation
        punctuation = '!()-[]{};:\,<>./?@#$%^&*_~'
        for char in punctuation:
            userInput = userInput.replace(char,' ')
        # Pass input through spell checking module
        input = botbot.spell_check(userInput)
        # Get response from bot & update response label
    
        # Translate only if not enlish
        if lang == "en":
            self.response = botbot.get_response(input)
        else: 
            self.response = translate.translate_text(lang,botbot.get_response(input))

        print("Response", self.response)
        self.responseLabel["text"] = self.response

    def show_help_popup(self):
        self.responseLabel["text"] = "Welcome, Adventurer! Please enter your question below.\n When you are done, " \
                                     "please end your question with a '?' and hit the 'Send' button below!"

    def __init__(self, master, lang):

        if lang == "fr":
            self.response = "Bienvenue, aventurier! Veuillez demander votre question.\n Lorsque vous avez terminé, veuillez terminer votre " \
                        "question avec un '?' et appuyez sur le bouton 'Envoyer' !" 
        elif lang == "es":
            self.response = "¡Bienvenido, aventurero! Introduce tu pregunta a continuación.\n Cuando hayas terminado, " \
                            "Por favor, termine su pregunta con un '?' y presione el botón 'Enviar' a continuación!"
        else:
            self.response = "Welcome, Adventurer! Please enter your question below.\n When you are done, " \
                                     "please end your question with a '?' and hit the 'Send' button below!"

        tk.Frame.__init__(self, master)
        # Response label is what the bot response will be output to

        self.responseLabel = tk.Label(self, text=self.response)
        self.responseLabel.pack(side="top", fill="x", pady=10)
        userInputField = tk.Text(self)
        userInputField.pack(side="top", fill="x", pady=10)
       
        # Bottom row of buttons
        tk.Button(self, text="Send",
                  command=lambda: self.retrieve_user_message(userInputField,lang)).pack(side="left")
        tk.Button(self, text="Help",
                  command=lambda: self.show_help_popup()).pack(side="left")
        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(HomeScreen)).pack(side="left")


botInterface = BotGUI()
botInterface.mainloop()
