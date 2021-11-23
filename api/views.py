from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import encoder
import decoder
# Create your views here.


class Encode(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

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
    """
    View to list decode the system.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        if request.GET.get('encoded_sentence') and request.GET.get('orginal_words'):
            sentence = request.GET.get('sentence')

            decoded_sentence = decoder.decode_sentence(sentence)
            response_obj = {
                "decoded_sentence": decoded_sentence[0],
            }
            return Response(response_obj)
        response_obj = {
            "error": "encoded_sentence or orginal_words param is not provided"}
        return Response(response_obj)
