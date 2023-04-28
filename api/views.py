from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def postRequest(request):
    park_ids = 155
    summary = request.data['result']
    for i in summary:
        if park_ids == i['park_id']:
            data = {
                "success": True
            }
        else:
            data = {
                "success": False
            }
    return Response(data)
