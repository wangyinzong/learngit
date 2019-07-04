
from django import template
from datetime import datetime
register = template.Library()

@register.filter
def time_since(value):
    # 小于1分钟显示刚刚
    # 小于1小时  x分钟以前
    # 小于24小时
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    timestamp = (now-value).total_seconds()
    if timestamp < 60:
        return "刚刚"
    elif timestamp >= 60 and timestamp < 60*60:
        minutes = int(timestamp/60)
        return "%s分钟以前" % minutes
    elif timestamp >= 60*60 and timestamp < 60 * 60*24:
        hours = int(timestamp / 60/60)
        return "%s小时以前" % hours
    elif timestamp >= 60*60*24 and timestamp < 60 * 60*24*30:
        day = int(timestamp / 60/60/24)
        return "%s天以前" % day
    else:
        return value.strftime("%Y/%M/%D /%H:%M")