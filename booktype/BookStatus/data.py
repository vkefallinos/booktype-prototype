
from .models import BookStatus





def create_book_status(status, ):
    new_bookstatus = BookStatus(
        status=status,
    
    )
    new_bookstatus.save()
    return new_bookstatus










def delete_book_status(bookstatus_id):
    bookstatus = BookStatus.objects.get(id=bookstatus_id)
    bookstatus.delete()
    return {"ok": True}








def get_bookstatus(bookstatus_id):
    return BookStatus.objects.get(id=bookstatus_id)

def get_BookStatuses():
    return BookStatus.objects.all()
