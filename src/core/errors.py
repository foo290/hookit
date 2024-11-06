class ExceptionBase(Exception):

    def __init__(self, msg, *args, **kwargs):
        super().__init__(msg, *args)


class ImmutableObjectError(ExceptionBase):
    ...




