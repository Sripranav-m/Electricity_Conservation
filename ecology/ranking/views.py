from django.shortcuts import render
from django.views import View
from .models import ranking,query
from datetime import date


def main_method(request):
    if request.method=="POST":
        print("---")
        name_g=request.POST.get("fullname")
        email_g=request.POST.get("email")
        phone_g=request.POST.get("phone")
        query_g=request.POST.get("query")
        print(query)
        obj=query(name=name_g,email=email_g,phone=phone_g,query=query_g)
        obj.save()
    try:
        ranklist=ranking.objects.all()
        find=ranklist[ranking.objects.count()-1]
        dict={101:find.units101,102:find.units102,103:find.units103,104:find.units104,105:find.units105,106:find.units106,107:find.units107,108:find.units108,109:find.units109,110:find.units110}
        dict=sorted(dict.items(), key=lambda x: x[1])
        maindict={'date_day_year':find.month,'rank1':dict[0][0],'rank2':dict[1][0],'rank3':dict[2][0],'units1':dict[0][1],'units2':dict[1][1],'units3':dict[2][1]}
        try:
            last1_month=ranklist[ranking.objects.count()-2]
            last1={101:last1_month.units101,102:last1_month.units102,103:last1_month.units103,104:last1_month.units104,105:last1_month.units105,106:last1_month.units106,107:last1_month.units107,108:last1_month.units108,109:last1_month.units109,110:last1_month.units110}
            last1=sorted(last1.items(), key=lambda x: x[1])
            maindict1={'1month':last1_month.month,'1rank1':last1[0][0],'1rank2':last1[1][0],'1rank3':last1[2][0]}
            maindict.update(maindict1)
        except:
            maindict1={'1month':"--",'1rank1':"--",'1rank2':"--",'1rank3':"--"}
            maindict.update(maindict1)
        try:
            last2_month=ranklist[ranking.objects.count()-3]
            last2={101:last2_month.units101,102:last2_month.units102,103:last2_month.units103,104:last2_month.units104,105:last2_month.units105,106:last2_month.units106,107:last2_month.units107,108:last2_month.units108,109:last2_month.units109,110:last2_month.units110}
            last2=sorted(last2.items(), key=lambda x: x[1])
            maindict2={'2month':last2_month.month,'2rank1':last2[0][0],'2rank2':last2[1][0],'2rank3':last2[2][0]}
            maindict.update(maindict2)
        except:
            maindict2={'2month':"--",'2rank1':"--",'2rank2':"--",'2rank3':"--"}
            maindict.update(maindict2)
        try:
            last3_month=ranklist[ranking.objects.count()-4]
            last3={101:last3_month.units101,102:last3_month.units102,103:last3_month.units103,104:last3_month.units104,105:last3_month.units105,106:last3_month.units106,107:last3_month.units107,108:last3_month.units108,109:last3_month.units109,110:last3_month.units110}
            last3=sorted(last3.items(), key=lambda x: x[1])
            maindict3={'3month':last3_month.month,'3rank1':last3[0][0],'3rank2':last3[1][0],'3rank3':last3[2][0]}
            maindict.update(maindict3)
        except:
            maindict3={'3month':"--",'3rank1':"--",'3rank2':"--",'3rank3':"--"}
            maindict.update(maindict3)
    except:
        maindict={'1rank1':"--",'1rank2':"--",'1rank3':"--",'2rank1':"--",'2rank2':"--",'2rank3':"--",'3rank1':"--",'3rank2':"--",'3rank3':"--",'1month':"--",'2month':"--",'3month':"--",'rank1':"--",'rank2':"--",'rank3':"--",'units1':"--",'units2':"--",'units3':"--"}
    return render(request,"index.html",maindict)