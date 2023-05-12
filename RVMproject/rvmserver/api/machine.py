from  rest_framework.response import Response 
from rest_framework.decorators import api_view 
from . import firebaseconfig

database = firebaseconfig.database()





@api_view(['GET'])
def getAllmachines(request):
  
    channel_data = database.child('machines') 
    return Response(channel_data.get().val())


@api_view(['POST'])
def addMachine(request):
  print("****************************************")

  print(request.data)
  channel_data = database.child('machines') 
  return Response( channel_data.push(request.data))

@api_view(['DELETE'])
def deleteMachine(request, id):
    machine = database.child("machines").child(id).get().val()
    if machine:
        database.child("machines").child(id).remove()
        return Response({"message": "Machine deleted successfully."})
    else:
        return Response({"error": "Machine not found."}, status=404)

@api_view(['PUT'])
def updateMachine(request, id):
    machine = database.child("machines").child(id).get().val()
    if machine:
        data = {
            "nom": request.data.get("nom", machine["nom"]),
            "capacity": request.data.get("capacity", machine["capacity"])
        }
        database.child("machines").child(id).update(data)
        return Response({"message": "Machine updated successfully."})
    else:
        return Response({"error": "Machine not found."}, status=404)


@api_view(['GET'])
def searchMachines(request):
    machines = []

    # retrieve all machines from the database
    all_machines = database.child('machines').get()

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
    machines_ref = database.child('machines')

    # delete all machines from the database
    machines_ref.remove()
    
    return Response({"message": "All machines deleted"})

     

