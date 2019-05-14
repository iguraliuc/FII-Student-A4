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


@login_required(login_url='/')
def settings(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = SettingsForm(request.POST)
        if form.is_valid():
            #update data
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            an_studiu = form.data['an_studiu']
            email = form.data['email']
            rol = form.data['rol']
            grupa = form.data['grupa']
            navbar_color = form.data['navbar_color']
            background_first = form.data['background_first']
            background_second = form.data['background_second']
            color1_first = form.data['color1_first']
            color1_second = form.data['color1_second']
            color2_first = form.data['color2_first']
            color2_second = form.data['color2_second']
            font_color = form.data['font_color']
            font_family = form.data['font_family']

            if first_name != '' and first_name != request.user.first_name:
                request.user.first_name = first_name
            if last_name != '' and last_name != request.user.last_name:
                request.user.last_name = last_name
            if an_studiu != '' and an_studiu != request.user.an_studiu:
                request.user.an_studiu = an_studiu
            if email != '' and email != request.user.email:
                request.user.email = email
            if rol != '' and rol != request.user.rol:
                request.user.rol = rol
            if grupa != '' and grupa != request.user.grupa:
                request.user.grupa = grupa
            if navbar_color != '' and navbar_color != request.user.personalise.navbar_color:
                request.user.personalise.navbar_color = navbar_color
            if background_first != '' and background_first != request.user.personalise.background_first:
                request.user.personalise.background_first = background_first
            if background_second != '' and background_second != request.user.personalise.background_second:
                request.user.personalise.background_second = background_second
            if font_color != '' and font_color != request.user.personalise.font_color:
                request.user.personalise.font_color = font_color
            if font_family != '' and font_family != request.user.personalise.font_family:
                request.user.personalise.font_family = font_family

            if color1_first != '' and color1_first != request.user.personalise.color1_first:
                request.user.personalise.color1_first = color1_first
            if color1_second != '' and color1_second != request.user.personalise.color1_second:
                request.user.personalise.color1_second = color1_second
            if color2_first != '' and color2_first != request.user.personalise.color2_first:
                request.user.personalise.color2_first = color2_first
            if color2_second != '' and color2_second != request.user.personalise.color2_second:
                request.user.personalise.color2_second = color2_second
            request.user.personalise.save()
            request.user.save()
    else:
        if not request.user.is_authenticated:
            pass  # TODO: should add redirect to error page here
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
        user.save()
        login(request, user)
        return redirect('landing_page.html')
    else:
        return render(request, 'activation_email_sent.html')


def activation_email_sent(request):
    return render(request, 'activation_email_sent.html')


def logout_view(request):
    logout(request)
    return render(request, 'prezentare_en.html')
