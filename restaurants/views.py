from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from restaurants.models import Restaurant, Food, Comment
from django.utils import timezone
from django.template import RequestContext
from restaurants.forms import CommentForm
# def menu(request):
#     food1 = {'name':'蕃茄炒蛋', 'price': 60, 'comment':'yummy', 'is_spicy':False}
#     food2 = {'name':'蒜泥白肉', 'price': 100, 'comment':'recommend', 'is_spicy':True}
#     foods = [food1, food2]
#     return render_to_response('menu.html', locals())
def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', locals())

def menu(request, id):
    if id:
        restaurant = Restaurant.objects.get(id=id)
        return render_to_response('menu.html', locals())
    else:
        return HttpResponseRedirect("/restaurant_list/")

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurant_list/")

    if request.POST:   
        f = CommentForm(request.POST)
        if f.is_valid(): 
            visitor = request.POST['visitor']
            content = request.POST['content']
            email = request.POST['email']
            date_time = timezone.localtime(timezone.now())
            c = Comment.objects.create(
                visitor = visitor, email = email, content = content,
                date_time = date_time, restaurant = r )
            f=CommentForm(initial={'content':'no comment'})

    else:
        f=CommentForm(initial={'content':'whatever'})   
                
    return render(request, 'comments.html', locals())

    #return render_to_response('comments.html', RequestContext(request, locals()))

def set_c(request):
	response = HttpResponse('set your lucky number as 7')
	response.set_cookie('lucky_number',7)
	return response

def get_c(request):
	if 'lucky_number' in request.COOKIES:
		return HttpResponse('your lucky number is {0}'.format(request.COOKIES['lucky_number']))
	else:
		return HttpResponse('no cookies.')
