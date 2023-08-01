from rest_framework.views import APIView
from django.http import HttpResponse
from .models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password


def greet(name, age):
    return f"Hello {name}. Your age is {age}."


# Create your views here.
class Hello(APIView):
    def get(self, request):
        return HttpResponse("Hello Guest")

    def post(self, request):
        name = request.data.get("name")
        age = request.query_params.get("age")
        wish = greet(name, age)
        return HttpResponse(wish)


class Signup(APIView):
    def post(self, request):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        name = request.query_params.get("name")
        profession = request.query_params.get("profession")
        age = request.query_params.get("age")
        # Find user based on a condition
        existingUser = User.objects.filter(username=username).first()
        if existingUser:
            return HttpResponse("User already exists")
        # Encrypt a password
        encrypted_password = make_password(password)
        newUser = User.objects.create(
            username=username,
            password=encrypted_password,
            name=name,
            profession=profession,
            age=age,
        )
        newUser.save()
        return HttpResponse(f"Hi {name} you are sucessfully registered.")


def user_entity(item):
    return {
        "username": item.username,
        "name": item.name,
        "profession": item.profession,
        "age": item.age,
        "is_active":item.is_online,
    }


def users_entity(entity):
    lst = [user_entity(item) for item in entity]
    return lst


class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        return JsonResponse(users_entity(users), safe=False)

    def delete(self, request):
        username = request.query_params.get("username")
        user = User.objects.filter(username=username)
        user.delete()
        print("status ")
        return HttpResponse("user deleted")

    def put(self, request):
        username = request.query_params.get("username")
        profession = request.query_params.get("profession")
        user = User.objects.get(username=username)
        user.profession = profession
        user.save()
        return HttpResponse(f"Hi {user.name}, your profession updated.")


class OnlineUsers(APIView):
    def get(self, request):
        online_users = User.objects.filter(is_online=True)
        json_data = users_entity(online_users)
        return JsonResponse(json_data, safe=False)
   
    def put(self, request):
        username = request.query_params.get("username")
        is_online = request.query_params.get("is_online")
        user = User.objects.get(username=username)
        user.is_online = is_online
        user.save()
        return HttpResponse(f"Hi {user.name}, your online status changed to {is_online}.")


class Login(APIView):
    def post(self, request):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        # Find user based on a condition
        user = User.objects.filter(username=username).first()
        if not user:
            return HttpResponse("User does not exist")
        encrypted_password = user.password
        # Check if a provided password matches the encrypted password
        is_password_matched = check_password(password, encrypted_password)
        if is_password_matched:
            json_data = user_entity(user)
            message = f"Hello {user.name}, you are a {json_data['profession']}."
            print(message)
            return HttpResponse(message)
        else:
            return HttpResponse("Password does not match!")
