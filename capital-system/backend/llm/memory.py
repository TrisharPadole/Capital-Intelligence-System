SESSION_MEMORY = {}

def store_context(session_id, data):
    SESSION_MEMORY[session_id] = data

def get_context(session_id):
    return SESSION_MEMORY.get(session_id)
