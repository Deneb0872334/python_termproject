from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Quiz, Player

import random

# Create your views here.
@login_required
def home(request):
    # This is the currently working code for home, don't change, can display question already
    if request.method == 'POST':
        all_questions =  Quiz.objects.all()
        if len(all_questions) >= 5:
            random_questions = random.sample(list(all_questions), 5) # Randomly pick 5 questions
            return render(request, 'home.html', {'questions': random_questions})
        else:
            return render(request, 'error.html', {'error': 'Not enough questions'})
    elif request.method == 'GET':
        all_questions =  Quiz.objects.all()
        if len(all_questions) >= 5:
            random_questions = random.sample(list(all_questions), 5) # Randomly pick 5 questions
            return render(request, 'home.html', {'questions': random_questions})
        else:
            return render(request, 'error.html', {'error': 'Not enough questions'})
    else:
        return render(request, 'error.html', {'error': 'Method not allowed'})

def display_result(request): 
    if request.method == 'POST':
        iScore = 0
        arrResults = []
        for key, value in request.POST.items():
            if key.startswith('choice_'):
                iQuestionID = key.split('_')[1]
                objQuestion = Quiz.objects.get(id=iQuestionID)
                blnCorrect = (value == objQuestion.answer)
                arrResults.append((objQuestion.question, value, blnCorrect))
                if blnCorrect:
                    iScore += 1
        iPercentage = (iScore / 5) * 100
        strMessage = ""
        match iScore:
            case 0:
                strMessage = "Please try again!"
            case 1:
                strMessage = "Please try again!"
            case 2:
                strMessage = "Please try again!"
            case 3:
                strMessage = "Good job!"
            case 4:
                strMessage = "Excellent work!"
            case 5:
                strMessage = "You are a genius!"

        # If score is below 3, ask Player if want to play again
        if iScore < 3:
            blnPlayAgain = True
        else:
            blnPlayAgain = False
        
        # Save player name and score in DB Model
        objPlayer, created = Player.objects.get_or_create(username = request.user.username)
        objPlayer.first_name = request.user.first_name
        objPlayer.last_name = request.user.last_name
        objPlayer.score = iScore
        objPlayer.save()
        # Get all Players to be displayed
        arrPlayers = Player.objects.all().order_by('-score') # Order by descending score
        return render(request, 'result.html', {'results': arrResults, 'score': iScore, 'percentage': iPercentage, 'message': strMessage, 'players': arrPlayers, 'play_again': blnPlayAgain})
    else:
        # Optionally handle other methods, like PUT, DELETE if not applicable
        return render(request, 'error.html', {'error': 'Method not allowed'})

