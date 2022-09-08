# Created this file by -WasimChadhar

from email.policy import default
from itertools import count
from pickle import TRUE
import re
from string import punctuation
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    params={
    'purpose': 'Text Analyzer',
    'analyzerText': 'Enter text to perform any of below acton : '
}
    return render(request, 'index.html', params)
    
def analyzer(request):
    getAnalyzingText = request.POST.get('text', 'default')
    removePunc = request.POST.get('removePunctuation','off')
    countCharacter = request.POST.get("charCount", 'off')

    analyzed=""

    if removePunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
        for char in getAnalyzingText:
            if char not in punctuations:
                analyzed = analyzed + char
            
        params={
            'purpose': 'Removed Punctuation',
            'analyzedText': analyzed
        }

        getAnalyzingText = analyzed

        return render(request, 'analyze.html', params)

    elif countCharacter == 'on' :
        letter_count = 0
        for char in getAnalyzingText:
            if char.isalpha():
                letter_count += 1

        params={
            'purpose': 'Character counted',
            'analyzedText': 'Total Number of character : ' + str(letter_count)
        }
        
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Mark the relevant Check-Box!")
    






