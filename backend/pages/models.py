import os
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .utils import LayoutUtils
from projects.models import Project

# ru = RoutingUtils(os.path.join(settings.FRONTEND_DIR, "pages"))
# routes = ru.get_nuxt_routes()
# ROUTE_CHOICES = [(r, r) for r in routes]
# PAGE_CHOICES = [
#     (r[1:] if r != "/" else "home", r[1:] if r != "/" else "home")
#     for r in routes  # if len(r.split("/")) <= 2
# ]
ROUTE_CHOICES = [("/", "/"), ]
PAGE_CHOICES = [("home",  "home"), ]
pu = LayoutUtils(os.path.join(settings.FRONTEND_DIR, "layouts"))
LAYOUT_CHOICES = [(sl, sl) for sl in pu.get_layouts()]
TARGET_CHOICES = [
    ("_blank", "blank"),
    ("_parent", "parent"),
    ("_self", "self"),
    ("_top", "top"),
]
PROJECT_SECTION_CHOICES = [
    ("state_of_art", "state of art"),
    ("context", "context"),
    ("design", "design")
]
DOC_TYPE_CHOICES = [
    ("statute", "state of art"),
    ("financial_balance", "financial balance"),
    ("social_balance", "social balance"),
    ("privacy_policy", "privacy policy"),
    ("cookies_policy", "cookies policy"),
    ("terms_of_use", "terms of use")
]
SOCIAL_CHOICES = [
    ("facebook", "facebook"),
    ("instagram", "instagram"),
    ("linkedin", "linkedin"),
    ("youtube", "youtube")
]


class Page(models.Model):
    order = models.PositiveSmallIntegerField(
        help_text=_("Page position in the navigation bar")
    )
    name = models.CharField(
        max_length=100, choices=PAGE_CHOICES,
        help_text=_("Page name.")
    )
    title = models.CharField(
        max_length=100,
        help_text=_("Page title (the one shown on navigation buttons).")
    )
    navigation = models.BooleanField(
        default=False,
        help_text=_("Is the page button into the navigation bar?")
    )
    layout = models.ForeignKey(
        to='Layout', on_delete=models.CASCADE, related_name='pages', null=True, blank=True,
        help_text="The layout to which the page belongs."
    )

    def __str__(self):
        return f"{self.order}_{self.name}"

    def clean_fields(self, exclude=None):
        if exclude is None:
            exclude = []
        errors = {}
        for f in self._meta.fields:
            if f.name in exclude:
                continue
            raw_value = getattr(self, f.attname)
            if f.blank and raw_value in f.empty_values:
                continue
            try:
                setattr(self, f.attname, f.clean(raw_value, self))
            except ValidationError as e:
                # For now we bypass validation on the "name" field
                if f.name.startswith("name"):
                    pass
                else:
                    errors[f.name] = e.error_list
        if errors:
            raise ValidationError(errors)

    class Meta:
        ordering = ["order"]


class Section(models.Model):
    page = models.ForeignKey(
        to=Page, on_delete=models.CASCADE, related_name='sections',
        help_text=_("The page to which the section belongs.")
    )
    order = models.PositiveSmallIntegerField(
        help_text=_("Position of the section into the page (descending order).")
    )
    title = models.CharField(
        max_length=150, null=True, blank=True,
        help_text=_("Section title.")
    )
    subtitle = models.CharField(
        max_length=500, null=True, blank=True,
        help_text=_("Section subtitle.")
    )

    def __str__(self):
        return f"{self.page.name}_section_{str(self.order)}"

    class Meta:
        ordering = ["order"]


class Text(models.Model):
    section = models.ForeignKey(
        to=Section, on_delete=models.CASCADE, related_name='texts', null=True, blank=True,
        help_text=_("The section to which the text belongs.")
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='texts', null=True, blank=True,
        help_text=_("The project to which the text belongs.")
    )
    project_section = models.CharField(
        max_length=100, choices=PROJECT_SECTION_CHOICES, null=True, blank=True,
        help_text=_("It defines to which part of the project the text belongs.")
    )
    order = models.PositiveSmallIntegerField(
        help_text=_("Position of the text into the section layout.")
    )
    title = models.CharField(
        max_length=150, null=True, blank=True,
        help_text=_("Text box title.")
    )
    subtitle = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Text box subtitle.")
    )
    content = models.TextField(
        max_length=1000, null=True, blank=True,
        help_text=_("The text content.")
    )

    def __str__(self):
        s = f"text_{str(self.order)}"
        if self.section:
            s = f"{s}_section_{self.section}"
        if self.project:
            s = f"{s}_{self.project}"
        if self.project_section:
            s = f"{s}_{self.project_section}"
        return s

    class Meta:
        ordering = ["order"]


