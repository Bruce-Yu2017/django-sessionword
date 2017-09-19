from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
  return render(request, 'session_word/index.html')

def add(request):
  newword = {}
  for key, value in request.POST.iteritems():
    if key != 'bigfont':
      newword[key] = value
  if 'bigfont' in request.POST:
    newword['bigfont'] = 'big'
  else:
    newword['bigfont'] = ""
  newword['created_at'] = datetime.now().strftime('%H:%M %P, %B %d, %Y') 
  try:
    request.session['text']
  except KeyError:
    request.session['text'] = []

  temp = request.session['text']
  temp.append(newword)
  request.session['text'] = temp
  return redirect('/')

def clear(request):
  for key in request.session.keys():
    del request.session[key]
  return redirect('/')
