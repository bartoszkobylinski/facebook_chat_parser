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
    characters_number = models.PositiveIntegerField(default=0)
    photos_number = models.PositiveIntegerField(default=0)
    links_number = models.PositiveIntegerField(default=0)
    gifs_number = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"""{self.name} is a participant of facebook chat with title
                {self.facebook_chat}"""


class ParticipantReaction(models.Model):
    """
    model for counting and storing various reaction of user in facebook chat
    """
    reaction = models.CharField(max_length=150)
    counts = models.PositiveIntegerField(default=0)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)


class Sentence(models.Model):
    """
    model for staring user sentence in facebook chat
    """
    sentence = models.TextField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)


class Word(models.Model):
    """
    model for storing user words in facebook chat
    """
    word = models.TextField()
    count = models.PositiveIntegerField(default=0)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