class Image(models.Model):
    section = models.ForeignKey(
        to=Section, on_delete=models.CASCADE, related_name='images', null=True, blank=True,
        help_text=_("The section to which the image belongs.")
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='images', null=True, blank=True,
        help_text=_("The project to which the image belongs.<br>"
                    "NOTE: if the file name contains the word 'vertical' "
                    "it will take 4 cols in the gallery grid, 8 otherwise.")
    )
    project_section = models.CharField(
        max_length=100, choices=PROJECT_SECTION_CHOICES, null=True, blank=True,
        help_text=_("It defines to which part of the project the image belongs.")
    )
    order = models.PositiveSmallIntegerField(
        help_text=_("Position of the image into the section layout.")
    )
    content = models.ImageField(
        help_text=_("The image file.")
    )
    alt_content = models.ImageField(
        null=True, blank=True,
        help_text=_("The alternate image file.")
    )
    alt = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Alternate text for screen readers. Leave empty for decorative images.")
    )

    def __str__(self):
        s = f"image_{str(self.order)}"
        if self.section:
            s = f"{s}_{self.section}"
        if self.project:
            s = f"{s}_{self.project}"
        if self.project_section:
            s = f"{s}_{self.project_section}"
        return s

    class Meta:
        ordering = ["order"]


class Button(models.Model):
    section = models.ForeignKey(
        to=Section, on_delete=models.CASCADE, related_name='buttons', null=True, blank=True,
        help_text=_("The section to which the button belongs.")
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='buttons', null=True, blank=True,
        help_text=_("The project to which the button belongs.")
    )
    project_section = models.CharField(
        max_length=100, choices=PROJECT_SECTION_CHOICES, null=True, blank=True,
        help_text=_("It defines to which part of the project the button belongs.")
    )
    order = models.PositiveSmallIntegerField(
        help_text=_("Position of the button into the section layout.")
    )
    to = models.CharField(
        max_length=100, choices=ROUTE_CHOICES, default="/", null=True, blank=True,
        help_text=_("Denotes the target route of the link.")
    )
    href = models.CharField(
        max_length=750, null=True, blank=True,
        help_text=_("External link of the button.")
    )
    target = models.CharField(
        max_length=10, choices=TARGET_CHOICES, null=True, blank=True,
        help_text=_("Denotes the target of the href.")
    )
    text_0 = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Base text shown inside the button.")
    )
    text_1 = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Additional text shown inside the button.")
    )

    def __str__(self):
        s = f"button_{str(self.order)}"
        if self.section:
            s = f"{s}_section_{self.section}"
        if self.project:
            s = f"{s}_{self.project}"
        if self.project_section:
            s = f"{s}_{self.project_section}"
        return s

    def clean_fields(self, exclude=None):
        if exclude is None:
            exclude = []
        errors = {}
        for f in self._meta.fields:
            if f.name in exclude:
                continue
            raw_value = getattr(self, f.attname)
            if f.blank and raw_value in f.empty_values:
                continue
            try:
                setattr(self, f.attname, f.clean(raw_value, self))
            except ValidationError as e:
                # For now we bypass validation on the "to" field
                if f.name == "to":
                    pass
                else:
                    errors[f.name] = e.error_list
        if errors:
            raise ValidationError(errors)

    class Meta:
        ordering = ["order"]


class Video(models.Model):
    section = models.ForeignKey(
        to=Section, on_delete=models.CASCADE, related_name='videos', null=True, blank=True,
        help_text=_("The section to which the video belongs.")
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='videos', null=True, blank=True,
        help_text=_("The project to which the video belongs.")
    )
    project_section = models.CharField(
        max_length=100, choices=PROJECT_SECTION_CHOICES, null=True, blank=True,
        help_text=_("It defines to which part of the project the video belongs.")
    )
    order = models.PositiveSmallIntegerField(
        help_text=_("Position of the video into the section layout.")
    )
    content = models.FileField(
        help_text=_("The video file.")
    )
    poster = models.ImageField(
        null=True, blank=True,
        help_text=_("Specifies an image to be shown while the video is downloading, "
                    "or until the user hits the play button. "
                    "If this is not included, the first frame of the video will be used instead.")
    )

    def __str__(self):
        s = f"video_{str(self.order)}"
        if self.section:
            s = f"{s}_section_{self.section}"
        if self.project:
            s = f"{s}_{self.project}"
        if self.project_section:
            s = f"{s}_{self.project_section}"
        return s

    class Meta:
        ordering = ["order"]


