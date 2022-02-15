from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from datetime import date
from .serializers import AgeSerializer


# Create your views here.
class AgeCalculate(APIView):
    
    def post(self,request):
        
        serializer = AgeSerializer(data = request.data)
        
        try:
            
            if serializer.is_valid():
                today_year = date.today().year
                birth_year = serializer['year'].value
                today_month = date.today().month
                birth_month = serializer['month'].value
                today_day = date.today().day
                birth_day = serializer['day'].value
                
                if(birth_month<=today_month and birth_day<=today_day):
                    return HttpResponse(today_year-birth_year)
                else:
                    return HttpResponse(today_year-birth_year-1)
        
        except:
            return HttpResponse("Enter details correctly")

    
def index(request):
    return HttpResponse('Please open this url to check your age => http://127.0.0.1:8000/api/age/')