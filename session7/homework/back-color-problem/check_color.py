def is_inside(x,y,c):
    if x >= c[0] and y>=c[1]:
        if x<c[2]+c[0] and y<=c[3]+c[1]:
            return True
        else:
            return False         
    else:
        return False