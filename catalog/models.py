from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date
import uuid # Required for unique book instances
# Create your models here.

# 书籍类别模型
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

# 书籍模型
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField('ISBN', max_length=13, null=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    imprint = models.CharField(max_length=200,null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    image = models.ImageField(upload_to='book',default='book/default.jpg')

    class Meta:
        ordering = ['title', 'imprint']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} {self.imprint}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    
    display_genre.short_description = 'Genre'


# 书籍模型（具体的某一本书）

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', '保存'),#Maintenance
        ('o', '借出'),#On loan
        ('a', '可借'),#Available
        ('r', '预约'),#Reserved
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned","Set book as returned"), ("renew_due_back", "renew return date"))

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.book.title} {self.book.imprint}'


    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


# 作者模型
class Author(models.Model):
    """Model representing an author."""
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    image = models.ImageField(upload_to='author',default='author/default.jpg')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the author',default="暂无简介")

    sex_list = (
        ('F','女'),
        ('M','男'),
        ('O','其他')
    )

    sex = models.CharField(
        max_length=1,
        choices=sex_list,
        blank=True,
        default='M',
        help_text='性别',
    )    
    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def get_sex(self):
        if self.sex=='F':
            return '女'
        elif self.sex=='M':
            return '男'
        else:
            return '其他'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

