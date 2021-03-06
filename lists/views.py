from django.core.exceptions import ValidationError
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

def blog_page(request):
	return render(request, 'blog_temp.html')

def view_list(request, list_id):
      # items = Item.objects.all()
      list_ = List.objects.get(id=list_id)
      error = None;
      # items = Item.objects.filter(list=list_)
      if request.method == 'POST':
          #Item.objects.create(text=request.POST['item_text'], list=list_)
          try:
          	  item = Item(text=request.POST['item_text'], list=list_)
          	  item.full_clean()
          	  item.save()
          	  return redirect(list_)
          except ValidationError:
          	  error = "You can't have an empty list item"
      comment = ''
      counterlist = Item.objects.filter(list_id=list_.id).count()

      if counterlist == 0 :
          comment = 'yey, waktunya berlibur'
      elif (counterlist > 0) and (counterlist < 5) :
          comment = 'sibuk tapi santai'
      else :
          comment = 'oh tidak'

      return render(request, 'list.html', {'list': list_, 'error': error, 'comment': comment})

def new_list(request):
      list_ = List.objects.create()
      item = Item.objects.create(text=request.POST['item_text'], list=list_)
      try:
          item.full_clean()
          item.save()
      except ValidationError:
      	  list_.delete()
      	  error = "You can't have an empty list item"
      	  return render(request, 'home.html', {"error": error})
      return redirect(list_)
