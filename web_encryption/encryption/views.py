from django.shortcuts import render
from . import encrypt_algo

def encryption_home(request):
    context = {}
    context['result_data']=''
    if request.method == 'POST':
        text_to_encrypt = request.POST['text_to_encrypt']
        encryption_type = request.POST['encryption_type']
        #print(text_to_encrypt)
        #print(encryption_type)
        result_data = encrypt_algo.encrypt_text(text_to_encrypt, encryption_type)
        context['result_data'] = result_data
        
        print(result_data)
    
    return render(request,'encryption.html',context)
# Create your views here.
