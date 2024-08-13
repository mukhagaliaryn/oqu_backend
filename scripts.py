from accounts.models import User
from main.models import CloneUser


def transfer_data():
    for user in User.objects.all():
        CloneUser.objects.create(
            pk=user.pk,
            username='user-' + str(user.pk),
            email=user.email,
            full_name=user.full_name,
            image=user.image,
            birthday=user.birthday,
            is_staff=user.is_staff,
            is_superuser=user.is_staff,
            is_active=user.is_active,
            date_joined=user.date_joined
        )
    print('Transfer data successfully')


def transfer_data_password():
    for user in User.objects.all():
        clone_user = CloneUser.objects.get(id=user.id)
        clone_user.password = user.password
        clone_user.save()

    print('Transfer data password successfully')
