



def stringify_bool(n,x):
	if n + x == 0:
		return "true"
	else:
		return "false"



def det2x2(det2_list):

    if len(det2_list) != 4:
        return None


    a,b,c,d = det2_list[0], det2_list[1], det2_list[2], det2_list[3]

    returnlist = [a,b,c,d]


    for i in returnlist:
        if i == str(i):
            return None


    else:
        g = ((a * b)-(c*d))
        return g





def det3x3(det3_list):
    a,b,c,d,e,f,g,h,i = det3_list[0], det3_list[1], det3_list[2], det3_list[3], det3_list[4], det3_list[5], det3_list[6], det3_list[7], det3_list[8]

    j = [a,b,c]
    k = [d,e,f]
    l = [g,h,i]
    m = (a * ((e * i)-(f * h))) - (b * ((d * i)-(f * g))) + (e * g)

    return m


#|A| = a(ei - fh) - b(di - fg) + c(dh - eg)

#3×6 − 8×4 = 18 − 32 = −14
