from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from ..models import Message, Label
from django.conf import settings
from django.core.mail import send_mail
from .serializers import MessageSerializer, LabelSerializer
from ..mailchimp import MailChimpManager
from mailchimp3.mailchimpclient import MailChimpError
from smtplib import SMTPException
import logging

logger = logging.getLogger("api_logger")


class SubscribeView(APIView):

    def post(self, request, format=None):
        if 'email' in request.data and request.data['email']:
            email = request.data["email"]
            try:
                validate_email(email)
            except ValidationError:
                status = HTTP_400_BAD_REQUEST
                message = "Missing or invalid email address."
            else:
                first_name = request.data["first_name"] if "first_name" in request.data else None
                last_name = request.data["last_name"] if "last_name" in request.data else None
                logger.info(f"Trying to subscribe {email} with first_name {first_name} and last_name {last_name}.")
                try:
                    mcm = MailChimpManager()
                except MailChimpError as mce:
                    status = mce.args[0]["status"]
                    message = mce.args[0]["detail"]
                else:
                    status, message = mcm.subscribe(email, first_name, last_name)
        else:
            status = HTTP_400_BAD_REQUEST
            message = "Missing or invalid email address."
        msg, created = Message.objects.get_or_create(text=message)
        if created:
            msg.text_to_users = message
            msg.save()
            if status == HTTP_200_OK:
                logger.info(f"{email} subscribed with success.")
            else:
                logger.error(f"Failed to subscribe {email}: {status} - {message}")
        return Response({"status_code": status, "message": msg.text_to_users})


class ContactFormView(APIView):

    def get(self, request, format=None):
        form_messages = Message.objects.filter(topic="contact_form")
        serializer = MessageSerializer(form_messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        status = HTTP_200_OK
        message = "Contact success"
        mc_status = mc_message = ""
        if data and \
                "firstname" in data and data["firstname"] and \
                "email" in data and data["email"] and \
                "object" in data and data["object"] and \
                "message" in data and data["message"] and \
                "privacy_agreement" in data and data["privacy_agreement"]:
            try:
                email = data["email"]
                validate_email(email)
            except ValidationError:
                status = HTTP_400_BAD_REQUEST
                message = "Missing or invalid email address."
            else:
                try:
                    first_name = data["firstname"]
                    last_name = data["lastname"] if "lastname" in data and data["lastname"] else ""
                    logger.info(f"Trying to sending a message from {email} "
                                f"(first_name {first_name}, last_name {last_name}).")
                    send_mail(
                        data["object"],
                        f'{data["message"]}\n\n{first_name} {last_name}',
                        email,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False
                    )
                except SMTPException as e:
                    status = HTTP_500_INTERNAL_SERVER_ERROR
                    message = str(e)
                except Exception as e:
                    status = HTTP_500_INTERNAL_SERVER_ERROR
                    message = f"Some errors occurred when sending the message: {e}."
                if "news_agreement" in data and data["news_agreement"]:
                    try:
                        logger.info(f"Trying to subscribe {email} with first_name "
                                    f"{first_name} and last_name {last_name}.")
                        mcm = MailChimpManager()
                    except MailChimpError as mce:
                        status = mce.args[0]["status"]
                        message = mce.args[0]["detail"]
                    else:
                        mc_status, mc_message = mcm.subscribe(email, first_name, last_name)
        else:
            status = HTTP_400_BAD_REQUEST
            message = "Missing input data."
        msg, created = Message.objects.get_or_create(text=message)
        mc_msg, mc_created = Message.objects.get_or_create(text=mc_message)
        # logging
        if status == HTTP_200_OK:
            logger.info(f"The message from {email} has been successfully sent.")
        else:
            logger.error(f"Failed to send message from {email}: {status} - {message}")
        if mc_status == HTTP_200_OK:
            logger.info(f"{email} subscribed with success.")
        else:
            logger.error(f"Failed to subscribe {email}: {status} - {message}")
        return Response({
            "email": {"status_code": status, "message": msg.text_to_users},
            "news": {"status_code": mc_status, "message": mc_msg.text_to_users},
        })


class LabelViewSet(viewsets.ModelViewSet):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()
    lookup_field = 'item'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        """
        Filtering against a `topic` query parameter in the URL
        """
        queryset = self.queryset
        topic = self.request.query_params.get('topic', None)
        if topic is not None:
            queryset = self.queryset.filter(topic=topic.lower())
        return queryset
