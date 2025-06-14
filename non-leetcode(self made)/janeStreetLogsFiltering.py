#find suspicious logins from a list of logs, where users
#are flagged if they log in from different IP addresses within a 10-minute window.


#(timestamp: int, username: str, ip_address: str)
def identify_suspicious_logins(logs : list[tuple[int, str,str]]): #
    window = {} 
    sus_logins = Set()
    for log in logs:
        stamp, user, ip  = log
        if user in sus_logins:
            continue
        if user not in window:
            window[user] = [stamp, ip]
        else:
            old_stamp, old_ip = window[user]
            if old_ip != ip and stamp - old_stamp < 600:
                sus_logins.add(user)
            else:
                window[user] = [stamp, ip]
    
    return sus_logins
    

        
#if need to remember multiple IPs => Deque + Set for each user

