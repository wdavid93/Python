from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, logout, authenticate
# from forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm
User = get_user_model()

# Vue pour gérer l'inscription
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username = username, password = password)
        # user = form.save()  # Enregistrer le nouvel utilisateur
        login(request, user)  # Connecter l'utilisateur
        return redirect('index')  # Rediriger vers la page d'accueil après l'inscription
    return render(request, 'accounts/signup.html')


def logout_user(request):
    logout(request)
    return redirect('index')  # Rediriger vers la page d'accueil après l'inscription


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authentifier l'utilisateur
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Connecter l'utilisateur
            return redirect('index')  # Rediriger vers la page d'accueil après connexion
        else:
            # Afficher un message d'erreur
            return render(request, 'accounts/login.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    
    return render(request, 'accounts/login.html')


# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # Enregistrer le nouvel utilisateur
#             login(request, user)  # Connecter l'utilisateur
#             return redirect('index')  # Rediriger vers la page d'accueil après l'inscription
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})
