from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserChapter, UserLesson


# class UserChapterAPIView(APIView):
#
#     def post(self, request, user_chapter_id):
#         user_type = request.user.user_type
#         if user_type == 'STUDENT':
#             user_chapter = get_object_or_404(UserChapter, pk=user_chapter_id)
#
#         else:
#             return Response({'user_type': user_type})

# ...
# class CreateUserQuiz(APIView):
#
#     def post(self, request, quiz_id):
#         user_type = request.user.user_type
#         if user_type == 'STUDENT':
#             quiz = get_object_or_404(Task, pk=quiz_id, task_type='QUIZ')
#             user_quiz_data = UserQuizData(user=request.user, quiz=quiz)
#             user_quiz_data.save()
#             user_questions = []
#             for qs in quiz.question_set.all().order_by('?')[:10]:
#                 user_questions.append(qs)
#                 if qs.format == 'MULTI':
#                     UserAnswer.objects.create(user_quiz_data=user_quiz_data, question=qs, max_score=2)
#                 else:
#                     UserAnswer.objects.create(user_quiz_data=user_quiz_data, question=qs)
#
#             user_quiz_data = UserQuizDataSerializer(user_quiz_data, data=request.data)
#             if user_quiz_data.is_valid():
#                 user_quiz_data.save(question=user_questions)
#                 return Response(user_quiz_data.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(user_quiz_data.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'user_type': user_type})
#
#
# # User Answer API
# class UserAnswerAPIView(APIView):
#
#     def post(self, request, pk, q_pk, a_pk):
#         user_quiz_data = get_object_or_404(UserQuizData, user=request.user, id=pk)
#         question = get_object_or_404(Question, id=q_pk)
#         answer = get_object_or_404(Answer, id=a_pk)
#         user_answer = get_object_or_404(UserAnswer, user_quiz_data=user_quiz_data, question=question)
#
#         if question.format == 'ONE':
#             if user_answer.answers.all().count() > 0:
#                 user_answer.answers.clear()
#                 user_answer.answers.add(answer)
#                 return Response({'status': 'Old user answer removed, new added!'})
#             else:
#                 user_answer.answers.add(answer)
#                 return Response({'status': 'Added user answer'})
#
#         elif question.format == 'MULTI':
#             if user_answer.answers.filter(id=answer.id).exists():
#                 user_answer.answers.remove(answer)
#                 return Response({'status': 'Old user answer removed!'})
#             else:
#                 user_answer.answers.add(answer)
#                 return Response({'status': 'User answer added!'})
#         else:
#             return Response({'status': 'Something error!'})
