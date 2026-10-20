def read_rows(lines: list[str]) -> list[dict]:
    headers = None
    result = []
    for line in lines:
        cleaned_line = line.strip()
        
        if not cleaned_line:
            continue
        
        if headers is None:
            headers = [col.strip() for col in cleaned_line.split(',')]
        else:
            values = [value.strip() for value in cleaned_line.split(',')]
            if len(values) != len(headers):
                continue
            row_dict = dict(zip(headers, values))
            result.append(row_dict)
    return result

def count_types(rows: list[dict]) -> dict:
    result = {}
    for row in rows:
        result[row['тип']] = result.get(row['тип'], 0) + 1
    return result

def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row['тип'] == kind:
            try:
                minutes = float(row['минуты'].replace(',', '.'))
                total += minutes
            except ValueError:
                continue
    return round(total, 1)

def to_csv(counts: dict) -> str:
    result = 'тип,количество\n'
    for kind, count in sorted(counts.items()):
        result += f'{kind},{count}\n'
    return result


        






        




        


