from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Mahasiswa PMPL</title><p>Nama : Radifan Aditya R</p><p>NPM : 1206238293</p></html>')
