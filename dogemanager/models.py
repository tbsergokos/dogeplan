from django.db import models as m
from uuid import uuid4 as u4
from django.contrib.auth.models import User as U
from tinymce.models import HTMLField as hf
# A projec
STAT = (('3', 'At Risk'), ('-2', 'On Hold'), ('-1', 'Off Track'),
        ('1', 'On Track'), ('2', 'Complete'),)
PRIV = (('0', 'Public'),  ('1', 'Private'),)
PRIOR = (('0', 'Low'),  ('1', 'Medium'), ('2', 'High'),)
class ParentGoal(m.Model):
  uid = m.UUIDField(u4)
  title = m.CharField(max_length=999)
  priority=m.CharField(max_length=999,choices=PRIOR)
  priority=m.CharField(max_length=999,choices=STAT)
  description= hf()
  due_date= m.DateField(blank=True)
  sub_goal=m.ManyToManyField(SubGoal)
  team=m.ManyToManyField(Team)
  metric=m.ManyToManyField(GoalMetric)
  portfolio=m.ManyToManyField(Portfolio)
  project=m.ManyToManyField(Project)
  creator=m.ForeignKey(U,on_delete=m.CASCADE)
  collaborator=m.ManyToManyField(U)
  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']
class SubGoal(m.Model):
  uid = m.UUIDField(u4)
  title = m.CharField(max_length=999)
  description= hf()
  due_date= m.DateField(blank=True)
  sub_goal=m.ManyToManyField(SubGoal)
  team=m.ManyToManyField(Team)
  metric=m.ManyToManyField(GoalMetric)
  creator=m.ForeignKey(U,on_delete=m.CASCADE)
  parent_goal=m.ForeignKey(ParentGoal,on_delete=m.CASCADE)
  collaborator=m.ManyToManyField(U)
  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']
class Team(m.Model):
  uid = m.UUIDField(u4)
  title = m.CharField(max_length=999)
  description= hf()
  member=m.ManyToManyField(U)
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']
class Task(m.Model):
  uid = m.UUIDField(u4)
  title = m.CharField(max_length=999)
  status=m.CharField(max_length=999,choices=S)
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['title']
class Section(m.Model):
  uid = m.UUIDField(u4)
  title = m.CharField(max_length=999)
  #section=m.ForeignKey()
  task=m.ManyToManyField(Task)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']
# Track a group of projects
class Portfolio(m.Model):
  uid = m.UUIDField(u4)
  title = m.CharField(max_length=999)
#  section=m.ForeignKey()
  #task=m.ManyToManyField(task)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']

class Project(m.Model):
  uid=m.UUIDField(u4)
  title=m.CharField(max_length=999)
  goal=m.ManyToManyField(goal)
  slug=m.SlugField(max_length=999)
  status=m.CharField(max_length=999,choices=S)
 # section=m.ManyToManyField(section)
#  portfolio=m.ManyToManyField(portfolio)
  member=m.ManyToManyField(U)
  created_on=m.DateTimeField(auto_now_add=True)
  updated_on=m.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title
  class Meta:
    ordering=['title']
