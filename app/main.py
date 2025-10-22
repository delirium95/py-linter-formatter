def format_linter_error(error: dict) -> dict:
    _dict = {**{new: error[old] for old, new in
        {
            "line_number": "line",
            "column_number": "column",
            "text": "message",
            "code": "name"
        }.items() if old in error},
        "source": "flake8"
    }
    return _dict


def format_single_linter_file(file_path: str, errors: list) -> dict:
    _dict = {"errors": [format_linter_error(e) for e in errors],
             "path": file_path,
             "status": "failed" if errors else "passed"
            }
    return _dict


def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(path, errors)
            for path, errors in linter_report.items()]
