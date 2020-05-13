from django.db import models
from django.utils.translation import ugettext_lazy as _

TOPIC_CHOICES = [
    ("contact_form", _("Contact form"))
]
ITEM_CHOICES = [
    ("first_name", _("First name")),
    ("last_name", _("Last name")),
    ("email", _("email")),
    ("where_from", _("Where from")),
    ("age", _("Age")),
    ("object", _("Object")),
    ("message", _("Message")),
    ("news_agreement", _("Agreement to receive the newsletters")),
    ("privacy_agreement", _("Agreement to the privacy policy")),
    ("submit", _("Submit button")),
    ("clear", _("Clear form")),
]


class Message(models.Model):
    text = models.CharField(
        max_length=250, null=False, blank=False,
        help_text=_("Message text content.")
    )
    topic = models.CharField(
        max_length=50, null=True, blank=True, choices=TOPIC_CHOICES,
        help_text=_("The message field of application (topic).")
    )
    text_to_users = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Message text exposed to users.")
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.text_to_users:
            self.text_to_users = self.text
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        s = self.text
        if self.topic:
            s = f"{self.topic} - {s}"
        if self.text_to_users:
            s = f"{s} - {self.text_to_users}"
        return s


class Label(models.Model):
    topic = models.CharField(
        max_length=50, choices=TOPIC_CHOICES,
        help_text=_("The label field of application (topic).")
    )
    item = models.CharField(
        max_length=100, choices=ITEM_CHOICES,
        help_text=_("The item the label will apply to.")
    )
    label = models.CharField(
        max_length=150,
        help_text=_("The label which will be visible.")
    )

    def __str__(self):
        return f"{self.topic} {self.item} label"
