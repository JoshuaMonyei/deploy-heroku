from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from .forms import AgentForm
from .models import Agent


def addagent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')
        else:
            return redirect('addagent')
    else:
        # If the request was not a POST, display the form to enter details.
        form = AgentForm()

        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).
    return render(request, 'agents/agentsform.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('login')
    else:
        return render(request, 'agents/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have logged out successfully')
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'agents/dashboard.html', context)