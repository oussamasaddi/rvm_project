from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
from . import firebaseconfig

database = firebaseconfig.database()

@api_view(['POST'])
def addbottles(request):
  print("****************************************")

  print(request.data)
  channel_data = database.child('bottles') 
  return Response( channel_data.push(request.data))

@api_view(['GET'])
def getAllbottles(request):
  
    channel_data = database.child('bottles') 
    return Response(channel_data.get().val())

@api_view(['DELETE'])
def deletebottle(request, id):
    machine = database.child("bottles").child(id).get().val()
    if machine:
        database.child("bottles").child(id).remove()
        return Response({"message": "Machine deleted successfully."})
    else:
        return Response({"error": "Machine not found."}, status=404)
    
@api_view(['PUT'])
def updateBottle(request, id):
    machine = database.child("bottles").child(id).get().val()
    if machine:
        data = {
            "type": request.data.get("type", machine["type"]),
            "taille": request.data.get("taille", machine["taille"])
        }
        database.child("bottles").child(id).update(data)
        return Response({"message": "Machine updated successfully."})
    else:
        return Response({"error": "Machine not found."}, status=404)
    

@api_view(['GET'])
def searchbottles(request):
    machines = []

    # retrieve all machines from the database
    all_machines = database.child('bottles').get()

    # loop through all machines and check if they match the search criteria
    for machine in all_machines.each():
        machine_data = machine.val()
        match = True

        # check if each attribute matches the corresponding request parameter
        for key, value in request.GET.items():
            if key not in machine_data or value.lower() not in str(machine_data[key]).lower():
                match = False
                break

        if match:
            machines.append(machine_data)

    return Response(machines)
@api_view(['DELETE'])
def deleteAllMachines(request):
    # get a reference to the machines node in the database
    machines_ref = database.child('bottles')

    # delete all machines from the database
    machines_ref.remove()
    
    return Response({"message": "All machines deleted"})

     