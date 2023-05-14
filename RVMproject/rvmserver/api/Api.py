from api import machine
from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
from . import firebaseconfig
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

database = firebaseconfig.database()
class MachineDataSerializer(serializers.Serializer):
    machine_name = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    status = serializers.CharField(required=True)
    num_items = serializers.IntegerField(required=True)
def __init__(self):
        self.machine = Machine()
        self.database = firebase.database()

@api_view(['POST'])
def add_machine_data(request):
    # Get the request data
    data = request.data
    
    # Check if required fields are present
    if 'machine_name' not in data:
        return Response({'error': 'Missing machine_name field'})
    if 'date' not in data:
        return Response({'error': 'Missing date field'})
    if 'status' not in data:
        return Response({'error': 'Missing status field'})
    if 'num_items' not in data:
        return Response({'error': 'Missing num_items field'})

    # Get a reference to the machines node in the database
    machines_ref = database.child('machines')

    # Check if the machine with the given name already exists in the database
    machine_ref = machines_ref.child(data['machine_name'])
    if machine_ref.get() is None:
        # Machine does not exist, so create a new one in the database
        machine_ref.set({
            'name': data['machine_name']
        })

    # Add the machine data object to the database
    machine_data_ref = machine_ref.child('data').push({
        'name': data['machine_name'],
        'date': data['date'],
        'status': data['status'],
        'num_items': data['num_items']
    })
    serializer = MachineDataSerializer(data=request.data)
    if not serializer.is_valid():
        raise ValidationError(serializer.errors)
    data = serializer.validated_data
    return Response({'success': True})
@api_view(['GET'])
def get_machine_data(self):
        machine_data = self.db.child("machines").child(self.machine_name).get().val()
        return machine_data