# from django.shortcuts import render, get_object_or_404,redirect, reverse
# from django.views import generic, View
# from django.views.generic.edit import CreateView
# from .forms import ProfileForm
# from .models import VolunteerProfile


# #volunteer home view
# class VolunteerPortfolio(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = VolunteerProfile.objects.all()
#         profile = get_object_or_404(queryset, slug=slug)

#         return render(
#             request,
#             "profile.html",
#             {
#                 "profile": profile
#             },
#         )




