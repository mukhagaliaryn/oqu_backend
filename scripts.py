from accounts.models import User, OldAccount
from main.models import CloneUser, CloneAccount


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


def transfer_account_data():
    for account in OldAccount.objects.all():
        CloneAccount.objects.create(
            pk=account.pk,
            user=CloneUser.objects.get(pk=account.user.pk),
            account_type=account.account_type,
            id_number=account.id_number,
            specialty=account.specialty,
            city=account.city,
            address=account.address,
            phone=account.phone,
            website=account.website,
            about=account.about,
            account_fill=account.account_fill,
        )
    print('Transfer CloneAccount data successfully')
