from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializer import DocxUploadSerializer
from .query_doc import query_response
from .new_doc import add_doc

class DocumentViewSet(viewsets.ModelViewSet):
    
    permission_classes=(IsAuthenticated,)
    
    queryset = Document.objects.all()
    serializer_class = DocxUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            uploaded_file = request.data.get('docx_file')
            filename = uploaded_file.name
            
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            add_doc(filename)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        sentence = request.data.get('answer')
        answer = query_response(sentence)
        return Response({'answer': answer}, status=status.HTTP_200_OK)