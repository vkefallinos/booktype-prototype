
from .models import Book





def create_book(name, description, licence, language, right_to_left, public, image, status, created, published, ):
    new_book = Book(
        name=name,
    
        description=description,
    
        licence=licence,
    
        language=language,
    
        right_to_left=right_to_left,
    
        public=public,
    
        image=image,
    
        status=status,
    
        created=created,
    
        published=published,
    
    )
    new_book.save()
    return new_book










def delete_book(book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return {"ok": True}












def set_owner_to_book_type_user(book_id, booktypeuser_id):
    book = Book.objects.get(id=book_id)
    booktypeuser = BookTypeUser.objects.get(id=booktypeuser_id)
    book.owner = booktypeuser
    book.save()
    return {"ok": True}









def set_metadata_to_book_metadata(book_id, bookmetadata_id):
    book = Book.objects.get(id=book_id)
    bookmetadata = BookMetadata.objects.get(id=bookmetadata_id)
    book.metadata = bookmetadata
    book.save()
    return {"ok": True}







def add_role_to_roles(book_id, role_id):
    book = Book.objects.get(id=book_id)
    role = Role.objects.get(id=role_id)
    book.roles.add(role)
    return {"ok": True}










def remove_role_from_roles(book_id, role_id):
    book = Book.objects.get(id=book_id)
    role = Roleobjects.get(id=role_id)
    book.roles.remove(role)
    return {"ok": True}











def reorder_role_on_roles(book_id, role_id, place):
    book = Book.objects.get(id=book_id)
    role = Role.objects.get(id=role_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}






def add_chapter_to_chapters(book_id, chapter_id):
    book = Book.objects.get(id=book_id)
    chapter = Chapter.objects.get(id=chapter_id)
    book.chapters.add(chapter)
    return {"ok": True}










def remove_chapter_from_chapters(book_id, chapter_id):
    book = Book.objects.get(id=book_id)
    chapter = Chapterobjects.get(id=chapter_id)
    book.chapters.remove(chapter)
    return {"ok": True}











def reorder_chapter_on_chapters(book_id, chapter_id, place):
    book = Book.objects.get(id=book_id)
    chapter = Chapter.objects.get(id=chapter_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}






def add_section_to_sections(book_id, section_id):
    book = Book.objects.get(id=book_id)
    section = Section.objects.get(id=section_id)
    book.sections.add(section)
    return {"ok": True}










def remove_section_from_sections(book_id, section_id):
    book = Book.objects.get(id=book_id)
    section = Sectionobjects.get(id=section_id)
    book.sections.remove(section)
    return {"ok": True}











def reorder_section_on_sections(book_id, section_id, place):
    book = Book.objects.get(id=book_id)
    section = Section.objects.get(id=section_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}






def add_cover_to_covers(book_id, cover_id):
    book = Book.objects.get(id=book_id)
    cover = Cover.objects.get(id=cover_id)
    book.covers.add(cover)
    return {"ok": True}










def remove_cover_from_covers(book_id, cover_id):
    book = Book.objects.get(id=book_id)
    cover = Coverobjects.get(id=cover_id)
    book.covers.remove(cover)
    return {"ok": True}











def reorder_cover_on_covers(book_id, cover_id, place):
    book = Book.objects.get(id=book_id)
    cover = Cover.objects.get(id=cover_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}








def set_design_to_book_design(book_id, bookdesign_id):
    book = Book.objects.get(id=book_id)
    bookdesign = BookDesign.objects.get(id=bookdesign_id)
    book.design = bookdesign
    book.save()
    return {"ok": True}





def get_book(book_id):
    return Book.objects.get(id=book_id)

def get_Books():
    return Book.objects.all()
