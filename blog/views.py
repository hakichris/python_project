from django.shortcuts import render

# Create your views here.

posts = [

  {
      'author': 'chris',
      'title': 'Love of my life',
      'content': 'My love story started when I was 6',
      'date_posted': 'August 6,2018'
  },


  {
      'author': 'chris',
      'title': 'Love of my life',
      'content': 'My love story started when I was 6',
      'date_posted': 'August 6,2018'
  },


  {
      'author': 'chris',
      'title': 'Love of my life',
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
    return render(request, 'blog/about.html')