# 310-Group-Project

## Project Description 

Our project is going to be an interactive chatbot that takes on the role of a would-be Atlantis explorer. The chatbot will only talk about things regarding Atlantis and will excitedly talk to the user about his upcoming adventure. The link to our GitHub repo is as follows https://github.com/edouarde1/310-Group-Project. 

## How to Run the Chat Bot 

1. Download our GitHub repo 
2. Open the repo using VSCode or Terminal 
3. run `run_me_first.sh` (If you are uncomfortable running a bash script refer to dependencies.) 
4. Run gui.py 

## Dependencies
This bot requires nltk, pyspechecker, and stanza in order to run properly. If you do not run first-time-setup.sh you will have to do the following
    
    pip install nltk
    pip install pyspellchecker
    pip install stanza
    
Then you have to run py_lib_install.py so python can install the additional libraries. 

## API Authentication
### Google Translate 
1. Create a Google Cloud platform project with the Google Cloud Translation API enabled. For help with this task please refer to [Create a project and enable the API](https://developers.google.com/workspace/guides/create-project).
2.  Create and download authorization credentials and move file into the 'bot' directory. Then, modify the name of credentials file to 'credentials.json' 
3.  In your in terminal type: 
   'export GOOGLE_APPLICATION_CREDENTIALS= /path/to/credentials.json'

### Twitter API
  1. Sign-up for a Twitter developer account, create a new project, and set up an application. For help with this task please refer to [Sign-up for a developer account](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and [Create a project](https://developer.twitter.com/en/docs/projects/overview)
  2. Change access level of project from 'essential access' to 'elevated access'. For help with this task refer to [Access Levels](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)
  3. Inside of the 'bot' directory create a .env folder which should include four authentication tokens. <br><br> The format should go as follows: <br><br>CONSUMER_KEY= {Insert key here}<br>
                  CONSUMER_SECRET= {Insert key here}<br>
                  ACCESS_TOKEN= {Insert  key here}<br>
                  ACCESS_TOKEN_SECRET= {Insert key here} <br> 





## Dataset 
This bot pulls from a json file with specifically designed responses for who, what, where, when, why style responses. Essentially, this bot smartly translates user text into queries to generate aproprait responses. 

## Classes and Functions 

## botbot.py 
This directory includes all the files for the bot. 

### get_response
This function recieves the keyword dictionary, asks for user input, and returns chat bot responses. User input is processed using `get_query_objects()`, which extracts nouns and proper nouns. A for-loop iterates through each processed noun in a list and detects if the word exists in entity_dict.json. If there is a match, that means there is a chat bot response for the keyword. If there is no keyword detected in the user response, then the bot returns "Sorry can't help provide any information that relates to [*whatever related noun the user entered*]". 

Parameters:
- response: a string input by the user acting as the key for keywords

  
Returns:
- output: a string containing the bots response

### spell_check()
Takes a string and returns a string with closest related permutation that is part of the english language.

 Parameter:
 - input: a string input  

 Returns:
 - correct: a corrected string output 
    
## tranlate.py 
This python module handles text translation

### translate_text()

This function takes an input and will translate the input into a target language. The translated input is then returned. 
 
Parameters: 
- target: String of the for the target language. Can be "en", "fr", or "es"
- text: String of text to be translated 
Returns: 
- text: String of translated text 
## gui.py

### BotGUI(tk.Tk)
The class which handles window switching and displays the alternate screens

#### HomeScreen (class)
The main title screen that shows when loading the application. 

#### LanguageScreen(class)
This window allows the user to select the language for the chat bot 
#### ChatSreen (class)
The class that manages the chatscreen. 
##### retrieve_user_message(inputField)
gets user input, and then passes the input to the bot for processing. Recieves the updated bot response, and updates the GUI with the new response.

Parameters:
- inputField: a string which determins what field to be inputed

#### get_tweets(self,inputField, lang)
This function recieves the user user input and queries input into the twitter  api. Which is then translated and output to console. 

Parameters: 
- inputField: a string which determines what field input
- lang: language target ("en","fr",or "es")

Returns
- None

### data_load.py
For managing data and searching

#### data_load
Loads text from a file.

 Parameters:
 - filepath: file to path to retrieve text from 

 Returns:
  - contents: string of raw text
  

#### preproc
Extracts the nouns and proper pouns from the user query. Takes a user query and runs string 
through Stanza's Dependency Parser. More information about this library is found here: 
https://stanfordnlp.github.io/stanza/depparse.html

Parameters:
 - query: a string 

 Returns:
- obj_list: a list nouns and proper nouns from the user query 


#### dependencyParser
Helper utility used to extract the depencies from a sentence. Runs the dp pipeline object 
in order to run depparse, lemma, and pos tagginig.

Parameters: 
 - sentence: a string 

### syn_detection.py

#### detect_syn
This function takes a word and uses wordnet in order to return a list of asociated synonyms with our word,.

Parameters
- input : word to get inputs from 

Returns
- synonyms: list of synonyms associated with said words. 

### search_json.py

#### search_noun_quest
takes a noun and searches for related question style keywords. 

Parameters
- noun, question: noun and question. Question is mostly used as an adverb in this case.

Returns
- data[noun][quest]: returns a string associated with indexed value

#### get_nouns
returns a list of all nouns within json file

Returns
 - nounList: list of nouns 

#### get_verbs
Parameters
- noun: a string 
 
Returns
 - questList: list of adverbs associated with said noun


#### test_spell_check
Tests functionality of `spell_check()` function in bot.py

#### test_get_response
Tests functionality of `get_response(query)` function in bot.py

#### test_load_data
Tests functionality of `load_data()` 

## New Features

### Translation 

This chat bot now makes use of the Google Cloud Translate API. The bot is able to speak in english, french, or spanish. When the user accesses the chat bot they are promted to a language selection screen where they may select the language of choice. For now the bot only accecpts english queries  and can respond in any of the three languages. 

### Twitter 

The chat bot can access Twitter using the Twitter API. If the user is not getting the right reponses from the chat bot the user may select the 'Ask Twitter' button which enables them to send their query directly to twitter. The API will respond with the most recent tweet related to the query. 