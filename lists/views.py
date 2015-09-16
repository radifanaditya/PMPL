from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
# def home_page(request):
    # return HttpResponse('<html><title>Mahasiswa PMPL</title><p>Nama : Radifan Aditya R</p><p>NPM : 1206238293</p></html>')

def home_page(request):
      if request.method == 'POST':
          # return HttpResponse(request.POST['item_text'])
          # new_item_text = request.POST['item_text']
          # Item.objects.create(text=new_item_text)
          Item.objects.create(text=request.POST['item_text'])
          return redirect('/')
      # else:
          # new_item_text = ''

      items = Item.objects.all()
      return render(request, 'home.html', {'items': items})

      # item = Item()
      # item.text = request.POST.get('item_text', '')
      # item.save()

      # return render(request, 'home.html', {
          # 'new_item_text': request.POST.get('item_text', ''),
          # 'new_item_text': new_item_text,
      # })
