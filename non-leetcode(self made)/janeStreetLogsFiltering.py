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

from typing import List, Tuple, Set
from collections import deque, defaultdict

def detect_multi_ip_logins(logs: List[Tuple[int, str, str]]) -> Set[str]:
    user_ips = defaultdict(set) 
    window = deque()  
    flagged = set()

    for stamp, user, ip in logs:
        while window and stamp - window[0][0] > 600:
            old_stamp, old_user, old_ip = window.popleft()
            if old_user not in flagged:
                user_ips[old_user].discard(old_ip)
                if not user_ips[old_user]:  # Clean up empty set
                    del user_ips[old_user]

        if user in flagged:
            continue

        # Suspicious if there's another IP already
        if ip not in user_ips[user] and user_ips[user]:
            flagged.add(user)
            del user_ips[user]  
        else:
            user_ips[user].add(ip)
            window.append((stamp, user, ip))

    return flagged
