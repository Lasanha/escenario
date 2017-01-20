from django import template
from django.conf import settings

register = template.Library()
GA_CODE = settings.GA_CODE
GADSENSE_CLIENT = settings.GADSENSE_CLIENT
GADSENSE_SLOT = settings.GADSENSE_SLOT


@register.simple_tag
def ganalytics():
    if GA_CODE:
        return """
<script>
(function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
(i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
}})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', '{0}', 'auto');
ga('send', 'pageview');
</script>
            """.format(GA_CODE)
    return ''


@register.simple_tag
def gadsense():
    if GADSENSE_CLIENT and GADSENSE_SLOT:
        return """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
 style="display:inline-block;width:300px;height:600px"
 data-ad-client="{0}"
 data-ad-slot="{1}"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({{}});
</script>
            """.format(GADSENSE_CLIENT, GADSENSE_SLOT)
    return ''
