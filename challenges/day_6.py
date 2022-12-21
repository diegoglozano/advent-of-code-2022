def find_marker(buffer, len_buffer):
    for i, _ in enumerate(buffer, start=1):
        if len(set(buffer[i:i+len_buffer])) == len_buffer:
            return buffer[i:i+len_buffer], i + len_buffer

BUFFER_LEN = 4
MESSAGE_LEN = 14

with open('data/day-6.csv') as f:
    buffer = f.read()

print(find_marker(buffer, BUFFER_LEN))
print(find_marker(buffer, MESSAGE_LEN))