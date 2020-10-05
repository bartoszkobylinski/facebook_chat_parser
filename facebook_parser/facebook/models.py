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


class Word(models.Model):
    """
    model for storing user words in facebook chat
    """
    word = models.TextField()
    count = models.PositiveIntegerField(default=0)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participant} uses {self.word} {self.count} times"
