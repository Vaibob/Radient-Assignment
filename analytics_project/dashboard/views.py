from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Order
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

def chart(request):
    return render(request, 'chart.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        x_ = Order.objects.filter(equity_id=request.session['equity_id']).order_by('date').values()
        labels, chartdata = [], []
        for row in x_:
            labels.append(row['date'])
            chartdata.append(row['returns'])
        chartLabel = "Equity return"
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)

def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        if request.POST.get('but') == 'sub':
            request.session['equity_id'] = request.POST['inp']

            equities = {
                '10277':'Agilent Technologies Inc',
                '10278':'Alcoa Inc', 
                '10279':'Yahoo! Inc' ,
                '10280':'American Addiction Centers',
                '10281':'American Airlines Group Inc', 
                '10282':'Altisource Asset Management Corp',
                '10283':'Atlantic American Corp', 
                '10284':"Aaron's, Inc",
                '10285':'Applied Optoelectronics Inc',
                '10286':"AAON, Inc" 
            }

            return render(request, 'chart.html', context={
                'equity_id': request.session['equity_id'],
                'equity_name': equities[request.session['equity_id']]
            })
        if request.POST.get('but') == 'del':
            del_obj = Order.objects.filter(equity_id=request.POST.get('eq'), date=request.POST.get('date')).delete()
            return render(request, 'delete.html', context={
                'del': del_obj
            })