# Generated by Django 1.11.13 on 2018-06-26 16:51


import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("survey", "0007_auto_20180217_1515")]

    operations = [
        migrations.AlterModelOptions(
            name="response",
            options={"verbose_name": "Set of answers to surveys", "verbose_name_plural": "Sets of answers to surveys"},
        ),
        migrations.AlterField(
            model_name="answer", name="body", field=models.TextField(blank=True, null=True, verbose_name="Content")
        ),
        migrations.AlterField(
            model_name="answer",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="survey.Question",
                verbose_name="Question",
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="response",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="survey.Response",
                verbose_name="Response",
            ),
        ),
        migrations.AlterField(
            model_name="answer", name="updated", field=models.DateTimeField(auto_now=True, verbose_name="Update date")
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="category", name="name", field=models.CharField(max_length=400, verbose_name="Name")
        ),
        migrations.AlterField(
            model_name="category",
            name="order",
            field=models.IntegerField(blank=True, null=True, verbose_name="Display order"),
        ),
        migrations.AlterField(
            model_name="category",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="survey.Survey",
                verbose_name="Survey",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="survey.Category",
                verbose_name="Category",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="choices",
            field=models.TextField(
                blank=True,
                help_text="""The choices field is only used if the question type
if the question type is 'radio', 'select', or
'select multiple' provide a comma-separated list of
options for this question.""",
                null=True,
                verbose_name="Choices",
            ),
        ),
        migrations.AlterField(model_name="question", name="order", field=models.IntegerField(verbose_name="Order")),
        migrations.AlterField(
            model_name="question", name="required", field=models.BooleanField(verbose_name="Required")
        ),
        migrations.AlterField(
            model_name="question",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="survey.Survey",
                verbose_name="Survey",
            ),
        ),
        migrations.AlterField(model_name="question", name="text", field=models.TextField(verbose_name="Text")),
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "text (multiple line)"),
                    ("short-text", "short text (one line)"),
                    ("radio", "radio"),
                    ("select", "select"),
                    ("select-multiple", "Select Multiple"),
                    ("select_image", "Select Image"),
                    ("integer", "integer"),
                ],
                default="text",
                max_length=200,
                verbose_name="Type",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="response",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="responses",
                to="survey.Survey",
                verbose_name="Survey",
            ),
        ),
        migrations.AlterField(
            model_name="response", name="updated", field=models.DateTimeField(auto_now=True, verbose_name="Update date")
        ),
        migrations.AlterField(
            model_name="response",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="survey", name="description", field=models.TextField(verbose_name="Description")
        ),
        migrations.AlterField(
            model_name="survey",
            name="display_by_question",
            field=models.BooleanField(verbose_name="Display by question"),
        ),
        migrations.AlterField(
            model_name="survey",
            name="is_published",
            field=models.BooleanField(verbose_name="Users can see it and answer it"),
        ),
        migrations.AlterField(
            model_name="survey", name="name", field=models.CharField(max_length=400, verbose_name="Name")
        ),
        migrations.AlterField(
            model_name="survey",
            name="need_logged_user",
            field=models.BooleanField(verbose_name="Only authenticated users can see it and answer it"),
        ),
        migrations.AlterField(
            model_name="survey",
            name="template",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Template"),
        ),
    ]
