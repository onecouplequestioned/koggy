
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
    a,b,c,d,e,f,g,h,i = det3_list

    j = [a,b,c]
    k = [d,e,f]
    l = [g,h,i]
    m = (a * ((e * i)-(f * h))) - (b * ((d * i)-(f * g))) + (e * g)

    return m
