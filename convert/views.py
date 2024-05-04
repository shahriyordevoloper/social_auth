from django.shortcuts import render
from .models import Files
from pdf2docx import Converter
import os,glob
import uuid
from os import listdir
from django.http import HttpResponse 
import os
import glob

def dd(request):
    if request.user.is_superuser:
        for x in os.listdir('media/generate_word'):
            file_path =os.path.join('media/generate_word', x)
            os.remove(file_path)

        for x in os.listdir('media/pdf'):
            file_path =os.path.join('media/pdf', x)
            os.remove(file_path)



        return HttpResponse('<center><h1>Barcha fayllar ochirildi</h1></center>')
    else:
        return HttpResponse('<center><h1>? kiriw mumkin emas</h1></center>')



def home(request):
    if request.method == 'POST':
        uid = uuid.uuid4()
        pdf = Files.objects.create(pdf=request.FILES.get('document_url'))


        cv = Converter(open(f'./media/{pdf.pdf}'))
        cv.convert(f'./media/generate_word/docs{uid}.docx',start=0, end=None)
        cv.close()
 

        return render(request,'index.html',{'url':f'./media/generate_word/docs{uid}.docx'})

    return render(request,'index.html')







