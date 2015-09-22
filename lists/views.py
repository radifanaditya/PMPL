from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
# def home_page(request):
    # return HttpResponse('<html><title>Mahasiswa PMPL</title><p>Nama : Radifan Aditya R</p><p>NPM : 1206238293</p></html>')

def home_page(request):
      # if request.method == 'POST':
          # return HttpResponse(request.POST['item_text'])
          # new_item_text = request.POST['item_text']
          # Item.objects.create(text=new_item_text)
          # Item.objects.create(text=request.POST['item_text'])
          # return redirect('/lists/the-only-list-in-the-world/')
      # else:
          # new_item_text = ''

      items = Item.objects.all()
      itemsCount = Item.objects.count()
      comment = 'yey, waktunya berlibur'

      if itemsCount == 0:
          comment = 'yey, waktunya berlibur'
      if itemsCount > 0:
          comment = 'sibuk tapi santai'
      if itemsCount >=5:
          comment = 'oh tidak'

      return render(request, 'home.html', {'comment': comment})

      # item = Item()
      # item.text = request.POST.get('item_text', '')
      # item.save()

      # return render(request, 'home.html', {
          # 'new_item_text': request.POST.get('item_text', ''),
          # 'new_item_text': new_item_text,
      # })

def view_list(request):
      items = Item.objects.all()
      return render(request, 'list.html', {'items': items})

def new_list(request):
      Item.objects.create(text=request.POST['item_text'])
      return redirect('/lists/the-only-list-in-the-world/')
