from django.shortcuts import render

# temp courses structure
courses = [
    {'id':1, 'name':'SWEN-261'},
    {'id':2, 'name':'SWEN-262'},
    {'id':3, 'name':'SWEN-340'},
]


# Create your views here.
# response the home page
def home(request):
    all_courses = {'courses': courses}
    return render(request, 'home.html', all_courses)

def rate_prof_page(request):
    return render(request, 'rate.html')