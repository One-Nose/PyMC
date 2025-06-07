from traceback import StackSummary


class DataPackCompilationError(Exception):
    def __init__(
        self,
        message: str = 'Data pack compilation error',
        stack_summary: StackSummary | None = None,
    ) -> None:
        summary = ''

        if stack_summary is not None:
            summary += (
                'The problem is likely in the following lines of code:\n'
                + ''.join(stack_summary.format()[:-1])
                + type(self).__name__
                + ': '
            )

        summary += message

        super().__init__(summary)


class FlatteningError(DataPackCompilationError):
    pass


class ContextCombineError(DataPackCompilationError):
    pass


class BadFunctionCall(DataPackCompilationError):
    pass


class ProviderStringifyError(DataPackCompilationError):
    pass
