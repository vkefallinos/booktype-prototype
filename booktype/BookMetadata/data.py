
from .models import BookMetadata





def create_book_metadata(title, short_title, subtitle, publisher, publication_date, copyright_date, copyright_holder, publisher_city, short_description, long_description, ebook_isbn, print_isbn, ):
    new_bookmetadata = BookMetadata(
        title=title,
    
        short_title=short_title,
    
        subtitle=subtitle,
    
        publisher=publisher,
    
        publication_date=publication_date,
    
        copyright_date=copyright_date,
    
        copyright_holder=copyright_holder,
    
        publisher_city=publisher_city,
    
        short_description=short_description,
    
        long_description=long_description,
    
        ebook_isbn=ebook_isbn,
    
        print_isbn=print_isbn,
    
    )
    new_bookmetadata.save()
    return new_bookmetadata










def delete_book_metadata(bookmetadata_id):
    bookmetadata = BookMetadata.objects.get(id=bookmetadata_id)
    bookmetadata.delete()
    return {"ok": True}








def get_bookmetadata(bookmetadata_id):
    return BookMetadata.objects.get(id=bookmetadata_id)

def get_BookMetadatas():
    return BookMetadata.objects.all()
