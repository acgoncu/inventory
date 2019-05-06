from django import forms

from .models import Post, Request

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

#request form 
class PurchaseRequestForm (forms.ModelForm):

    class Meta:
    	model = Request
    	fields = ('requester', 'request_date', 'branch', 'quantity', 'description', 'product_ID', 
'unit_price', 'reason', 'vendor', 'approver', 'approval_date', 'munis_GL_number', 'munis_PO_number', 
    'munis_PO_date', 'receive_date', 'receiver', 'order_status')