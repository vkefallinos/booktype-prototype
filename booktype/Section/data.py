
from .models import Section





def create_section(title, ):
    new_section = Section(
        title=title,
    
    )
    new_section.save()
    return new_section










def delete_section(section_id):
    section = Section.objects.get(id=section_id)
    section.delete()
    return {"ok": True}










def add_chapter_to_chapters(section_id, chapter_id):
    section = Section.objects.get(id=section_id)
    chapter = Chapter.objects.get(id=chapter_id)
    section.chapters.add(chapter)
    return {"ok": True}










def remove_chapter_from_chapters(section_id, chapter_id):
    section = Section.objects.get(id=section_id)
    chapter = Chapterobjects.get(id=chapter_id)
    section.chapters.remove(chapter)
    return {"ok": True}











def reorder_chapter_on_chapters(section_id, chapter_id, place):
    section = Section.objects.get(id=section_id)
    chapter = Chapter.objects.get(id=chapter_id)
    #not implemented
    #find a way to store and change the order of a ManyToManyField
    return {"not": "implemented"}




def get_section(section_id):
    return Section.objects.get(id=section_id)

def get_Sections():
    return Section.objects.all()
