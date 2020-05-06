from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def home(request):
    return render(request, 'index.htm', {'what':'Upload PDB Files for use in Fragalysis\nHello'})

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print(uploaded_file.name)
        print(uploaded_file.size)
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")    
    
    return HttpResponse("Failed")
    

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        print('creating directory')
        os.makedirs('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            

