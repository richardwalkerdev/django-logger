from django.http import HttpResponseRedirect
from django.shortcuts import render

#from .forms import NameForm

import logging
import datetime
	
# generate random integer values
import random



def logger(request):
    number1 = random.randint(1000,9999)
    number2 = random.randint(1000,9999)
    now = datetime.datetime.now()
    formatedDate = now.strftime("%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger(__name__)
    healthy_string = f'[{formatedDate}] "HEALTHY" Status: 200 "Message from Logger:" OK'
    warn_string = f'[{formatedDate}] "WARNING" Status: 404 "Message from Logger:" Not Found'
    error_string = f'[{formatedDate}] "ERROR" Status: 500 "Message from Logger:" Internal Server Error'
    info_string = f'[{formatedDate}] "INFO" Status: 200 Customer Credit Card number 4321-4321-{number1}-{number2}'

    if 'OK' in request.POST:
        if 'HEALTHY'  == request.POST.get('OK'):
            logger.error(healthy_string)
            return HttpResponseRedirect('/')
        else:
            pass
    if 'not-found' in request.POST:
        if 'WARN'  == request.POST.get('not-found'):
            logger.error(warn_string)
            return HttpResponseRedirect('/')
        else:
            pass   
    if 'internal-server-error' in request.POST:
        if 'ERROR'  == request.POST.get('internal-server-error'):
            logger.error(error_string)
            return HttpResponseRedirect('/')
        else:
            pass           
    if 'card-number' in request.POST:
        if 'INFO'  == request.POST.get('card-number'):
            logger.error(info_string)
            return HttpResponseRedirect('/')
        else:
            pass               

    # if 'name' in request.POST:
    #     if 'value'  == request.POST.get('name'):
    #         #form = NameForm(request.POST)
    #         logger = logging.getLogger(__name__)
    #         logger.error('Something went wrong!')
    #         return HttpResponseRedirect('/')
    #     else:
    #         form = NameForm()

    return render(request, 'index.html')