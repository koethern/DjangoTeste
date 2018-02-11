from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')
def contact(request):
    return render(request, 'personal/contato.html', {'content':['se você gostaria de me contatar, me mande um email','koethern@gmail.com']})
