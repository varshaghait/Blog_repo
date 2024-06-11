from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Blog
from django.db.models import Q

class BlogView(APIView):
    """
    Blog View handles the retrieval, creation, updating, and deletion of blog posts.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        Retrieve a list of blogs for the authenticated user.
        
        Optional query parameters:
        - search: A string to search for in blog titles and text.

        Returns a list of blogs.
        """
        try:
            blogs = self.get_blogs(request)
            print("BLOGGGGG:",blogs)
            serializer = BlogSerializer(blogs, many=True)
            if serializer.data:
                return Response({
                    'data': serializer.data,
                    'message': 'Blogs fetched successfully'
                }, status=status.HTTP_200_OK)
            else:
                raise IndexError
        except IndexError:
            return Response({
                'message': 'Blog data not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST) 

    def get_blogs(self, request):
            # seven_days_ago = timezone.now().date() - timedelta(days=7)
            # recent_blogs = Blog.objects.filter(created_at__gte=seven_days_ago)
            # serializer = BlogSerializer(recent_blogs, many=True)
            # return Response(serializer.data)
        if request.GET.get('search'):
            search = request.GET.get('search')
            blogs = blogs.filter(Q(title__icontains = search)| Q(blog_text__icontains = search))
        blogs = Blog.objects.filter(user = request.user)
        return blogs

    def post(self, request):
        """
        Create a new blog post.
        
        Expects the following fields in the request data:
        - title: The title of the blog post.
        - blog_text: The content of the blog post.

        Returns the created blog post.
        """
        try:
            # data = request.data
            data = request.data.copy()
            data['user'] = request.user.id
            serializer = BlogSerializer(data = data)
            if not serializer.is_valid():
                return Response({
                    'data' :  serializer.errors,
                    'message' : 'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                'data' : serializer.data,
                'message' : 'blog created successfully'
            }, status=status.HTTP_201_CREATED)
        

        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):
        """
        Update an existing blog post.
        
        Expects the following fields in the request data:
        - uid: The unique identifier of the blog post.
        - title (optional): The new title of the blog post.
        - blog_text (optional): The new content of the blog post.

        Returns the updated blog post.
        """
        try:
            data = request.data

            blog = Blog.objects.filter(uid=data.get('uid')) #use get , rename

            if not blog.exists():
                return Response({
                    'data' : {},
                    'message' : 'invalid id'
                },status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
                return Response({
                    'data' : {},
                    'message' : 'not authorized'
                },status=status.HTTP_400_BAD_REQUEST)
            
            serializer = BlogSerializer(blog[0],data=data, partial = True)

            if not serializer.is_valid():
                return Response({
                    'data' :  serializer.errors,
                    'message' : 'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                'data' : serializer.data,
                'message' : 'blog updated succesfully'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        """
        Delete an existing blog post.
        
        Expects the following fields in the request data:
        - uid: The unique identifier of the blog post.

        Returns a success message if the blog post was deleted.
        """
        try:
            data = request.data

            blog = Blog.objects.filter(uid=data.get('uid'))

            if not blog.exists():
                return Response({
                    'data' : {},
                    'message' : 'invalid id'
                },status=status.HTTP_400_BAD_REQUEST)


            if request.user != blog[0].user:
                return Response({
                    'data' : {},
                    'message' : 'unauthorized request'
                },status=status.HTTP_400_BAD_REQUEST)
            
            blog[0].delete()
            return Response({
                'data' : {},
                'message' : 'blog deleted'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

            
    