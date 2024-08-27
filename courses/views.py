import uuid
from datetime import datetime

from decouple import config
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shared import generateRefNo

from .models import Courses, Chapter, Lesson
from .serializers import CoursesSerializer, ChapterSerializer, LessonSerializer

# Create your views here.


class CourseView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request):
        course = Courses(
            name=request.data["name"],
            description=request.data["description"],
            price=request.data["price"],
            url=uuid.uuid4(),
        )
        if request.FILES != None and request.FILES["thumbnail"] != None:
            course.thumbnail = request.data["thumbnail"]

        course.save()

        res = {"status": 1, "message": "Course added successfuly"}

        return JsonResponse(res)

    def get(self, request, url=None):

        if url == None:
            courses= Courses.objects.filter(visibility=True)
            serializedCourses = CoursesSerializer(courses, many=True)

            return JsonResponse({"status": 1, "data": serializedCourses.data})

        else:
            try:
                course = Courses.objects.get(url=url, visibility=True)
                serializedCourse = CoursesSerializer(course)

                return JsonResponse({"status": 1, "data": serializedCourses.data})

            except course.DoesNotExist as e:
                return Response("Course not found", status=status.HTTP_404_NOT_FOUND)

    @permission_classes([IsAuthenticated])
    def put(self, request, url):
        try:
            course = Courses.objects.get(url=url)

        except Courses.DoesNotExist as e:
            return Response("Course not found", status=status.HTTP_404_NOT_FOUND)

        course.name = request.data["name"]
        course.description = request.data["description"]
        course.price = request.data["price"]
        course.date_updated = datetime.now()

        if request.FILES != None:
            course.thumbnail = request.data["thumbnail"]

        course.save()

        res = {"status": 1, "message": "Course edited successfuly"}

        return JsonResponse(res)

    @permission_classes([IsAuthenticated])
    def delete(self, request):

        for url in request.data["urls"]:
            try:
                course = Courses.objects.get(url=url)

            except Courses.DoesNotExist as e:
                return Response("Course not found", status=status.HTTP_404_NOT_FOUND)

            course.visibility = False

            course.save()

        res = {"status": 1, "message": "Course edited successfuly"}

        return JsonResponse(res)
    
# CHAPTER VIEW
class ChapterView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request):
        chapter = Chapter(
            course=Courses.objects.get(url=request.data.get("url")),
            name=request.data["name"],
            description=request.data["description"],
            url=uuid.uuid4(),
        )
        if request.FILES != None and request.FILES["thumbnail"] != None:
            chapter.thumbnail = request.data["thumbnail"]

        chapter.save()

        res = {"status": 1, "message": "Chapter added successfuly"}

        return JsonResponse(res)

    def get(self, request, url=None):

        if url == None:
            chapters = Chapter.objects.filter(visibility=True)
            serializedChapters = ChapterSerializer(chapters, many=True)

            return JsonResponse({"status": 1, "data": serializedChapters.data})

        else:
            try:
                chapter = Chapter.objects.get(url=url, visibility=True)
                serializedChapter = ChapterSerializer(chapter)

                return JsonResponse({"status": 1, "data": serializedChapter.data})

            except Chapter.DoesNotExist as e:
                return Response("Chapter not found", status=status.HTTP_404_NOT_FOUND)

    @permission_classes([IsAuthenticated])
    def put(self, request, url):
        try:
            chapter = Chapter.objects.get(url=url)

        except Chapter.DoesNotExist as e:
            return Response("Chapter not found", status=status.HTTP_404_NOT_FOUND)

        chapter.name = request.data["name"]
        chapter.description = request.data["description"]
        chapter.date_updated = datetime.now()

        if request.FILES != None:
            chapter.thumbnail = request.data["thumbnail"]

        chapter.save()

        res = {"status": 1, "message": "Chapter edited successfuly"}

        return JsonResponse(res)

    @permission_classes([IsAuthenticated])
    def delete(self, request):

        for url in request.data["urls"]:
            try:
                chapter = Chapter.objects.get(url=url)

            except Chapter.DoesNotExist as e:
                return Response("Chapter not found", status=status.HTTP_404_NOT_FOUND)

            chapter.visibility = False

            chapter.save()

        res = {"status": 1, "message": "Chapter deleted successfuly"}

        return JsonResponse(res)
    

# LESSON VIEW
class LessonView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request):
        lesson = Lesson(
            name=request.data["name"],
            description=request.data["description"],
            url=uuid.uuid4(),
        )
        if request.FILES != None and request.FILES["thumbnail"] != None:
            lesson.thumbnail = request.data["thumbnail"]

        if request.FILES != None and request.FILES["video"] != None:
            lesson.video = request.data["video"]

        lesson.save()

        res = {"status": 1, "message": "Lesson added successfuly"}

        return JsonResponse(res)

    def get(self, request, url=None):

        if url == None:
            lessons = Lesson.objects.filter(visibility=True)
            serializedLessons = LessonSerializer(lessons, many=True)

            return JsonResponse({"status": 1, "data": serializedLessons.data})

        else:
            try:
                lesson = Lesson.objects.get(url=url, visibility=True)
                serializedLesson = LessonSerializer(lesson)

                return JsonResponse({"status": 1, "data": serializedLesson.data})

            except Chapter.DoesNotExist as e:
                return Response("Lesson not found", status=status.HTTP_404_NOT_FOUND)

    @permission_classes([IsAuthenticated])
    def put(self, request, url):
        try:
            lesson = Lesson.objects.get(url=url)

        except Lesson.DoesNotExist as e:
            return Response("Lesson not found", status=status.HTTP_404_NOT_FOUND)

        lesson.name = request.data["name"]
        lesson.description = request.data["description"]
        lesson.content = request.data["content"]
        lesson.date_updated = datetime.now()

        if request.FILES != None:
            lesson.thumbnail = request.data["thumbnail"]

        lesson.save()

        res = {"status": 1, "message": "Lesson edited successfuly"}

        return JsonResponse(res)

    @permission_classes([IsAuthenticated])
    def delete(self, request):

        for url in request.data["urls"]:
            try:
                lesson = Lesson.objects.get(url=url)

            except Lesson.DoesNotExist as e:
                return Response("Lesson not found", status=status.HTTP_404_NOT_FOUND)

            lesson.visibility = False

            lesson.save()

        res = {"status": 1, "message": "Lessons deleted successfuly"}

        return JsonResponse(res)
