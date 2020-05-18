from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.datetime import get_diff_in_seconds, get_datetime_now


class Session(
    models.Model
):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='session',
        on_delete=models.CASCADE,
        verbose_name=_("User"),
        primary_key=True
    )

    logged_at = models.DateTimeField(
        _("Logged at"),
        auto_now_add=True
    )

    logout_at = models.DateTimeField(
        _("Logout at"),
        default=None,
        null=True,
        blank=True
    )

    def logout(self):
        self.logout_at = get_datetime_now()
        self.save()

    @property
    def duration(self):
        if not self.logout_at:
            return -1

        seconds = get_diff_in_seconds(
            start_date=self.logged_at,
            end_date=self.logout_at
        )
        return seconds


class Counter(
    models.Model
):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='counters',
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )

    label = models.CharField(
        _('Counter label'),
        max_length=20
    )

    value = models.PositiveIntegerField(
        _("Counter value"),
        default=0
    )

    class Meta:
        unique_together = (('user', 'label'),)

    def increment(self):
        self.value += 1
        self.save()
