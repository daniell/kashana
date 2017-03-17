from organizations.backends.defaults import InvitationBackend as BaseInvitationBackend


class InvitationBackend(BaseInvitationBackend):
    """
    A backend for inviting new users to join the site as members of an
    organization.
    """

    def invite_by_email(self, email, sender=None, request=None, **kwargs):
        """Creates an inactive user with the information we know and then sends
        an invitation email for that user to complete registration.
        """
        try:
            user = self.user_model.objects.get(business_email=email)
        except self.user_model.DoesNotExist:
            # TODO break out user creation process
            user = self.user_model.objects.create(business_email=email, password=self.user_model.objects.make_random_password())
            user.is_active = False
            user.save()
        self.send_invitation(user, sender, **kwargs)
        return user
