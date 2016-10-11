
from .models import Role





def create_role(name, description, ):
    new_role = Role(
        name=name,
    
        description=description,
    
    )
    new_role.save()
    return new_role










def delete_role(role_id):
    role = Role.objects.get(id=role_id)
    role.delete()
    return {"ok": True}








def get_role(role_id):
    return Role.objects.get(id=role_id)

def get_Roles():
    return Role.objects.all()
