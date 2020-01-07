from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from .serializer import QuestionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from vsite import LHKit

@api_view(['GET','POST'])
def apiAllquestionoldzz(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    ha = LHKit.LHStand.LHResult()
    ha['data'] = serializer.data

    return Response(ha)

@api_view(['GET','POST'])
def apiAllquestionold2(request, format=None):
    questions = Question.objects.all().order_by('-pub_date')
    itCount = len(questions)
    page = int ( request.POST.get('page',1 ) )
    rows = int ( request.POST.get('rows', 5  ) )
   
    standRt = LHKit.LHStand.LHResult()
    if (page-1)*rows > itCount :
        standRt ['data'] = []
    else :
        lastPageNumber = rows
        if  ((page * rows) >= itCount ) :
            lastPageNumber = itCount - ((page - 1) * rows)
        ser = QuestionSerializer(instance=questions[(page-1)*rows: (page-1)*rows + lastPageNumber] , many=True)
        standRt['data'] = ser.data
    resp =  Response(standRt)
    return resp

@api_view(['GET','POST'])
def apiPostTest(request):
    rt = LHKit.LHStand.LHResult()
    #name1 = request.GET.get('para', "无数据" )
    name1 = request.POST.get('para', "无数据" )
    rt['data'] = name1
    return Response(rt)

class apiAllquestionnew(generics.ListAPIView):
    queryset =  Question.objects.all()  # Product.objects.all()
    serializer_class = QuestionSerializer


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})




class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def test (request):
    return render(request, 'polls/test.html')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))