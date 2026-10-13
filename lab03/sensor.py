threshold = float(input())
n = int(input())

error_count = 0
exceed_count = 0
valid_count = 0
sum_temp = 0.0
max_temp = 0.0

for _ in range(n):
    record = input().strip()
    
    
    if record == "error":
        error_count += 1
    else:
        temp = float(record)
        
    
        valid_count += 1
        sum_temp += temp
        
        
        if temp > threshold:
            exceed_count += 1
            
    
        if valid_count == 1:
            max_temp = temp 
        elif temp > max_temp:
            max_temp = temp