import ulid
from typing import Optional

from django.db import models
from django.utils import timezone

from applibs.logger import get_logger

logger = get_logger(__name__)

class UrlShortenerManager(models.Manager):
    def create_short_url(
        self,
        url : str
    ) -> Optional["UrlShortener"]:
        try:
            new_object = self.create(
                url=url,
                created_at=timezone.now()
            )
            logger.info(f"New short url db object creation successful")
            return new_object
        except Exception as e:
            logger.error(f"Error creating new short url db object: {repr(e)}")
            return None

class UrlShortener(models.Model):
    id = models.CharField(max_length=26, primary_key=True, editable=False)
    url = models.CharField(max_length=2000)
    created_at = models.DateTimeField(null=True, blank=True)

    objects = UrlShortenerManager()

    def __str__(self) -> str:
        return f"URLShortener Object: {self.id}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(ulid.new())
        super.save(*args, **kwargs)

    class Meta:
        verbose_name = "URL Shortener"
        verbose_name_plural = "URL Shortener List"
        db_table = "url_shortener"