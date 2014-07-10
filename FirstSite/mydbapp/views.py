from django.shortcuts import render
from django.shortcuts import render_to_response #for index function
from django.template import RequestContext #for index function

from django.http import HttpResponse #for about function

from mydbapp.models import Employees #for displaying data from mysql db
from mydbapp.forms import EmployeeForm #for forms to get user input

# Create your views here.
#old index function
def index(request):
    #request context, context contains info such as the clients machine details
    context = RequestContext(request)

    #query db for first 10 employees
    employees_list = Employees.objects.order_by('emp_no')[:10]

    #construct dict to pass to template engine as it's context.
    context_dict = {'employees': employees_list}

    #return the rendered response to send to the client
    #we make use of the shortcut function to make our lives easier.
    #note that the first parameter is the template we wish to use
    return render_to_response('mydbapp/index.html', context_dict, context)

    #return HttpResponse("My DB app says hello! <a href='/mydbapp/about'>About</a>")
    
def add_employee(request):
    #get context from form
    context = RequestContext(request)

    #a http post?
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        #have we been provide with a valid form?
        if form.is_valid():
            #save new employee to the database
            form.save(commit=True)

            #now call the index() view
            #The user will be shown the homepage
            return index(request)
        else:
            #the supplied form contained errors - just print them to the terminal
            print form.errors
    else:
        #if the request was not a POST, display the form to enter details.
        form = EmployeeForm

    #bad form (or form details), no form supplied...
    #render the form with error message (if any).
    return render_to_response('mydbapp/add_employee.html', {'form': form}, context)


def get_employee(request):
    context = RequestContext(request)
    #query_data = None
    query_data = Employees.objects.order_by('emp_no')[:10]
    context_dict = {'employees': query_data}

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        #have we been provide with a valid form?
        if form.is_valid():
            query_data = Employees.objects.order_by('emp_no')[:10]

            return get_employee(request)
        else:
            #the supplied form contained errors - just print them to the terminal
            print form.errors
    else:
        #if the request was not a POST, display the form to enter details.
        form = EmployeeForm

    return render_to_response('mydbapp/get_employee.html', context_dict, context)


def about(request):
    return HttpResponse("ABOUT PAGE! <a href='/mydbapp/'>Index</a>")
