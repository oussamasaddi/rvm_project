from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
from . import firebaseconfig

database = firebaseconfig.database()





@api_view(['GET'])
def getAllusers(request):
  
    channel_data = database.child('users') 
    return Response(channel_data.get().val())


@api_view(['POST'])
def addUser(request):
  print("****************************************")

  print(request.data)
  channel_data = database.child('users') 
  return Response( channel_data.push(request.data))





     

