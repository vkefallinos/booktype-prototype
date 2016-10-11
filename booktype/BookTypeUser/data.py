
from .models import BookTypeUser





def create_book_type_user(email, fullName, about, profile_image, public_email, twitter, facebook, linked_in, youtube, vimeo, hashed_password, preferred_Language, ):
    new_booktypeuser = BookTypeUser(
        email=email,
    
        fullName=fullName,
    
        about=about,
    
        profile_image=profile_image,
    
        public_email=public_email,
    
        twitter=twitter,
    
        facebook=facebook,
    
        linked_in=linked_in,
    
        youtube=youtube,
    
        vimeo=vimeo,
    
        hashed_password=hashed_password,
    
        preferred_Language=preferred_Language,
    
    )
    new_booktypeuser.save()
    return new_booktypeuser










def delete_book_type_user(booktypeuser_id):
    booktypeuser = BookTypeUser.objects.get(id=booktypeuser_id)
    booktypeuser.delete()
    return {"ok": True}








def get_booktypeuser(booktypeuser_id):
    return BookTypeUser.objects.get(id=booktypeuser_id)

def get_BookTypeUsers():
    return BookTypeUser.objects.all()
