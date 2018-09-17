
class LoadResult:

    def __init__(self):
        self.rows_succeeded = 0
        self.failed_rows = []
        self.failed_rows_reasons = []

    def increment_success(self):
        self.rows_succeeded += 1

    def increment_failure(self, row_number, reason):
        self.failed_rows.append(row_number)
        self.failed_rows_reasons.append(reason)

    def succeeded(self):
        return len(self.failed_rows) == 0