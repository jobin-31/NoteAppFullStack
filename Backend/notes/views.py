from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import NoteInfo
from .serializers import NoteSerializer

class NoteListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = NoteInfo.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # sets user automatically
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
