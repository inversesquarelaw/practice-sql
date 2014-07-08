from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponse

# Create your views here.
def index(request):
    #request context, context contains info such as the clients machine details
    context = RequestContext(request)
    #construct dict to pass to template engine as it's context.
    #note the key boldmessage is the same as {{boldmessage}} in the template
    context_dict = {'boldmessage': 'I am bold font from the context'}
    #return the rendered response to send to the client
    #we make use of the shortcut function to make our lives easier.
    #note that the first parameter is the template we wish to use
    return render_to_response('mydbapp/index.html', context_dict, context)

    #return HttpResponse("My DB app says hello! <a href='/mydbapp/about'>About</a>")

def about(request):
    return HttpResponse("ABOUT PAGE! <a href='/mydbapp/'>Index</a>")
