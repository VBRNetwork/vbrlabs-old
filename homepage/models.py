from django.db import models
from colorfield.fields import ColorField
MEDIA_TYPE = (
    ('image', 'Image'),
    ('video', 'Video'),
)

class HomePageContent(models.Model):

    id = models.AutoField(primary_key=True)
    heading_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_subtitle = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_media_type = (
        models.CharField(max_length=255, choices=MEDIA_TYPE, unique=False, blank=True, null=False)
    )
    heading_image = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )
    heading_image_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_video_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_image_alt = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_image_caption = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_content = models.TextField(unique=False, blank=True, null=False)
    heading_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    heading_button_link_target_blank = models.BooleanField(default=False)
    second_heading_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    second_heading_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    second_heading_button_link_target_blank = models.BooleanField(default=False)
    first_section_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    first_section_subtitle = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    first_section_content = models.TextField(unique=False, blank=True, null=False)
    first_section_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    first_section_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    first_section_button_link_target_blank = models.BooleanField(default=False)
    second_section_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    second_section_subtitle = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    second_section_content = models.TextField(unique=False, blank=True, null=False)
    second_section_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    second_section_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    second_section_button_link_target_blank = models.BooleanField(default=False)
    third_section_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    third_section_subtitle = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    third_section_content = models.TextField(unique=False, blank=True, null=False)
    third_section_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    third_section_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    third_section_button_link_target_blank = models.BooleanField(default=False)
    fourth_section_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    fourth_section_subtitle = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    fourth_section_content = models.TextField(unique=False, blank=True, null=False)
    fourth_section_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    fourth_section_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    fourth_section_button_link_target_blank = models.BooleanField(default=False)

    def __str__(self):
        return self.heading_title

    class Meta:
        verbose_name = "Homepage Content"
        verbose_name_plural = "Homepage Content"

    
class Subscribers(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    discord_id = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
        


class Partners(models.Model):
    
    id = models.AutoField(primary_key=True)
    partner_name = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    partner_image = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )
    partner_image_alt = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    partner_image_caption = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    partner_image_width = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    partner_image_margin = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    partner_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    partner_link_target_blank = models.BooleanField(default=False)
    partner_order = models.IntegerField(unique=False, blank=True, null=False)

    def __str__(self):
        return f"{self.partner_name} | {self.partner_order}"

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
        ordering = ['partner_order']

class Technologies(models.Model):

    id = models.AutoField(primary_key=True)
    technology_name = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    technology_image = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )
    technology_image_alt = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    technology_image_caption = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    technology_image_width = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    technology_image_margin = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    technology_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    technology_link_target_blank = models.BooleanField(default=False)
    technology_order = models.IntegerField(unique=False, blank=True, null=False)

    def __str__(self):
        return f"{self.technology_name} | {self.technology_order}"

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ['technology_order']

class TeamMembers(models.Model):

    id = models.AutoField(primary_key=True)
    team_member_name = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_member_role = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_member_image = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )
    team_member_image_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_member_image_alt = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_member_image_caption = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_member_image_width = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_member_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_member_link_target_blank = models.BooleanField(default=False)
    team_member_order = models.IntegerField(unique=False, blank=True, null=False)
    team_member_web_projects_completed = (
        models.IntegerField(unique=False, blank=True, null=True)
    )
    team_member_mobile_projects_completed = (
        models.IntegerField(unique=False, blank=True, null=True)
    )
    team_member_blockchain_projects_completed = (
        models.IntegerField(unique=False, blank=True, null=True)
    )

    def __str__(self):
        return f"{self.team_member_name} | {self.team_member_order}"


    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['team_member_order']



class Team(models.Model):

    id = models.AutoField(primary_key=True)
    team_name = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    team_cover_image = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )
    team_members = models.ManyToManyField(TeamMembers, blank=True)

    projects = models.ManyToManyField("Projects", blank=True)



    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

class Services(models.Model):

    id = models.AutoField(primary_key=True)
    service_name = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    service_image = models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    service_image_alt = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    service_image_caption = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    service_icon_name = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    service_icon_color = ColorField(default='rgb(66, 102, 99)')
    service_content = models.TextField(unique=False, blank=True, null=False)
    service_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    service_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    service_button_link_target_blank = models.BooleanField(default=False)
    service_order = models.IntegerField(unique=False, blank=True, null=False)
    technologies = models.ManyToManyField(Technologies, blank=True)

    def __str__(self):
        return f"{self.service_name} | {self.service_order}"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['service_order']


class Projects(models.Model):

    id = models.AutoField(primary_key=True)
    project_name = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    project_image = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )
    project_image_alt = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    project_image_caption = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    project_image_width = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    project_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    project_link_target_blank = models.BooleanField(default=False)
    project_order = models.IntegerField(unique=False, blank=True, null=False)
    project_partners = models.ManyToManyField(Partners, blank=True)

    def __str__(self):
        return f"{self.project_name} | {self.project_order}"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['project_order']


class AboutUs(models.Model):

    id = models.AutoField(primary_key=True)
    about_us_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_subtitle = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_content = models.TextField(unique=False, blank=True, null=False)
    about_us_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_button_link_target_blank = models.BooleanField(default=False)
    about_us_order = models.IntegerField(unique=False, blank=True, null=False)
    about_us_roadmap_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_roadmap_content = models.TextField(unique=False, blank=True, null=False)
    about_us_roadmap_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_roadmap_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_roadmap_button_link_target_blank = models.BooleanField(default=False)
    about_us_roadmap_order = models.IntegerField(unique=False, blank=True, null=False)
    about_us_roadmap_image = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )
    about_us_roadmap_image_alt = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_roadmap_image_caption = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    about_us_roadmap_image_order = models.IntegerField(unique=False, blank=True, null=False)
    about_us_roadmap_icon = (
        models.ImageField(upload_to="homepage/images/", blank=True, null=False)
    )

    def __str__(self):
        return self.about_us_title

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"
        ordering = ['about_us_order']

class BlockchainContent(models.Model):
    id = models.AutoField(primary_key=True)
    blockchain_title = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    blockchain_subtitle = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    blockchain_content = models.TextField(unique=False, blank=True, null=False)
    blockchain_button_text = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    blockchain_button_link = (
        models.CharField(max_length=255, unique=False, blank=True, null=False)
    )
    blockchain_button_link_target_blank = models.BooleanField(default=False)
    blockchain_order = models.IntegerField(unique=False, blank=True, null=False)

    def __str__(self):
        return self.blockchain_title

    class Meta:
        verbose_name = "Blockchain Content"
        verbose_name_plural = "Blockchain Content"
        ordering = ['blockchain_order']