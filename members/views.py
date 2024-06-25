from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member


def members(request):
  mymembers = Member.objects.all().order_by('hcp').values()
  template = loader.get_template('all_members.html')
  context = {
      'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def scoreboard(request):
  myscoreboard = Member.objects.all().order_by('score').values()
  template = loader.get_template('scoreboard.html')
  context = {
      'myscoreboard': myscoreboard,
  }
  return HttpResponse(template.render(context, request))


def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
      'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  mydata = Member.objects.all().order_by('firstname').values()
  template = loader.get_template('template.html')
  context = {
      'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
