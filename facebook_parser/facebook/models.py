from django.db import models


class FacebookChat(models.Model):
    """
    model for FacebookChat file uploaded by user
    """
    chat_title = models.CharField(max_length=150)
    participants_number = models.PositiveIntegerField(default=0)
    gifs_number = models.PositiveIntegerField(default=0)
    messages_number = models.PositiveIntegerField(default=0)
    photos_number = models.PositiveIntegerField(default=0)
    characters_number = models.PositiveIntegerField(default=0)
    reactions_number = models.PositiveIntegerField(default=0)
    links_number = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.chat_title} Facebook chat"


class Participant(models.Model):
    """
    model for Participant of FacebookChat
    """
    name = models.CharField(max_length=150)
    facebook_chat = models.ForeignKey(FacebookChat, on_delete=models.CASCADE)
    messages_number = models.PositiveIntegerField(default=0)
    words_number = models.PositiveIntegerField(default=0)
    characters_number = models.PositiveIntegerField(default=0)
    photos_number = models.PositiveIntegerField(default=0)
    links_number = models.PositiveIntegerField(default=0)
    gifs_number = models.PositiveIntegerField(default=0)
    most_common_reaction = models.CharField(max_length=150)
    counter_most_common_react = models.PositiveIntegerField(default=0)
    total_numbers_of_reactions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"""{self.name} is a participant of facebook chat with title
                {self.facebook_chat}"""

class FourCharWord(models.Model):
    """
    model for word in chat which has four character
    """
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    word = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.participant} used {self.count} times {self.word}"

class FiveCharWord(models.Model):
    """
    model for word in chat which has five character
    """
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    word = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.participant} used {self.count} times {self.word}"

class SixCharWord(models.Model):
    """
    model for word in chat which has six character
    """
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    word = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.participant} used {self.count} times {self.word}"

class SevenCharWord(models.Model):
    """
    model for word in chat which has seven character
    """
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    word = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.participant} used {self.count} times {self.word}"

class EightCharWord(models.Model):
    """
    model for word in chat which has eight character
    """
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    word = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.participant} used {self.count} times {self.word}"

class NineCharWord(models.Model):
    """
    model for word in chat which has nine character
    """
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    word = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.participant} used {self.count} times {self.word}"

class TenAndMoreCharWord(models.Model):
    """
    model for word in chat which has ten and more character 
    """
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    word = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.participant} used {self.count} times {self.word}"
