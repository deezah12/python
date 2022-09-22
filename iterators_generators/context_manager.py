import contextlib


@contextlib.contextmanager
def manage_context():
    print("Entering the context manager")
    yield 1
    print("Exiting the context manager")


with manage_context() as one:
    print(one)


# class ContextManger():
#     def __enter__(self):
#         print("entering the context")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
