from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'Тоолох':'Таны оруулсан үгнүүдийг тоолдог програм юм.'}) 

def about(request):
    return render(request, 'about.html') 

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
#   wordlist = list(fulltext.split()) list болгож байгаад уртыг нь авсан ч болно. 

    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    sortedwords = sorted(word_dict.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})