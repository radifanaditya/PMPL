from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from lists.models import Item, List

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

      # if itemsCount == 0:
          # comment = 'yey, waktunya berlibur'
      # if itemsCount > 0:
          # comment = 'sibuk tapi santai'
      # if itemsCount >=5:
          # comment = 'oh tidak'

      return render(request, 'home.html', {'comment': comment})

      # item = Item()
      # item.text = request.POST.get('item_text', '')
      # item.save()

      # return render(request, 'home.html', {
          # 'new_item_text': request.POST.get('item_text', ''),
          # 'new_item_text': new_item_text,
      # })

def view_list(request, list_id):
      # items = Item.objects.all()
      list_ = List.objects.get(id=list_id)
      # items = Item.objects.filter(list=list_)
      comment = ''
      counterlist = Item.objects.filter(list_id=list_.id).count()

      if counterlist == 0 :
          comment = 'yey, waktunya berlibur'
      elif (counterlist > 0) and (counterlist < 5)
          comment = 'sibuk tapi santai'
      else
          comment = 'oh tidak'

      return render(request, 'list.html', {'list': list_, 'comment': comment})

def new_list(request):
      list_ = List.objects.create()
      Item.objects.create(text=request.POST['item_text'], list=list_)
      return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
      list_ = List.objects.get(id=list_id)
      Item.objects.create(text=request.POST['item_text'], list=list_)
      return redirect('/lists/%d/' % (list_.id,))
