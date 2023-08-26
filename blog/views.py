from django.shortcuts import render

# Create your views here.

posts = [

  {
      'author': 'John',
      'title': 'Love of my life 1',
      'content': 'My love story started when I was 6',
      'date_posted': 'August 6,2018'
  },


  {
      'author': 'John',
      'title': 'Love of my life 2',
      'content': 'My love story started when I was 6',
      'date_posted': 'August 6,2018'
  },


  {
      'author': 'John',
      'title': 'Love of my life 3',
      'content': 'My love story started when I was 6',
      'date_posted': 'August 6,2018'
  }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})