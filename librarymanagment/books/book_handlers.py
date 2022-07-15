from .models import Book, Author, BookAuthorMapping


class BookHandler:

    def get_all_books_author_mapping(self):
        books = Book.objects.all()
        return [self.generate_book_author_response(book)
                for book in books]

    def create_books_and_author_map(self, book_name, description, year, author_names):
        book = Book.objects.filter(book_name=book_name).first()
        if not book:
            book = Book.objects.create(book_name=book_name,
                                       description=description,
                                       year=year)
        for author_name in author_names:
            author = Author.objects.create(author_name=author_name.get('author'))
            BookAuthorMapping.objects.create(book=book, author=author)
        return self.generate_book_author_response(book)

    def update_books_and_author_map(self, book_name, description, year, book_id):
        book = Book.objects.filter(uuid=book_id).first()
        setattr(book, 'book_name', book_name)
        setattr(book, 'description', description)
        setattr(book, 'year', year)
        book.save()
        return self.generate_book_author_response(book)

    def delete_books_and_author_map(self, book_id):
        book = Book.objects.filter(uuid=book_id).first()
        print(book)
        book.delete()
        return {'message': "deleted successfully"}

    def generate_book_author_response(self, book):
        return{
            'book_name': book.book_name,
            'description': book.description,
            'year': book.year,
            'book_authors': self.get_book_author(book.uuid),
            'uuid': str(book.uuid)
        }

    def get_book_author(self, book_id):
        book_user_maps = BookAuthorMapping.objects.filter(book__uuid=book_id)
        return [{'author_name': book_user_map.author.author_name,
                 'uuid': str(book_user_map.author.uuid)}
                for book_user_map in book_user_maps]
