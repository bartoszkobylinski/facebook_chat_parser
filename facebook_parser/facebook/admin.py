from django.contrib import admin
from facebook.models import (FacebookChat, Participant, FourCharWord, FiveCharWord,
                             SixCharWord, SevenCharWord, EighthCharWord, NineCharWord, 
                             TenAndMoreCharWord)


admin.site.register(FacebookChat)
admin.site.register(Participant)
admin.site.register(FourCharWord)
admin.site.register(FiveCharWord)
admin.site.register(SixCharWord)
admin.site.register(SevenCharWord)
admin.site.register(EighthCharWord)
admin.site.register(NineCharWord)
admin.site.register(TenAndMoreCharWord)
