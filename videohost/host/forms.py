from django import forms
from s3direct.widgets import S3DirectWidget

class S3DirectUploadForm(forms.Form):
    videos = forms.URLField(widget=S3DirectWidget(
        dest='videodest',
        html=(
            '<div class="s3direct" data-policy-url="{policy_url}">'
            '  <a class="file-link" target="_blank" href="{file_url}">{file_name}</a>'
            '  <a class="file-remove" href="#remove">Remove</a>'
            '  <input class="file-url" type="hidden" value="{file_url}" id="{element_id}" name="{name}" />'
            '  <input class="file-dest" type="hidden" value="{dest}">'
            '  <input class="file-input" type="file" />'
            '  <div class="progress progress-striped active">'
            '    <div class="bar"></div>'
            '  </div>'
            '</div>'
        )))