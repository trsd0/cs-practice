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


        


