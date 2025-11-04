### DELETE Operation
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all().values()
# Expected output:
# <QuerySet []>
```