class Document(models.Model):
    section = models.ForeignKey(
        to=Section, on_delete=models.CASCADE, related_name='documents', null=True, blank=True,
        help_text=_("The section to which the document belongs.")
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name='documents', null=True, blank=True,
        help_text=_("The project to which the document belongs.")
    )
    project_section = models.CharField(
        max_length=100, choices=PROJECT_SECTION_CHOICES, null=True, blank=True,
        help_text=_("It defines to which part of the project the document belongs.")
    )
    order = models.PositiveSmallIntegerField(
        help_text=_("Position of the document into the section layout.")
    )
    title = models.CharField(
        max_length=150, null=True, blank=True,
        help_text=_("Document title.")
    )
    subtitle = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Document subtitle.")
    )
    description = models.CharField(
        max_length=500, null=True, blank=True,
        help_text=_("Document description.")
    )
    file = models.FileField(
        help_text=_("The document file.")
    )
    type = models.CharField(
        max_length=100, choices=DOC_TYPE_CHOICES, null=True, blank=True,
        help_text=_("Document type.")
    )

    def __str__(self):
        s = f"document_{str(self.order)}"
        if self.type:
            s = f"{s}_type_{self.type}"
        if self.section:
            s = f"{s}_section_{self.section}"
        if self.project:
            s = f"{s}_{self.project}"
        if self.project_section:
            s = f"{s}_{self.project_section}"
        return s

    class Meta:
        ordering = ["order"]


class Footer(models.Model):
    corporate_full_name = models.CharField(
        max_length=150, null=True, blank=True,
        help_text=_("Company full name.")
    )
    corporate_short_name = models.CharField(
        max_length=20, null=True, blank=True,
        help_text=_("Company short name (acronym).")
    )
    footer_1_col_title = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Title of the first footer column.")
    )
    footer_2_col_title = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Title of the second footer column.")
    )
    footer_3_col_title = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Title of the third footer column.")
    )
    donation_title = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Title of the donation section of the third column.")
    )
    transparency_title = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Title of the transparency section.")
    )
    footer_1_col_text = models.TextField(
        max_length=500, null=True, blank=True,
        help_text=_("Text inside the first footer column.")
    )
    footer_2_col_text = models.TextField(
        max_length=500, null=True, blank=True,
        help_text=_("Text inside the second footer column.")
    )
    footer_3_col_text = models.TextField(
        max_length=500, null=True, blank=True,
        help_text=_("Text inside the third footer column.")
    )
    document_0 = models.ForeignKey(
        to=Document, on_delete=models.CASCADE, related_name='doc_0_footer', null=True, blank=True,
        help_text=_("First document exposed in the footer.")
    )
    document_1 = models.ForeignKey(
        to=Document, on_delete=models.CASCADE, related_name='doc_1_footer', null=True, blank=True,
        help_text=_("Second document exposed in the footer.")
    )
    subscribe_btn_text = models.CharField(
        max_length=50, null=True, blank=True,
        help_text=_("Text inside the newsletter subscribe button.")
    )
    email = models.EmailField(
        blank=True, null=True,
        help_text=_("Email address.")
    )
    fiscal_code = models.CharField(
        max_length=16, null=True, blank=True,
        help_text=_('Fiscal code')
    )
    registered_office = models.CharField(
        max_length=150, null=True, blank=True,
        help_text=_("Registered office address.")
    )

    def __str__(self):
        if self.corporate_short_name:
            return f"{self.corporate_short_name}_footer"
        return "footer"


