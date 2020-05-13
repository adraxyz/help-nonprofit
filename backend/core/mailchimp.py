from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from django.conf import settings
from django.core.mail import send_mail


class MailChimpManager:

    def __init__(self):
        self.client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, mc_user=settings.MAILCHIMP_USERNAME)
        self.audience_lists = self.client.lists.all(get_all=True, fields="lists.id")

    def subscribe(self, email, first_name=None, last_name=None):
        status = HTTP_200_OK
        message = "Subscription success"
        if 'lists' in self.audience_lists and self.audience_lists['lists']:
            audience_list = self.audience_lists['lists']
            for audience in audience_list:
                audience_id = audience["id"]
                try:
                    self.client.lists.members.create(
                        audience_id,
                        {
                            'email_address': email,
                            'status': 'subscribed',
                            'merge_fields': {
                                'FNAME': first_name if first_name else "",
                                'LNAME': last_name if last_name else "",
                            }
                        }
                    )
                    send_mail(
                        "New newsletter subscription!",
                        f"Subscription details:\n\n"
                        f"Audience: {audience_id}\n"
                        f"Email: {email}\n"
                        f"First name: {first_name if first_name else 'not provided'}\n"
                        f"Last name: {last_name if last_name else 'not provided'}\n"
                        f"Status: subscribed",
                        email,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False
                    )
                except MailChimpError as mce:
                    status = mce.args[0]["status"]
                    message = mce.args[0]["title"]
                except:
                    pass
        else:
            status = HTTP_404_NOT_FOUND
            message = "Lists are not available."
        return status, message
