from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from .models import FiiUser


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(email=user.email, password=raw_password)
            # login(request, user)

            current_site = get_current_site(request)
            subject = 'Activeaza contul FII-Student'
            uid = urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8')
            token = account_activation_token.make_token(user)
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            })
            user.email_user(subject, message)

            return redirect('/users/activation_email_sent/')
    else:
        form = SignupForm()
    return render(request, 'signup2.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = FiiUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, FiiUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('')
    else:
        return render(request, 'activation_email_sent.html')


def activation_email_sent(request):
    return render(request, 'activation_email_sent.html')


def logout_view(request):
    logout(request)
    return render(request, 'landing_page.html')
