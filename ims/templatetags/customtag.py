from django import template
#from django.contrib.admin.templatetags.admin_list import result_list as admin_list_result_list
#from django.utils.safestring import mark_safe
#from .models import *
#register = template.Library()

# @register.simple_tag
# def build_campaign_select():
#     campaigns = Campaign.objects.all()
#     select_box = "<select name='campaign' id='campaign'>"
#     for campaign in campaigns:
#         select_box+= '<option value='+str(campaign.id)+'>'+campaign.name+'</option>'
#     select_box_final = select_box + '</select>'
#     return mark_safe(select_box_final)


register = template.Library()

@register.simple_tag
def current_time():
    l=["ram","vinay","Jitendra"]
    # select_box="<select name='inv'>"
    # for r in l:
    #     select_box +='<option>'+r+'</option>'
    # select_box_final= select_box+'</select>'   
    #return (select_box_final)
    return (l)