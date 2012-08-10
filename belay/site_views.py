from django.views import generic

"""
Contains views that are not specific to any application, such as the
site index (home) page.
"""

class Index(generic.TemplateView):
    """
    The homepage of belayapp.com
    """
    template_name = "index.html"