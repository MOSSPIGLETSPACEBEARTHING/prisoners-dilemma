####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'TKN'
strategy_name = 'Liam Neeson'
strategy_description = '''\
Betray first round, make the move the opposing player made last round for the next
turn. Continue this for the next moves.'''

def move(my_history, their_history, my_score, their_score):
    
    if len(my_history)==0: # It's the first round: betray
        return 'b'
    else:
        # If there was a previous round just like the last one,
        # do whatever they did in the round that followed it
        
        # Reference last round
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
                    
        # Look at rounds before that one
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            # If one matches
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return their_history[round]
        # No match found
        if my_history[-1]=='c' and their_history[-1]=='b':
            return 'b' # Betray if they were severely punished last time
        else:
            return 'c' # Otherwise collude.