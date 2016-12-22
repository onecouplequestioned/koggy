
def stringify_bool(n,x):
	if n + x == 0:
		return "true"
	else:
		return "false"



def det2x2(det2_list):

    if len(det2_list) != 4:
        return None

    a,b,c,d = det2_list
    returnlist = [a,b,c,d]

    for i in returnlist:
        if type(i) == str:
            return None
    g = ((a * b)-(c*d))
    return g



def det3x3(det3_list):

    if len(det3_list) != 9:
        return None

    a,b,c,d,e,f,g,h,i = det3_list
    returnlist = [a,b,c,d]

    for i in returnlist:
        if type(i) == str:
            return None

    m = (a * ((e * i)-(f * h))) - (b * ((d * i)-(f * g))) + (e * g)
    return m
