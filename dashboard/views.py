from django.shortcuts import render, HttpResponse
import serial
import io

# Create your views here.
def index(request):
    with serial.Serial('/dev/serial0', 115200, timeout=1) as ser:
        sio = io.TextIOWrapper(io.BufferedReader(ser))
        temperature = sio.readline()
        return HttpResponse("<h>{}</h>".format(temperature))
