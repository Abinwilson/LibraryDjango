from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from books.models import Book
from django.contrib.auth.models import User
from books.serializers import bookserializer, userserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from rest_framework.permissions import IsAuthenticated


# # viewsets based
# # ==============
class bookviewset(viewsets.ModelViewSet):  # primary and non primary key based
    permission_classes = [IsAuthenticated, ]
    queryset = Book.objects.all()
    serializer_class = bookserializer


class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer

# # generics class based
# # ====================
# class Booklist(generics.ListCreateAPIView):  # non primary key based
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
#
# class Bookdetail(generics.RetrieveUpdateDestroyAPIView): # primary key based
#     queryset = Book.objects.all()
#     serializer_class = bookserializer

# # mixins class based
# # ==================

# class Booklist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):  # non primary key based
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class Bookdetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):  # primary key based
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
#     def get(self, request, pk):
#         return self.retrieve(request)
#
#     def put(self, request, pk):
#         return self.update(request)
#
#     def delete(self, request, pk):
#         return self.destroy(request)

# # class based
# # ===========

# class Booklist(APIView):  # non primary key based
#     def get(self, request):
#         books = Book.objects.all()
#         s = bookserializer(books, many=True)
#         return Response(s.data)
#
#     def post(self, request):
#         s = bookserializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class Bookdetail(APIView):  # primary key based
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk):
#         book = self.get_object(pk)
#         s = bookserializer(book)
#         return Response(s.data)
#
#     def put(self, request, pk):
#         book = self.get_object(pk)
#         s = bookserializer(book, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # function based
# # ==============

# @api_view(['GET', 'POST'])
# def booklist(request):
#     if request.method == "GET":
#         books = Book.objects.all()
#         b = bookserializer(books, many=True)
#         return Response(b.data)
#     elif request.method == "POST":
#         b = bookserializer(data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data, status=status.HTTP_201_CREATED)
#         return Response(b.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def bookdetail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         b = bookserializer(book)
#         return Response(b.data)
#     elif request.method == "PUT":
#         b = bookserializer(book, data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data, status=status.HTTP_201_CREATED)
#         return Response(b.errors, status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
