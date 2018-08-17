from django.shortcuts import render_to_response, render, redirect
from django.urls import reverse

from companyManagment.forms import (
    RegistrationForm,
    EditProfileForm,
    EditExtraFieldsForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import UserProfile, Invitation
from django.contrib.auth.decorators import login_required


def register(request):
    """
    Custom user registration view automatically logs user in 
    after creating user profile
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('view_profile')
        else:
            return render(request, 'accounts/reg_form.html', {'form': form})
    else:
        if request.user.is_authenticated:
            return redirect('view_profile')
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


@login_required
def view_profile(request, pk=None):
    """
    This view provides basic and custom user 
    info from userprofile model
    """
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


@login_required
def recievied_invitations(request):
    """
    This view display current pending invitations sent 
    by company admin to join there company and also accept and reject
    pending invitations.
    """
    pk = request.GET.get('pk')
    result = request.GET.get('result')
    invitationid = request.GET.get('invitation')
    if pk:
        if "accepted" in result:
            current_user = request.user
            get_admin = User.objects.get(pk=pk)
            admin_company = get_admin.userprofile.company
            current_user_profile = UserProfile.objects.get(
                user_id=current_user.id)
            current_user_profile.company = admin_company
            current_user_profile.save()
            current_user_invitations = Invitation.objects.get(pk=invitationid)
            current_user_invitations.status = result
            current_user_invitations.save()
            return redirect('recievied_invitations')
        elif "rejected" in result:
            user = request.user
            current_user_invitations = Invitation.objects.get(pk=invitationid)
            current_user_invitations.status = result
            current_user_invitations.save()
    else:
        user = request.user

    notification = Invitation.objects.filter(user=request.user)
    args = {'user': user, 'invite': notification}
    return render(request, 'accounts/invitations.html', args)


@login_required
def invite_status(request, pk=None):
    """
    This view helps company admin to view status of there 
    sent to users to join there company
    """
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
        if not user.userprofile.admin:
            return redirect('login')
    invited = Invitation.objects.filter(invitedby=request.user)
    args = {'user': user, 'invited': invited}
    return render(request, 'accounts/invite_status.html', args)


@login_required
def invite_employee(request, pk=None):
    """
    This view list out users without the company
    and helps company admins in inviting them
    """
    if pk:
        user = User.objects.get(pk=pk)
        current_user = request.user
        company = current_user.userprofile.company
        text = "Invited you to join " + str(company)
        send = Invitation(user=user, invitedby=current_user,
                          text=text, status="pending")
        send.save()
        return redirect('invite_employee')
    else:
        user = request.user
        if not user.userprofile.admin:
            return redirect('login')

    if user.userprofile.admin:
        all_entries = User.objects.exclude(invitation__invitedby=user.id)
    args = {'all': all_entries}
    return render(request, 'accounts/invite.html', args)


@login_required
def myemployee(request):
    """
    This view shows company admins in removing
    current employees from the company
    """
    pk = request.GET.get('remove')
    if pk:
        user = UserProfile.objects.get(user_id=pk)
        user.company = None
        user.save()
        return redirect('myemployee')
    else:
        user = request.user
        if not user.userprofile.admin:
            return redirect('login')

    if user.userprofile.admin:
        all_entries = User.objects.filter(
            userprofile__company=user.userprofile.company, userprofile__admin=False)
    args = {'all': all_entries}
    return render(request, 'accounts/employee_in_company.html', args)


@login_required
def edit_profile(request):
    """
    This view helps users in editing there basic info
    """
    if request.method == 'POST':
        user = request.user
        userprofile = UserProfile.objects.get(user_id=user.id)
        form1 = EditProfileForm(
            request.POST, instance=request.user, prefix='some_prefix')
        form2 = EditExtraFieldsForm(
            request.POST, instance=userprofile, prefix='another_prefix')
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect(reverse('view_profile'))
    else:
        user = request.user
        userprofile = UserProfile.objects.get(user_id=user.id)
        form1 = EditProfileForm(instance=request.user, prefix='some_prefix')
        form2 = EditExtraFieldsForm(
            instance=userprofile, prefix='another_prefix')
        args = {'form1': form1, 'form2': form2}
        return render(request, 'accounts/edit_profile.html', args)
