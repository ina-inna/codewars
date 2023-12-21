def bouncing_ball(h, bounce, window):
    ball_height = h * bounce
    count = 1
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while ball_height > window:
            count += 2
            ball_height = ball_height * bounce
        return count
    else:  
        return -1