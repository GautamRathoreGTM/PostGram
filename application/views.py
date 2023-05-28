from django.shortcuts import render
# from requests import Response

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PostBlog, Like, UserTable

class Postgram(APIView):
    def post(self, request):
        data = request.data
        user_id = data["user_id"]
        name = data["name"]
        email = data["email"]
        password = data["password"]
        status = data["status"]

        post_id = data["post_id"]
        title = data["title"]
        description = data["description"]
        content = data["content"]

        like_id = data["like_id"]
        like_status = data["like_status"]

        context = {}
        try:
            if not UserTable.objects.filter(user_id=user_id).exists():
                user_obj = UserTable.objects.create(
                    user_id = user_id,
                    name = name,
                    email = email,
                    password = password,
                    status = status,
                )
                user_obj.save()                
        except:
            context = {
                "status" : 200,
                "message": "Find issue while creating User"
            }
            return Response(context)

        try:
            if not PostBlog.objects.filter(post_id=post_id).exists():
                user_obj = UserTable.objects.get(user_id=user_id) 
                post_obj = PostBlog.objects.create(
                    user_id=user_obj,
                    post_id=post_id,
                    title=title,
                    description=description,
                    content=content,
                )
                post_obj.save()                
        except:
            context = {
                "status" : 200,
                "message": "Find issue while creating Post or Blog"
            }
            return Response(context)

        try:
            if not Like.objects.filter(like_id=like_id).exists():
                user_obj = UserTable.objects.get(user_id=user_id) 
                post_obj = PostBlog.objects.get(post_id=post_id)
                like_obj = Like.objects.create(
                    user_id=user_obj,
                    post_id=post_obj,
                    like_id=like_id,
                    like_status=like_status
                )
                like_obj.save()                    
        except:
            context = {
                "status" : 200,
                "message": "Find issue while creating Like for post"
            }
            return Response(context)

        context = {
            "status" : 200,
            "message": "Data created Successfully"
        }
        return Response(context)
    
    def put(self, request):
        data = request.data
        user_id = data["user_id"]
        name = data["name"]
        email = data["email"]
        password = data["password"]
        status = data["status"]

        post_id = data["post_id"]
        title = data["title"]
        description = data["description"]
        content = data["content"]

        like_id = data["like_id"]
        like_status = data["like_status"]

        try:
            if UserTable.objects.filter(user_id=user_id).exists():
                user_obj = UserTable.objects.get(user_id = user_id)
                user_obj.name =  name                                          
                user_obj.email =  email                                          
                user_obj.password =  password                                          
                user_obj.status =  status                                          
                user_obj.save()  
        except:
            context = {
                "status" : 200,
                "message": "Find issue while creating User"
            }
            return Response(context)
        
        try:
            if PostBlog.objects.filter(post_id=post_id).exists():
                user_obj = UserTable.objects.get(user_id=user_id) 
                post_obj = PostBlog.objects.get(user_id=user_obj, post_id=post_id)
                post_obj.title = title
                post_obj.description = description
                post_obj.content = content
                post_obj.save()                
        except:
            context = {
                "status" : 200,
                "message": "Find issue while creating Post or Blog"
            }
            return Response(context)
        
        try:
            if Like.objects.filter(like_id=like_id).exists():
                user_obj = UserTable.objects.get(user_id=user_id) 
                post_obj = PostBlog.objects.get(post_id=post_id)
                like_obj = Like.objects.get(user_id=user_obj, post_id=post_obj, like_id=like_id)
                like_obj.like_status = like_status
                like_obj.save()                    
        except:
            context = {
                "status" : 200,
                "message": "Find issue while creating Like for post"
            }
            return Response(context)

        context = {
            "status" : 200,
            "message": "Data Updated Successfully"
        }
        return Response(context)


    def get(self, request):
        data = request.data
        user_id = data["user_id"]

        context = {}
        user_data_list = []
        try:
            if UserTable.objects.filter(user_id=user_id).exists():

                user_obj = UserTable.objects.get(user_id = user_id)
                if user_obj.status =="PUBLIC":
                    user_objs = UserTable.objects.all()
                    for user_data in user_objs:
                        data_list = {}
                        post_list = []
                        post_objs = PostBlog.objects.filter(user_id=user_data)
                        for post_obj in post_objs:
                            post_dict = {}
                            like_obj_count = Like.objects.filter(user_id=user_data, post_id=post_obj, like_status=True).count()
                            post_dict["title"] = post_obj.title 
                            post_dict["description"] = post_obj.description 
                            post_dict["content"] = post_obj.content 
                            post_dict["likes"] = like_obj_count
                            post_list.append(post_dict)

                        data_list["name"] = user_data.name
                        data_list["email"] = user_data.email
                        data_list["status"] = user_data.status
                        data_list["posts"] = post_list
                        user_data_list.append(data_list)
                    context = {
                        "status" : 200,
                        "Message": "User data fetch Successfully.",
                        "Data": user_data_list
                    }
                    return Response(context)

                else:
                    post_objs = PostBlog.objects.filter(user_id=user_obj)
                    post_list = []
                    for post_obj in post_objs:
                        post_dict = {}
                        like_obj_count = Like.objects.filter(user_id=user_obj, post_id=post_obj, like_status=True).count()
                        post_dict["title"] = post_obj.title 
                        post_dict["description"] = post_obj.description 
                        post_dict["content"] = post_obj.content 
                        post_dict["likes"] = like_obj_count
                        post_list.append(post_dict)
                        
                    user_data = {
                        "name" : user_obj.name,
                        "email": user_obj.email,
                        "status": user_obj.status,
                        "posts": post_list
                    }
                    user_data_list.append(user_data)
                    context = {
                        "status" : 200,
                        "Message": "User data fetch Successfully.",
                        "Data": user_data_list
                    }
                    return Response(context)
            else:
                context = {
                    "status" : 200,
                    "Message": "No data available for this User.",
                    "Data": user_data_list
                }
                return Response(context)
        except:
            context = {
                "status" : 200,
                "message": "Find issue while fitch User data"           
            }

            return Response(context)
        
    def delete(self, request):
        data = request.data
        user_id = data["user_id"]
        post_id = data["post_id"]
        like_id = data["like_id"]

        
        context = {}
        if user_id != None:
            try:
                UserTable.objects.filter(user_id=user_id).delete()                 
            except:
                context = {
                    "status" : 200,
                    "message": "Find issue while removing User"
                }
                return Response(context)
            
        if post_id != None:
            try:
                PostBlog.objects.filter(post_id=post_id).delete()                 
            except:
                context = {
                    "status" : 200,
                    "message": "Find issue while removing User"
                }
                return Response(context)
            
        if like_id != None:
            try:
                Like.objects.filter(like_id=like_id).delete()                 
            except:
                context = {
                    "status" : 200,
                    "message": "Find issue while removing User"
                }
                return Response(context)

        context = {
            "status" : 200,
            "message": "Data deleted successfuly."           
        }

        return Response(context)
            
        
        



        
   


