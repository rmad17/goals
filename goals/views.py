from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, \
        authentication_classes

from .serializers import UserSerializer, GoalSerializer
from .modelops import get_goal_by_uuid, get_user_by_username

# Create your views here.


def home(request):
    return HttpResponse("This is test")


@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data': serializer.data}, status=201)
    return JsonResponse({'error': serializer.errors}, status=400)


@api_view(['POST'])
@authentication_classes((TokenAuthentication))
@permission_classes((IsAuthenticated, ))
def create_goal(request):
    """
    Create a goal
    """
    data = JSONParser().parse(request)
    serializer = GoalSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data': serializer.data}, status=201)
    return JsonResponse({'error': serializer.errors}, status=400)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def goal_list(request, username):
    """
    List all goals.
    """
    user = get_user_by_username(username)
    if str(request.auth) != str(user.auth_token):
        return JsonResponse({"message": "Don't peep into other's house"},
                            status=200)
    serializer = UserSerializer(user)
    return JsonResponse({'data': serializer.data}, status=200)


@csrf_exempt
@api_view(['GET, POST, PUT, DELETE'])
def goal_detail(request, uuid):
    """
    Retrieve, update or delete a goal.
    """
    goal = get_goal_by_uuid(uuid)
    if not goal:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GoalSerializer(goal)
        return JsonResponse({'data': serializer.data}, status=200)

    elif request.method == 'PUT' or request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GoalSerializer(goal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, status=200)
        return JsonResponse({'error': serializer.errors}, status=400)

    elif request.method == 'DELETE':
        goal.delete()
        return JsonResponse({'messsage': 'deleted successfully'}, status=204)
