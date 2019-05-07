from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, SettingsForm
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
from .models import FiiUser, Personalise


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
            aux = urlsafe_base64_encode(force_bytes(user.pk))
            if isinstance(aux, str):
                uid = aux
            else:
                uid = aux.decode('utf-8')
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


def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            #update data
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            email = form.data['email']
            rol = form.data['rol']
            navbar_color = form.data['navbar_color']
            background_color = form.data['background_color']
            accent_color = form.data['accent_color']
            font_color = form.data['font_color']
            font_family = form.data['font_family']

            if first_name != '':
                request.user.first_name = first_name
            if last_name != '':
                request.user.last_name = last_name
            if email != '':
                request.user.email = email
            if rol != '' and rol != request.user.rol:
                request.user.rol = rol
            if navbar_color != '' and navbar_color != request.user.personalise.navbar_color:
                request.user.personalise.navbar_color = navbar_color
            if background_color != '' and background_color != request.user.personalise.background_color:
                request.user.personalise.background_color = background_color
            if accent_color != '' and accent_color != request.user.personalise.accent_color:
                request.user.personalise.accent_color = accent_color
            if font_color != '' and font_color != request.user.personalise.font_color:
                request.user.personalise.font_color = font_color
            if font_family != '' and font_family != request.user.personalise.font_family:
                request.user.personalise.font_family = font_family
            request.user.personalise.save()
            request.user.save()
    else:
        form = SettingsForm()
    return render(request, 'settings.html', {'form': form})


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
        # init personalise
        p = Personalise()
        p.save()
        p.init_orar(user.an_studiu, user.grupa)
        user.personalise = p

        login(request, user)
        return redirect('landing_page.html')
    else:
        return render(request, 'activation_email_sent.html')


def activation_email_sent(request):
    return render(request, 'activation_email_sent.html')


def logout_view(request):
    logout(request)
    return render(request, 'landing_page2.html')
