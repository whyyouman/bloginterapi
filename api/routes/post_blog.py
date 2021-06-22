from rest_framework.response import Response 
from rest_framework.views import APIView
from ..models import Blog
from ..serializers import BlogApi



class PostBlog(APIView):
	def post(self, request):
		try:
			if(request.method == "POST"):
				image = request.data['image']
				title = request.data['title']
				content = request.data['content']
				date = request.data['date']

				Blog.objects.create(
					image = image,
					title = title,
					content = content,
					date = date,
				).save()

			return Response({'message': 'Success'})
		except:
			return Response({'message': 'Something Went Wrong !'})


