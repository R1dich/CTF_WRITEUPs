import idautils

start_address = 0x402000
array_size = 52

encoded_bytes = []
for i in range(array_size):
    byte = idaapi.get_byte(start_address + i)
    encoded_bytes.append(byte)

print("Encoded bytes:", [hex(b) for b in encoded_bytes])