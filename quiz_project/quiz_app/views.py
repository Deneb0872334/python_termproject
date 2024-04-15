from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Quiz

import random

# Create your views here.
@login_required
def home(request):
    all_questions =  Quiz.objects.all()

    random_questions = random.sample(list(all_questions), 5) # Randomly pick 5 questions
    print("Home: Step 1")
    if request.method == 'POST':
        print("Home: POST")
        selected_answers = {}
        for key, value in request.POST.items():
            print(f"Home: Step 2: {value}")
            if key.startswith('choice1'):
                print("Home: Step 3")
                question_id = key.replace('question','')
                selected_answers[question_id] = value
                print(f"Question: {question_id}, Answer: {value}")
            # 'selected_answers' dictionary contains question IDs and their selected answers
            # compare these with the correct answers in the database
    else:
        # handle GET request (initial page load) logic here
        pass
    return render(request, 'home.html', {'questions': random_questions})
