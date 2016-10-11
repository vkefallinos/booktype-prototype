
from .models import BookDesign





def create_book_design(theme, heading, color, font_size, alignment, paragraph, text_indent, line_height, ):
    new_bookdesign = BookDesign(
        theme=theme,
    
        heading=heading,
    
        color=color,
    
        font_size=font_size,
    
        alignment=alignment,
    
        paragraph=paragraph,
    
        text_indent=text_indent,
    
        line_height=line_height,
    
    )
    new_bookdesign.save()
    return new_bookdesign










def delete_book_design(bookdesign_id):
    bookdesign = BookDesign.objects.get(id=bookdesign_id)
    bookdesign.delete()
    return {"ok": True}








def get_bookdesign(bookdesign_id):
    return BookDesign.objects.get(id=bookdesign_id)

def get_BookDesigns():
    return BookDesign.objects.all()
