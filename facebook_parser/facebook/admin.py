from django.contrib import admin
from .models import FacebookChat, Participant, ParticipantReaction, Word


admin.site.register(FacebookChat)
admin.site.register(Participant)
admin.site.register(ParticipantReaction)
admin.site.register(Word)
