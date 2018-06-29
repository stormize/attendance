from addpeople.models import people
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import date
import datetime
from django.core import serializers


def afrad_line(req):
    #data for line chart type=0
    data1 = people.objects.filter(date__date=date.today(),sector=5,attendance=1,type=0).values('name').distinct()
    yesterday=date.today()-datetime.timedelta(days=1)
    data2 = people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=0).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=2)
    data3=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=0).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=3)
    data4=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=0).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=4)
    data5=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=0).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=5)
    data6=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=0).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=6)
    data7=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=0).values('name').distinct()
    #data for pie chart type=0
    pie1=people.objects.filter(date__date=date.today(),sector=5,attendance=1,type=0).values('name').distinct().count()
    pie2=people.objects.filter(date__date=date.today(),sector=5,attendance=2,type=0).values('name').distinct().count()
    pie3=people.objects.filter(date__date=date.today(),sector=5,attendance=3,type=0).values('name').distinct().count()
    pie4=people.objects.filter(date__date=date.today(),sector=5,attendance=4,type=0).values('name').distinct().count()
    pie5=people.objects.filter(date__date=date.today(),sector=5,attendance=5,type=0).values('name').distinct().count()
    pie6=people.objects.filter(date__date=date.today(),sector=5,attendance=6,type=0).values('name').distinct().count()
    #data for line chart type=1
    mydata1 = people.objects.filter(date__date=date.today(),sector=5,attendance=1,type=1).values('name').distinct()
    yesterday=date.today()-datetime.timedelta(days=1)
    mydata2 = people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=1).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=2)
    mydata3=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=1).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=3)
    mydata4=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=1).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=4)
    mydata5=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=1).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=5)
    mydata6=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=1).values('name').distinct()
    yesterday=yesterday-datetime.timedelta(days=6)
    mydata7=people.objects.filter(date__date=yesterday,sector=5,attendance=1,type=1).values('name').distinct()
    #data for pie chart type=1
    mypie1=people.objects.filter(date__date=date.today(),sector=5,attendance=1,type=1).values('name').distinct().count()
    mypie2=people.objects.filter(date__date=date.today(),sector=5,attendance=2,type=1).values('name').distinct().count()
    mypie3=people.objects.filter(date__date=date.today(),sector=5,attendance=3,type=1).values('name').distinct().count()
    mypie4=people.objects.filter(date__date=date.today(),sector=5,attendance=4,type=1).values('name').distinct().count()
    mypie5=people.objects.filter(date__date=date.today(),sector=5,attendance=5,type=1).values('name').distinct().count()
    mypie6=people.objects.filter(date__date=date.today(),sector=5,attendance=6,type=1).values('name').distinct().count()
    #dic to render
    data= {
    "data1":data1.count(),
    "date1":date.today(),
    "data2":data2.count(),
    "date2":date.today()-datetime.timedelta(days=1),
    "data3":data3.count(),
    "date3":date.today()-datetime.timedelta(days=2),
    "data4":data4.count(),
    "date4":date.today()-datetime.timedelta(days=3),
    "data5":data5.count(),
    "date5":date.today()-datetime.timedelta(days=4),
    "data6":data6.count(),
    "date6":date.today()-datetime.timedelta(days=5),
    "data7":data7.count(),
    "date7":date.today()-datetime.timedelta(days=6),
    "pie1":pie1,
    "pie2":pie2,
    "pie3":pie3,
    "pie4":pie4,
    "pie5":pie5,
    "pie6":pie6,
    "mydata1":mydata1.count(),
    "mydate1":date.today(),
    "mydata2":mydata2.count(),
    "mydate2":date.today()-datetime.timedelta(days=1),
    "mydata3":mydata3.count(),
    "mydate3":date.today()-datetime.timedelta(days=2),
    "mydata4":mydata4.count(),
    "mydate4":date.today()-datetime.timedelta(days=3),
    "mydata5":mydata5.count(),
    "mydate5":date.today()-datetime.timedelta(days=4),
    "mydata6":mydata6.count(),
    "mydate6":date.today()-datetime.timedelta(days=5),
    "mydata7":mydata7.count(),
    "mydate7":date.today()-datetime.timedelta(days=6),
    "mypie1":mypie1,
    "mypie2":mypie2,
    "mypie3":mypie3,
    "mypie4":mypie4,
    "mypie5":mypie5,
    "mypie6":mypie6,
       }
    return JsonResponse(data)
def dashboard(req):
    return render(req,'afrad/dashboard.html')
