from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import Createusers
from django.contrib.auth.decorators import login_required
from .chatAI import reply

# Create your views here.
def signin(request):
	if request.method == 'POST':
		form = Createusers(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = Createusers()
	context = {'form': form}

	return render(request, 'chatapp/signin.html', context)


def chat(request):
	user = request.user.username
	content = {'user': user}

	return render(request, 'chatapp/cover.html', content)

@login_required(redirect_field_name='next', login_url='login')
def home(request):
	user = request.user.username
	content = {'user': user}

	return render(request, 'chatapp/heroe.html',content)

def response(request):
	try:
		message = request.GET.get('message')
		tr = reply(message)
		tr = str(tr)
		print(tr)
		answer = tr[9:-1]
		responsedata = {}
		responsedata['message'] = message
		responsedata['replytext'] = answer
		print(message)
		return JsonResponse(responsedata, safe=False)
	except:
		JsonResponse('this is fucked up', safe=False)