class Social(models.Model):
    order = models.PositiveSmallIntegerField(
        help_text=_("Position of the social link.")
    )
    platform = models.CharField(
        max_length=100, choices=SOCIAL_CHOICES,
        help_text=_("Social network platform.")
    )
    link = models.CharField(
        max_length=250, null=True, blank=True,
        help_text=_("Link to the youtube page.")
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.platform


class Layout(models.Model):
    name = models.CharField(
        max_length=30, choices=LAYOUT_CHOICES,
        help_text=_("Layout name.")
    )
    logo = models.ForeignKey(
        to=Image, on_delete=models.CASCADE, related_name='logo_layouts', null=True, blank=True,
        help_text="Layout logo image."
    )
    donation_button = models.ForeignKey(
        to=Button, on_delete=models.CASCADE, related_name='donation_button_layouts', null=True, blank=True,
        help_text="Layout donation button."
    )
    contact_button = models.ForeignKey(
        to=Button, on_delete=models.CASCADE, related_name='contact_button_layouts', null=True, blank=True,
        help_text="Layout contact button."
    )
    footer = models.ForeignKey(
        to=Footer, on_delete=models.CASCADE, related_name='footer_layouts', null=True, blank=True,
        help_text="Layout footer."
    )

    def __str__(self):
        return self.name


class MetaTag(models.Model):
    hid = models.CharField(
        max_length=50,
        help_text=_("Tag unique identifier.")
    )
    name = models.CharField(
        max_length=50,
        help_text=_("Tag name.")
    )
    content = models.CharField(
        max_length=500,
        help_text=_("Tag content.")
    )
    layout = models.ForeignKey(
        to=Layout, on_delete=models.CASCADE, related_name='meta_tags', null=True, blank=True,
        help_text="The layout to which the tag will be attached."
    )
    page = models.ForeignKey(
        to=Page, on_delete=models.CASCADE, related_name='meta_tags', null=True, blank=True,
        help_text="The page to which the tag will be attached."
    )
    section = models.ForeignKey(
        to=Section, on_delete=models.CASCADE, related_name='meta_tags', null=True, blank=True,
        help_text="The section to which the tag will be attached."
    )
    text = models.ForeignKey(
        to=Text, on_delete=models.CASCADE, related_name='meta_tags', null=True, blank=True,
        help_text="The text to which the tag will be attached."
    )
    image = models.ForeignKey(
        to=Image, on_delete=models.CASCADE, related_name='meta_tags', null=True, blank=True,
        help_text="The image to which the tag will be attached."
    )
    video = models.ForeignKey(
        to=Video, on_delete=models.CASCADE, related_name='meta_tags', null=True, blank=True,
        help_text="The video to which the tag will be attached."
    )
    document = models.ForeignKey(
        to=Document, on_delete=models.CASCADE, related_name='meta_tags', null=True, blank=True,
        help_text="The document to which the tag will be attached."
    )

    def __str__(self):
        string = f"{self.hid}"
        if self.layout:
            string = f"{string}_layout_{self.layout}"
        if self.page:
            string = f"{string}_page_{self.page}"
        if self.section:
            string = f"{string}_section_{self.section}"
        if self.text:
            string = f"{string}_text_{self.text}"
        if self.image:
            string = f"{string}_image_{self.image}"
        if self.video:
            string = f"{string}_video_{self.video}"
        if self.document:
            string = f"{string}_document_{self.document}"
        return string


class CookiesSnackbar(models.Model):
    title = models.CharField(
        max_length=100,
        help_text=_("Snackbar title.")
    )
    info_text = models.TextField(
        max_length=1000,
        help_text=_("Snackbar info text.")
    )
    accept_button_label = models.CharField(
        max_length=50,
        help_text=_("Accept button label.")
    )
    cookies_preferences_link_label = models.CharField(
        max_length=100,
        help_text=_("Cookies preferences link label.")
    )

    def __str__(self):
        return f"{self.title}"


class CookiesPreferences(models.Model):
    title = models.CharField(
        max_length=100,
        help_text=_("Cookies preferences dialog title.")
    )
    info_text = models.TextField(
        max_length=1000,
        help_text=_("Cookies preferences dialog info text.")
    )
    save_button_label = models.CharField(
        max_length=50,
        help_text=_("Save preferences button label.")
    )
    reject_all_button_label = models.CharField(
        max_length=50,
        help_text=_("Reject all button label.")
    )
    accept_all_button_label = models.CharField(
        max_length=50,
        help_text=_("Accept all button label.")
    )

    def __str__(self):
        return f"{self.title}"
