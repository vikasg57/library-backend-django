from .models import Book, Author, BookAuthorMapping


class BookHandler:

    def get_all_books_author_mapping(self):
        book_author_maps = BookAuthorMapping.objects.all()
        return [self.generate_book_author_mapping_response(book_author_map)
                for book_author_map in book_author_maps]

    def create_books_and_author_map(self, book_name, description, year, author_name):
        book = Book.objects.filter(book_name=book_name).first()
        author = Author.objects.filter(author_name=author_name).first()
        if not book:
            book = Book.objects.create(book_name=book_name,
                                       description=description,
                                       year=year)
        if not author:
            author = Author.objects.create(author_name=author_name)
        book_author_map = BookAuthorMapping.objects.create(book=book, author=author)
        return self.generate_book_author_mapping_response(book_author_map)

    def update_books_and_author_map(self, book_name, description, year, author_name, book_map_id):
        book_author_map = BookAuthorMapping.objects.filter(uuid=book_map_id).first()
        setattr(book_author_map.book, 'book_name', book_name)
        setattr(book_author_map.book, 'description', description)
        setattr(book_author_map.book, 'year', year)
        book_author_map.book.save()
        setattr(book_author_map.author, 'author_name', author_name)
        book_author_map.author.save()
        return self.generate_book_author_mapping_response(book_author_map)

    def delete_books_and_author_map(self, book_map_id):
        book_author_map = BookAuthorMapping.objects.filter(uuid=book_map_id).first()
        book_author_map.book.delete()
        book_author_map.author.delete()
        return {'message': "deleted sucessfully"}

    def generate_book_author_mapping_response(self, book_author_map):
        return{
            'book_name': book_author_map.book.book_name,
            'description': book_author_map.book.description,
            'year': book_author_map.book.year,
            'author_name': book_author_map.author.author_name,
            'uuid': str(book_author_map.uuid)
        }
