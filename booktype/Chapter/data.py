
from .models import Chapter





def create_chapter(title, content, status, ):
    new_chapter = Chapter(
        title=title,
    
        content=content,
    
        status=status,
    
    )
    new_chapter.save()
    return new_chapter










def delete_chapter(chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    chapter.delete()
    return {"ok": True}










def add_comment_to_comments(chapter_id, comment_id):
    chapter = Chapter.objects.get(id=chapter_id)
    comment = Comment.objects.get(id=comment_id)
    chapter.comments.add(comment)
    return {"ok": True}










def remove_comment_from_comments(chapter_id, comment_id):
    chapter = Chapter.objects.get(id=chapter_id)
    comment = Commentobjects.get(id=comment_id)
    chapter.comments.remove(comment)
    return {"ok": True}











def reorder_comment_on_comments(chapter_id, comment_id, place):
    chapter = Chapter.objects.get(id=chapter_id)
    comment = Comment.objects.get(id=comment_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}




def get_chapter(chapter_id):
    return Chapter.objects.get(id=chapter_id)

def get_Chapters():
    return Chapter.objects.all()
