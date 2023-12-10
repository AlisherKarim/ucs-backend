# from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView

# from discussions.models import Discussion
# from discussions.serializers import DiscussionSerializer


# class DiscussionsList(ListCreateAPIView):
#     queryset = Discussion.objects.all()
#     serializer_class = DiscussionSerializer
#     permission_classes = [IsAuthenticated]
    
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = DiscussionSerializer(queryset)
#         return Response(serializer.data)
    
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)