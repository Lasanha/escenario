from django import template
from django.conf import settings

register = template.Library()
GA_CODE = settings.GA_CODE

@register.simple_tag
def ganalytics():
    if GA_CODE:
        return """
            <script>
              (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                   m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                     })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
                ga('create', '""" + GA_CODE + """', 'auto');
                ga('send', 'pageview');
            </script>
            """
    return ''
