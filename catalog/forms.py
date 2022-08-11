#表单相关
from django import forms

from django.core.exceptions import ValidationError
# 低版本django，高版本不支持
# from django.utils.translation import ugettext_lazy as _
import datetime 

# 续借
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="输入续借后的归还日期(限制在4周内，默认为3周).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #检查输入
        if data < datetime.date.today():
            raise ValidationError('无效日期 - 不能输入过去的日期')

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('无效日期 - 续借超出4周')

        return data

