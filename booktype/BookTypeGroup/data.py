
from .models import BookTypeGroup





def create_book_type_group(name, description, image, ):
    new_booktypegroup = BookTypeGroup(
        name=name,
    
        description=description,
    
        image=image,
    
    )
    new_booktypegroup.save()
    return new_booktypegroup










def delete_book_type_group(booktypegroup_id):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    booktypegroup.delete()
    return {"ok": True}












def set_owner_to_book_type_user(booktypegroup_id, booktypeuser_id):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    booktypeuser = BookTypeUser.objects.get(id=booktypeuser_id)
    booktypegroup.owner = booktypeuser
    booktypegroup.save()
    return {"ok": True}







def add_book_type_user_to_members(booktypegroup_id, booktypeuser_id):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    booktypeuser = BookTypeUser.objects.get(id=booktypeuser_id)
    booktypegroup.members.add(booktypeuser)
    return {"ok": True}










def remove_book_type_user_from_members(booktypegroup_id, booktypeuser_id):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    booktypeuser = BookTypeUserobjects.get(id=booktypeuser_id)
    booktypegroup.members.remove(booktypeuser)
    return {"ok": True}











def reorder_book_type_user_on_members(booktypegroup_id, booktypeuser_id, place):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    booktypeuser = BookTypeUser.objects.get(id=booktypeuser_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}






def add_book_to_books(booktypegroup_id, book_id):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    book = Book.objects.get(id=book_id)
    booktypegroup.books.add(book)
    return {"ok": True}










def remove_book_from_books(booktypegroup_id, book_id):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    book = Bookobjects.get(id=book_id)
    booktypegroup.books.remove(book)
    return {"ok": True}











def reorder_book_on_books(booktypegroup_id, book_id, place):
    booktypegroup = BookTypeGroup.objects.get(id=booktypegroup_id)
    book = Book.objects.get(id=book_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}




def get_booktypegroup(booktypegroup_id):
    return BookTypeGroup.objects.get(id=booktypegroup_id)

def get_BookTypeGroups():
    return BookTypeGroup.objects.all()
