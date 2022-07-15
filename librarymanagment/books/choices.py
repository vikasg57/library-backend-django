class UserTypeChoices:
    ADMIN = 0
    CUSTOMER = 1


USER_CHOICES = (
    (UserTypeChoices.ADMIN, 'ADMIN'),
    (UserTypeChoices.CUSTOMER, 'CUSTOMER')
)
