from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice,Question

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([p.question_text for p in latest_question_list])
#    return HttpResponse(output)
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = RequestContext(request, {
#        'latest_question_list': latest_question_list,
#    })
#    return HttpResponse(template.render(context))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# Create your views here.

def detail(request, question_id):
    try:
	question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
	raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
#    return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
