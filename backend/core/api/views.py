from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from ..models import Message, Label, CookiesCategory
from shop.models import Shipment
from django.conf import settings
from django.core.mail import send_mail
from .serializers import MessageSerializer, LabelSerializer, CookiesCategorySerializer
from ..mailchimp import MailChimpManager
from mailchimp3.mailchimpclient import MailChimpError
from smtplib import SMTPException
from datetime import datetime, timezone
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


class UserDataForm(APIView):

    topic = ""

    def get(self, request, format=None):
        form_messages = Message.objects.filter(topic=self.topic)
        serializer = MessageSerializer(form_messages, many=True)
        return Response(serializer.data)


class ContactFormView(UserDataForm):

    topic = "contact_form"

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
                        f'{data["message"]}\n\n{first_name} {last_name}\n\n{email}',
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
            logger.error(f"Failed to subscribe {email}: {mc_status} - {message}")
        return Response({
            "email": {"status_code": status, "message": msg.text_to_users},
            "news": {"status_code": mc_status, "message": mc_msg.text_to_users},
        })


class ShipmentFormView(UserDataForm):

    topic = "shipment_form"

    def post(self, request, format=None):
        data = request.data
        status = HTTP_200_OK
        message = "Success"
        mc_status = mc_message = ""
        if data and \
                "first_name" in data and data["first_name"] and \
                "last_name" in data and data["last_name"] and \
                "email" in data and data["email"] and \
                "address" in data and data["address"] and \
                "address_number" in data and data["address_number"] and \
                "country" in data and data["country"] and \
                "city" in data and data["city"] and \
                "province" in data and data["province"] and \
                "cap" in data and data["cap"] and \
                "phone" in data and data["phone"] and \
                "cart" in data and data["cart"] and \
                "privacy_agreement" in data and data["privacy_agreement"]:
            try:
                email = data["email"]
                validate_email(email)
            except ValidationError:
                status = HTTP_400_BAD_REQUEST
                message = "Missing or invalid email address."
            else:
                try:
                    first_name = data["first_name"]
                    last_name = data["last_name"]
                    address = data["address"]
                    address_number = data["address_number"]
                    country = data["country"]
                    city = data["city"]
                    province = data["province"]
                    cap = data["cap"]
                    phone = data["phone"]
                    products = "\n".join([str(p) for p in data["cart"]["products"]])
                    total_price = data["cart"]["total"]
                    timestamp = datetime.utcnow().replace(tzinfo=timezone.utc)
                    Shipment.objects.create(
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        address=address,
                        address_number=address_number,
                        country=country,
                        city=city,
                        province=province,
                        cap=cap,
                        phone=phone,
                        products=products,
                        total_price=total_price,
                        timestamp=timestamp,
                        state="sent"
                    )
                    mail_text = f"Shipment request by {first_name} {last_name} on {timestamp}.\n\n" \
                                f"Email: {email}\n" \
                                f"Country: {country}\n" \
                                f"Province: {province}\n" \
                                f"City: {city}\n" \
                                f"Address: {address} {address_number}\n" \
                                f"CAP: {cap}\n" \
                                f"Phone: {phone}\n\n" \
                                f"Products: \n{products}\n\n" \
                                f"Minimum donation: {total_price}€."
                    logger.info(f"Sending email to notify shipment request on {timestamp} by {email}")
                    send_mail(
                        subject=f"Shipment request by {email} on {timestamp}",
                        message=mail_text,
                        from_email=email,
                        recipient_list=[settings.EMAIL_HOST_USER],
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
            logger.error(f"Failed to subscribe {email}: {mc_status} - {message}")
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


class CookiesCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CookiesCategorySerializer
    queryset = CookiesCategory.objects.all()
    lookup_field = 'name'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
