from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    job_number = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Report(models.Model):
    project = models.ForeignKey(Project)
    date = models.DateField(auto_now_add=True)
    previous_day = models.TextField()
    today = models.TextField()
    blockers = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.project.id.__str__() + " : " + self.date.__str__()
