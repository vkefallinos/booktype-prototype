
from .models import Comment











def resolve(comment_id, resolved):
    comment = Comment.objects.get(id=comment_id)
    comment.resolved = resolved
    comment.save()
    return {"ok": True}



def create_comment(selected_text, resolved, ):
    new_comment = Comment(
        selected_text=selected_text,
    
        resolved=resolved,
    
    )
    new_comment.save()
    return new_comment










def delete_comment(comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return {"ok": True}












def set_user_to_book_type_user(comment_id, booktypeuser_id):
    comment = Comment.objects.get(id=comment_id)
    booktypeuser = BookTypeUser.objects.get(id=booktypeuser_id)
    comment.user = booktypeuser
    comment.save()
    return {"ok": True}







def add_sub_comment_to_subcomments(comment_id, subcomment_id):
    comment = Comment.objects.get(id=comment_id)
    subcomment = SubComment.objects.get(id=subcomment_id)
    comment.subcomments.add(subcomment)
    return {"ok": True}










def remove_sub_comment_from_subcomments(comment_id, subcomment_id):
    comment = Comment.objects.get(id=comment_id)
    subcomment = SubCommentobjects.get(id=subcomment_id)
    comment.subcomments.remove(subcomment)
    return {"ok": True}











def reorder_sub_comment_on_subcomments(comment_id, subcomment_id, place):
    comment = Comment.objects.get(id=comment_id)
    subcomment = SubComment.objects.get(id=subcomment_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}




def get_comment(comment_id):
    return Comment.objects.get(id=comment_id)

def get_Comments():
    return Comment.objects.all()
