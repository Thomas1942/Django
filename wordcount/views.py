import operator

from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext,
                                          'count': len(wordlist),
                                          'worddict': worddict,
                                          'sortedwords': sortedwords})

def info(request):
    vec = [1938.80, 1681.72, 2372.63, 2001.72, 1973.01,
        1826.82, 1885.49, 2172.71, 1934.19, 1889.90,
        1979.15, 2002.53, 1984.22, 1990.84, 3312,
        1990.84, 1984.22, 1984.22, 1990.83, 2669.80,
        2939.61, 3369.73, 3215.64, 3215.64, 3215.64,
        4347.17, 3584.69, 3215.64, 3215.64, 3215.64,
        3215.64, 6069.11, 3235.53, 3257.76, 3257.76,
        3658.12, 3391.34]

    plt.plot(vec)
    plt.savefig('info.png')

    return render(request, 'info.html', 'info.png')