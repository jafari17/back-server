from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from infoPrice import get_ohlcv

class LastPriceApi(APIView):

    def get(self, request):

        list_BTCUSDT = get_ohlcv('BTC/USDT')
        last_price_BTCUSDT = list_BTCUSDT[0][-2]

        list_ETHUSDT = get_ohlcv('ETH/USDT')
        last_price_ETHUSDT = list_ETHUSDT[0][-2]

        return Response({'BTCUSDT': last_price_BTCUSDT,
                         'ETHUSDT': last_price_ETHUSDT})