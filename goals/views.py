from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, GroupSerializer, GoalSerializer
from .modelops import get_all_goals, get_goal_by_uuid

# Create your views here.


def home(request):
    return HttpResponse("This is test")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@csrf_exempt
def goal_list(request):
    """
    List all goals.
    """
    if not request.method == 'GET':
        return JsonResponse({'msg': 'invalid request'}, status=403)
    goals = get_all_goals
    serializer = GoalSerializer(goals, many=True)
    return JsonResponse({'data': serializer.data}, status=200)


@csrf_exempt
def create_goal(request):
    """
    Create a goal
    """
    if not request.method == 'POST':
        return JsonResponse({'message': 'invalid request'}, status=403)
    data = JSONParser().parse(request)
    serializer = GoalSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data': serializer.data}, status=201)
    return JsonResponse({'error': serializer.errors}, status=400)


@csrf_exempt
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
