entries = []


def add_entry(content, date):
    entries.append(
        {
            "content": content,
            "date": date,
        }
    )


def get_entries():
    return entries
