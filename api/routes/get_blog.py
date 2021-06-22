from rest_framework.response import Response 
from rest_framework.views import APIView
from ..models import Blog
from ..serializers import BlogApi



class GetBlog(APIView):
	def get(self, request):

		if(request.method == "GET"):
			
			db_data = Blog.objects.all()
			ser = BlogApi(db_data, many=True)
			print(ser.data)

			return Response(ser.data)

