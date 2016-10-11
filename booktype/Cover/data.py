
from .models import Cover











def approve(cover_id, approved):
    cover = Cover.objects.get(id=cover_id)
    cover.approved = approved
    cover.save()
    return {"ok": True}



def create_cover(title, creator, licence, notes, image, approved, ):
    new_cover = Cover(
        title=title,
    
        creator=creator,
    
        licence=licence,
    
        notes=notes,
    
        image=image,
    
        approved=approved,
    
    )
    new_cover.save()
    return new_cover










def delete_cover(cover_id):
    cover = Cover.objects.get(id=cover_id)
    cover.delete()
    return {"ok": True}








def get_cover(cover_id):
    return Cover.objects.get(id=cover_id)

def get_Covers():
    return Cover.objects.all()
