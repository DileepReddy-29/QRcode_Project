from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings
# Create your views here.

def qr_generator(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        
        if form.is_valid():
            company_name = form.cleaned_data['Company_name']
            url = form.cleaned_data['url']
            # Generate QR Code
            img = qrcode.make(url)
            file_name = company_name.replace(" ", "_").lower()+".png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            img.save(file_path)


            #Create URL for the QR Code
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            context = {
                'company_name': company_name,
                'qr_url': qr_url,
                'file_name': file_name,

            }
            
            return render(request, 'qr_code_display.html', context)
    else:
        form = QRCodeForm()
        context = {
            'form': form,

        }
        return render(request, 'qr_generator.html', context)
