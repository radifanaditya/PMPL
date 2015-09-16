from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home_page(request):
    # return HttpResponse('<html><title>Mahasiswa PMPL</title><p>Nama : Radifan Aditya R</p><p>NPM : 1206238293</p></html>')

def home_page(request):
      # if request.method == 'POST':
          # return HttpResponse(request.POST['item_text'])
      # return render(request, 'home.html')
      return render(request, 'home.html', {
          'new_item_text': request.POST.get('item_text', ''),
      })
