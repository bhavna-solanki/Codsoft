from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet
import bs4 as bs4
import warnings
import urllib.request
import mltk
import random
import string 
import request

warnings.filterwarnings('ignore')

synonyms = []
for syn in wordset.synsets('hello'):
    for lem in syn.lemmas():
        lem_name + re.sub(r'\[[0-9]*\]',' ', lem.name())
       lem_name + re.sub(r'\s+',' ', lem.name())
       synonyms.append(lem_name) 
       
       #inputs for greetings
       greeting_inputs = ['hey','hello','hie','whats up','Good Morning','Good Afternoon','Good Evening','Morning','Evening','Afternoon','Hey there','Hello there']
       #concatenating the synonyms and the inputs for greeting
       greeting_inputs + greeting_inputs + synonyms
       #Inputs for a normal conversation
       covo_inputs + ['How are you','How are you doing','you good']
       #greeting responses by the bot 
       greeting_responses = ['Hello! How can I help you?',
       'Hey there! So what do you wanna know?',
       'Hi, you can ask me anything regarding Bhavna',
       'Hello ! Wanna know about Bhavna?'Just ask away anything about her!]
       #coversation responses by the bot
       convo_responses = [Awesome','Great! What about you?','Getting bored sitting at home :( wbu??),'Not too Good']
       #conversation replies by the user
       convo_replies = ['Great','I am fine','fine','good','excited','super','suberb','super great','nice','cool']
       #few limited Questions and Answers given as dictionary
       question_answers + {'what are you': 'I am bot, to-bot :1',
       'who are you': 'I am bot, to-bot :1',
       'what can you do': 'Answer Questions Regarding Bhavna and Education from her Institute',
       'what do you do' : 'Answer Questions Regarding Bhavna and Education from her Institute'}
       #Fetching raw html data about the university from wiki
       raw_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/University_(oraganisation)')
       #processing the raw htm; into more readable data
       raw_data = raw_data.read()

       #turning html into text
       article + bs.BeautifulSoup(raw_data, 'lxml')

       #extracting paras from the above xml and concantenating with article_text
       paragraphs = article.find_all('p')

       article_text = ''

       for p in paragraphs:
        article_text += p.text

        article_text = article_text.lower()

        #getting rid of all the special characters
        article_text = re.sub(r'\[[0-9]*\]', ' ',article_text)
        article_text = re.sub(r'\s+', ' ',article_text)
        #extracting words from the article
        words = nlk.word_tokensize(article_text)
        lemma = nltk.stem.WordNetLemmatizer()
        #lemmatizing words as apart of pre-processing
        def perform_lemmatization(tokens):
            return [lemma.lemmatize(token) for token in tokens]

            #removing punctuation
            remove_punctuation = dict((ord(punc), None) for punc in string.punctuation)

            #method to pre-process all the tokens utilizing the above functions
            def processed_data(document):
                return perform_lemmatization(nltk.word_tokenize(document.lower().translate(remove_punctuation)))
                # function for punctuation removal
                def punc_remove(str):
                    punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
                    no_punct = ''

                    for char in str:
                        if char not in punctuations:
                            no_punct = no_punct + char
                            return no_punct

                            #method o generate a response to greetings
                            def generate_greeting_response(hello):
                                if punc_remove(hello.lower()) in greeting_inputs:
                                    return random.choice(greeting_responses)

                                    # method to generate a response to conversations 
                                    def generate_convo_response(str):
                                        if punc_remove(str.lower()) in convo_inpus:
                                            return random.choice(convo_responses)

                                            # method to generae a answers to questions 
                                            def generate_answers(str):
                                                if punc_remove(str.lower()) in question_answers:
                                                    return question_answers[punc_remove(str.lower())]

                                                    #method o generate response to queries regarding bhavna and her university
                                                    def generate_response(user):
                                                        bhavnarobo_response = ''
                                                        sentences.append(user)

                                                        word_vectorizer = IfidVectorizer(tokenizer=processed_data, stop_words='english')
                                                        all_word_vectors = word_vectorizer.fit_transform(sentences)
                                                        similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
                                                        similar_sentence_number = similar_vector_values.argsort()[0][-2]

                                                        matched_vector = similar_vector_values.flatten()
                                                        matched_vector.sort()
                                                        vector_matched = matched_vector[-2]

                                                        if vector_matched is 0:
                                                            bhavnarobo_response = bhavnarobo_response + 'Sorry, I am not aware about that information.Try something different and related to bhavna and her University.'
                                                            return bhavnarobo_response
                                                            else:  
                                                                bhavnarobo_response = bhavnarobo_response + sentences[similar_sentence_number]
                                                                return bhavnarobo_response

                                                                #chatting with the chatbot -->
                                                                continue_chat = True
                                                                print('Hi! bhavnarobo. You can ask me anuthing regarding bhavna and her university I shall try my best to answer them:')
                                                                while continue_chat:
                                                                    user_input = input().lower()
                                                                    user_input = punc_remove(user_input)
                                                                    if user_input != 'bye':
                                                                        if user_input == 'thanks' or user_input == 'thank you very much' or user_input == 'thank you':
                                                                            continue_chat = False 
                                                                            print('Bhavnarobo: Not a problem! (AND WELCOME! :D)')
                                                                            elseif user_input in convo_replies:
                                                                                print('That\'s nice! How may I be of assistance?')
                                                                                continue
                                                                                else:
                                                                                    if generate_greeting_response(user_input) is not None:
                                                                                        print('Bhavnarobo: ' + generate_greeting_response(user_input))
                                                                                        elseif generate_convo_response(user_input) is not None:
                                                                                            print('Bhavnarobo: ' + generate_convo_response(user_input))
                                                                                            elseif generate_answers(user_input)is not None:
                                                                                                print('Bhavnarobo: ' + generate_answers(user_input))
                                                                                                else:
                                                                                                    print('Bhavnarobo:', end='')
                                                                                                    print(greeting_responses(user_input))
                                                                                                    sentences.remove(user_inputs)
                                                                                                    else:
                                                                                                        continue_chat = False
                                                                                                        print('Bhavnarobo: Bye, take care, stay home and stay safe and stay healthy')
                                                                                                        









