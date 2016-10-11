
from .models import SubComment





def create_sub_comment(text, ):
    new_subcomment = SubComment(
        text=text,
    
    )
    new_subcomment.save()
    return new_subcomment










def delete_sub_comment(subcomment_id):
    subcomment = SubComment.objects.get(id=subcomment_id)
    subcomment.delete()
    return {"ok": True}












def set_user_to_book_type_user(subcomment_id, booktypeuser_id):
    subcomment = SubComment.objects.get(id=subcomment_id)
    booktypeuser = BookTypeUser.objects.get(id=booktypeuser_id)
    subcomment.user = booktypeuser
    subcomment.save()
    return {"ok": True}





def get_subcomment(subcomment_id):
    return SubComment.objects.get(id=subcomment_id)

def get_SubComments():
    return SubComment.objects.all()
