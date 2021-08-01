# Mitesh Choksi
from typing import Counter
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello, World!!!</h1>")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('extraspaceremover','off')
    counter = request.POST.get('counter','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Want To Capitalize', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char !="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed   
        # return render(request, 'analyze.html', params)
    if spaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed=analyzed+char
        params = {'purpose':'SpaceRemover','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if counter == "on":
        count = 0
        for char in djtext:
            count+=1
        params={'purpose':'COUNTER','analyzed_text':count}
        djtext = str(count) + djtext
    if (removepunc != "on" and uppercase != "on" and newlineremover != "on" and spaceremover != "on" and counter != "on"):
        return HttpResponse("ERROR")
        
    return render(request,'analyze.html',params)

# def readTxt(request):
#     f = open("E:\Django Tutorials CodeWithHarry\TextUtils\\1.txt",'r')
#     fread = f.read()
#     f.close()
#     return HttpResponse(fread)

def links(request):
    return render(request, "index.html")
#     # return HttpResponse('<a href = "https://web.whatsapp.com">Whats App </a></br><a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Code With Harry Django Playlist</a></br><a href = "https://www.facebook.com">Facebook</a></br><a href = "https://mail.google.com/mail/u/0/#inbox">GMAIL</a>')

# def facebook(request):
#     return HttpResponse('</br><a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Code With Harry Django Playlist</a>')