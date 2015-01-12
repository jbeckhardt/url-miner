import nltk.stem
import sys
import urllib2, cookielib
import random
from bs4 import BeautifulSoup
import json

protocol = ['sy','sy']
#list that outlines how to build the string - eg ["c","v","c","su"] for a consonant-vowel-consonant-vowel
#consonant (c), vowel (v), word (w), stem (st), syllable (sy), prefix (pr), suffix (su)
#phoneme (ph), phoneme consonant (phc), phoneme vowel (phv)
#prefixes return empty strings

max_domain_length = 10

cycles = 100

class RandomString(object):
    def __init__(self, protocol):
        self.string = self.getString(protocol)

    def getString(self, protocol):
        string = ""
        for x in protocol:
            substring = self.getSubstring(x)
            string += substring
        self.string = string
        return string
    
    def getSubstring(self, argument):
        if argument == "c":
            substring = self.getRandomConsonant()
        elif argument == "v":
            substring = self.getRandomVowel()
        elif argument == "w":
            substring = self.getRandomWord()
        elif argument == "st":
            substring = self.getRandomStem()
        elif argument == "sy":
            substring = self.getRandomSyllable()
        elif argument == "pr":
            substring = self.getRandomPrefix()
        elif argument == "su":
            substring = self.getRandomSuffix()
        elif argument == "ph":
            substring = self.getRandomPhoneme()
        elif argument == "phc":
            substring = self.getRandomPhonemeConsonant()
        elif argument == "phv":
            substring = self.getRandomPhonemeVowel()
        else:
            substring = ""
        return substring

    def getRandomConsonant(self):
        consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        random_consonant = random.choice(consonants)
        return random_consonant
    
    def getRandomVowel(self):
        vowels = ['a','e','i','o','u', 'y']
        random_vowel = random.choice(vowels)
        return random_vowel

    def getRandomWord(self):
        with open("dictionaries/words.txt", 'r') as words:
            random_word = random.choice(words.readlines())[:-2]
            random_word = random_word[:-1] if random_word[-1] == "%" else random_word
        return random_word

    def getRandomStem(self):
        random_word = self.getRandomWord()
        stemmer = nltk.stem.snowball.EnglishStemmer()
        random_stem = stemmer.stem(random_word)
        return random_stem

    def getRandomSyllable(self):
        syllables = ['th', 'he', 'an', 'er', 'in', 're', 'nd', 'ou', 'en', 'on', 'ed', 'to', 'it', 'ha', 'at', 've', 'or', 'as', 'hi', 'ar', 'te', 'es', 'ng', 'is', 'st', 'le', 'al', 'ti', 'se', 'wa', 'ea', 'me', 'nt', 'ne', 'al', 'an', 'ar', 'as', 'at', 'ea', 'ed', 'en', 'er', 'es', 'ha', 'he', 'hi', 'in', 'is', 'it', 'le', 'me', 'nd', 'ne', 'ng', 'nt', 'on', 'or', 'ou', 're', 'se', 'st', 'te', 'th', 'ti', 'to', 've', 'wa', 'all', 'and', 'are', 'but', 'ent', 'era', 'ere', 'eve', 'for', 'had', 'hat', 'hen', 'her', 'hin', 'his', 'ing', 'ion', 'ith', 'not', 'ome', 'oul', 'our', 'sho', 'ted', 'ter', 'tha', 'the', 'thi', 'tio', 'uld', 'ver', 'was', 'wit', 'you', 'the', 'and', 'ing', 'her', 'you', 'ver', 'was', 'hat', 'not', 'for', 'thi', 'tha', 'his', 'ent', 'ith', 'ion', 'ere', 'wit', 'all', 'eve', 'oul', 'uld', 'tio', 'ter', 'hen', 'had', 'sho', 'our', 'hin', 'era', 'are', 'ted', 'ome', 'but']
        random_syllable = random.choice(syllables)
        return random_syllable

    def getRandomPrefix(self):
        random_prefix = ""
        return random_prefix

    def getRandomSuffix(self):
        with open("dictionaries/suffixes.txt", 'r') as suffixes:
            random_suffix = random.choice(suffixes.readlines())[:-1]
        return random_suffix

    def getRandomPhoneme(self):
        phonemes = ['p','b','t','d','f','v','th','dh','s','z','sh','zh','ch','jh','k','ng','g','m','n','l','r','w','y','hh','aa','ae','ah','ao','aw','ax','ay','ea','eh','er','ey','ia','ih','iy','oh','ow','oy','ua','uh','uw']
        random_phoneme = random.choice(phonemes)
        return random_phoneme

    def getRandomPhonemeConsonant(self):
        phoneme_consonants = ['p','b','t','d','f','v','th','dh','s','z','sh','zh','ch','jh','k','ng','g','m','n','l','r','w','y','hh']
        random_phoneme_consonant = random.choice(phoneme_consonants)
        return random_phoneme_consonant

    def getRandomPhonemeVowel(self):
        phoneme_vowels = ['aa','ae','ah','ao','aw','ax','ay','ea','eh','er','ey','ia','ih','iy','oh','ow','oy','ua','uh','uw']
        random_phoneme_vowel = random.choice(phoneme_vowels)
        return random_phoneme_vowel

    def getTruncatedString(self, index):
        truncated_string = self.string[:index]
        return truncated_string

class Url(object):
    def __init__(self,string):
        self.address = "http://www." + string + ".com"
        self.short_address = "www." + string + ".com"

    def getStatus(self):
        api_url = 'http://freedomainapi.com/?key=xjeovl5cot&domain=' + self.short_address
        available = str(json.loads(urllib2.urlopen(api_url).read())["available"])
        if available == 'True':
            status = "1"
        elif available == 'False':
            status = "0"
        else:
            status = available
        return status
    
    def logStatus(self, output_file):
        status = self.getStatus()
        string_and_status = self.short_address[4:] + "," + status + '\n'
        with open(output_file,"a+") as output_file:
            output_file.write(string_and_status.format())
        print string_and_status

def getSuggestedOutputFile(protocol):
    suggested_output_file = "outputs/"
    for x in protocol:
        suggested_output_file += x + '_'
    suggested_output_file = suggested_output_file[:-1] + '.txt'
    return suggested_output_file

print protocol

output_file = getSuggestedOutputFile(protocol)

for i in range(cycles):
    random_string = RandomString(protocol).string
    if len(random_string) <= max_domain_length:
        random_url = Url(random_string)     
        random_url.logStatus(output_file)
    else:
        print "string too long   -   " + random_string
    
