##rgb2float
# r=109
# g=114
# b=134;
# rgb = (r << 16 | g << 8 | b)

from struct import pack, unpack

def flaot2rgb(float_value):
    float_bytes = pack('f', float_value)
    int_value = unpack('L', float_bytes)[0]

    r = (int_value >> 16) & 0x0000ff
    g = (int_value >> 8) & 0x0000ff
    b = int_value & 0x0000ff
    rgb = [r,g,b]
    #print rgb
    return rgb

data_xyz = []
data_rgb_float = []
data_rgb_int = []
for line in open("rgb_float.txt"):
    xyz_float = line.split(" ")
    for i in range(len(xyz_float)):
        xyz_float[i] = float(xyz_float[i])
    xyz_int = xyz_float[0:3]
    rgb = flaot2rgb(xyz_float[3])
    for i in rgb:
        xyz_int.append(i)
    data_rgb_int.append(xyz_int)
f = open("rgb_int.txt",'w')
for i in data_rgb_int:
    f.write(str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(i[3])+" "+str(i[4])+" "+str(i[5])+"\n")
f.close