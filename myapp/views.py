from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .models import *
from .forms import *

def home_page(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			newform=form.save()															
			with open(settings.MEDIA_ROOT + '/' + newform.files.name) as csvfile:
				#return os.path.basename(value.file.name)
				reader = csv.DictReader(csvfile)
				for row in reader:
					f_name = row['c1']
					l_name = row['c2']
					e_mail = row['c3']
					mobile = row['c4']
					if not Tabletwo.objects.filter(c3=e_mail).exists():
						tablet = Tabletwo(c1=f_name, c2=l_name, c3=e_mail, c4=mobile)
						tablet.save()
			return redirect('home_page')
		else:
			logger.error(form.errors)
	else:
		form = FileForm()

	return render(request, 'home.html', {'form': form})