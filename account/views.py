from main.models import User
from main.serializers import UserSer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from .tokens import RefreshToken

@api_view(['POST'])
def login_user_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                token = get_tokens_for_user(usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                    'token': token
                }
            else:
                status = 403
                message = "Invalid Password or Username !"
                data = {
                    'status': status,
                    'message': message
                }
        except User.DoestNotExist:
            status = 404,
            message = "This User is not defined !"
            data = {
                'status': status,
                'mesaage': message
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def singup_user_view(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        new = User.objects.create_user(
            full_name=full_name,
            password=password,
            address=address,
            phone_number=phone_number,
        )
        ser = Userserilaizer(new)
        return Response(ser.data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_user_view(request):
    logout(request)
    return Response({'data': 'succes'})


@api_view(['PUT'])
def edit_user_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.POST.get('username')
            password = request.POST.get('pawword')
            user.username = username
            if password is not None:
                user.set_password(password)
            user.save()
            ser = Userserilaizer(user)
            return Response(ser.data)
        except:
            staus = 404
            message = "Request failed"
            data = {
                'status': status,
                'message': message,
            }
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message':message,
        }
        return Response(data)


@api_view(['DELETE'])
def delete_user_view(requst, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        data = {
            'message': "User deleted successfully"
        }
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            "message": message
        }
        return Response(data)

