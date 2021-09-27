from django.shortcuts import render, redirect
import random, time

def gold(request):
   if request.method == "GET":
      # request.session['money'] = 0
      return render(request, "index.html")
   if request.method == "POST":
      request.session.flush()
      request.session['money'] = 0
      request.session['log'] = ""
      return render(request, "index.html")

def process_money(request):
   if "farm" in request.POST:
      x = random.randrange(10,20)
      request.session['money'] += x
      request.session['log'] += f"Grew {x} gold from the farm. ({time.strftime('%m/%d/%Y %H:%M:%S')})\n"
      return redirect("/")
   if "cave" in request.POST:
      x = random.randrange(5,30)
      request.session['money'] += x
      request.session['log'] += f"Found {x} gold in the cave. ({time.strftime('%m/%d/%Y %H:%M:%S')})\n"
      return redirect("/")
   if "house" in request.POST:
      x = random.randrange(0,2)
      if x == 0:
         request.session['money'] = 0
         request.session['log'] += f"Got busted and lost it all to the cops. ({time.strftime('%m/%d/%Y %H:%M:%S')})\n"
      else:
         y = random.randrange(0,100)
         request.session['money'] += y
         request.session['log'] += f"Stole {y} gold from a house. ({time.strftime('%m/%d/%Y %H:%M:%S')})\n"
      return redirect("/")
   if "casino" in request.POST:
      x = random.randrange(-50,50)
      request.session['money'] += x
      if x < 0:
         request.session['log'] += f"Lost {x} gold at the casino. ({time.strftime('%m/%d/%Y %H:%M:%S')})\n"
      else:
         request.session['log'] += f"Won {x} gold at the casino. ({time.strftime('%m/%d/%Y %H:%M:%S')})\n"
      return redirect("/")