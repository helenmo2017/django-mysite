from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, Http404
from restaurants.models import Restaurant, Food, Comment
from django.utils import timezone
from django.template import RequestContext
from restaurants.forms import CommentForm
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView
# def menu(request):
#     food1 = {'name':'蕃茄炒蛋', 'price': 60, 'comment':'yummy', 'is_spicy':False}
#     food2 = {'name':'蒜泥白肉', 'price': 100, 'comment':'recommend', 'is_spicy':True}
#     foods = [food1, food2]
#     return render_to_response('menu.html', locals())

class RestaurantsView(ListView):
    model = Restaurant
    template_name = 'restaurants_list.html'
    context_object_name = 'restaurants'

# @login_required
# def restaurants_list(request):
#     restaurants = Restaurant.objects.all()
#     request.session['restaurants'] = restaurants
    
#     return render_to_response('restaurants_list.html', locals())

# @login_required
# def menu(request, id):
#     if id:
#         restaurant = Restaurant.objects.get(id=id)
#         return render_to_response('menu.html', locals())
#     else:
#         return HttpResponseRedirect("/restaurant_list/")

class MenuView(DetailView):
    model = Restaurant
    template_name = 'menu.html'
    context_object_name = 'restaurant'
    #pk_url_kwarg = 'id'

    def get(self, request, pk, *args, **kwargs):
        try:
            return super(MenuView, self).get(self, request, pk=pk, *args, **kwargs)
        except Http404:
            return HttpResponseRedirect('/restaurants/list/')

# @login_required
# def comment(request, id):
#     if id:
#         r = Restaurant.objects.get(id=id)
#     else:
#         return HttpResponseRedirect("/restaurant_list/")

#     if request.POST:   
#         f = CommentForm(request.POST)
#         if f.is_valid(): 
#             visitor = request.POST['visitor']
#             content = request.POST['content']
#             email = request.POST['email']
#             date_time = timezone.localtime(timezone.now())
#             c = Comment.objects.create(
#                 visitor = visitor, email = email, content = content,
#                 date_time = date_time, restaurant = r )
#             f=CommentForm(initial={'content':'no comment'})

#     else:
#         f=CommentForm(initial={'content':'whatever'})   
                
#     return render(request, 'comments.html', locals())

    #return render_to_response('comments.html', RequestContext(request, locals()))

class CommentView(FormView, SingleObjectMixin):
    form_class = CommentForm
    template_name = 'comments.html'
    success_url = '/comment/'
    initial={'content':'no comment'}
    model = Restaurant
    context_object_name = 'r'

    def form_valid(self, form):
        Comment.objects.create(
            visitor = form.cleaned_data['visitor'], email = form.cleaned_data['email'], 
            content = form.cleaned_data['content'],
            date_time = timezone.localtime(timezone.now()), restaurant = self.get_object()
        )
        return self.render_to_response(self.get_context_data( form = self.form_class(initial=self.initial) ))

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        return super(CommentView, self).get_context_data(object=self.object, **kwargs)

def set_c(request):
	response = HttpResponse('set your lucky number as 7')
	response.set_cookie('lucky_number',7)
	return response

def get_c(request):
	if 'lucky_number' in request.COOKIES:
		return HttpResponse('your lucky number is {0}'.format(request.COOKIES['lucky_number']))
	else:
		return HttpResponse('no cookies.')

def use_session(request):
	request.session['lucky_number'] = 8
	if 'lucky_number' in request.session:
		lucky_number = request.session['lucky_number']
		response = HttpResponse('Your lucky number is :'+ str(lucky_number))
	del request.session['lucky_number']
	return response

def session_test(request):
    if request.session.test_cookie_worked():
        sid = request.COOKIES['sessionid']
        sid2 = request.session.session_key 

        s = Session.objects.get(pk=sid)
        s_info = 'Session ID:'+ sid +  '<br>SessionID2:' +sid2 + '<br>Expire_date:'+str(s.expire_date) + '<br>Data:'+str(s.get_decoded())
    else:
        s_info = 'cookies is not allow'
    request.session.set_test_cookie()
    return HttpResponse(s_info)

def test(request):
    return HttpResponse("it's a test")

