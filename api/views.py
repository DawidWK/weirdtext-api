from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import encoder
import decoder
# Create your views here.


class Encode(APIView):
    def get(self, request, format=None):
        if request.GET.get('sentence'):
            sentence = request.GET.get('sentence')

            encoded_sentence = encoder.encode_sentence(sentence)
            response_obj = {
                "encoded_sentence": encoded_sentence[0],
                "orginal_words": encoded_sentence[1]
            }
            return Response(response_obj)

        response_obj = {"error": "sentence param is not provided"}
        return Response(response_obj)


class Decode(APIView):
    def get(self, request, format=None):
        if request.GET.get('encoded_sentence') and request.GET.get('orginal_words'):
            sentence = request.GET.get('encoded_sentence')
            orginal_words = request.GET.get('orginal_words')
            decoded_sentence = decoder.decode_sentence(sentence, orginal_words)
            response_obj = {
                "decoded_sentence": decoded_sentence,
            }
            return Response(response_obj)
        response_obj = {
            "error": "encoded_sentence or orginal_words param is not provided"}
        return Response(response_obj)
