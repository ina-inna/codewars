def hex_string_to_RGB(hex_string): 
    rgbdict = {
        'r': 0,
        'g': 0,
        'b': 0,
    }

    if hex_string.startswith("#"):
        hex_string = hex_string[1:]
        
    def turn_to_rgb (a):
        result = int(a[0], 16) * 16
        result2 = int(a[1], 16)
        final_result = result + result2
        return final_result
            
    r_rgb = turn_to_rgb(hex_string[0:2])
    rgbdict['r'] = r_rgb
    
    g_rgb = turn_to_rgb(hex_string[2:4])
    rgbdict['g'] = g_rgb
    
    b_rgb = turn_to_rgb(hex_string[4:6])
    rgbdict['b'] = b_rgb
    
    return rgbdict
