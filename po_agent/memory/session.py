class InMemorySessionService:
    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id: str):
        self.sessions[session_id] = {"history": [], "context": {}}

    def update_context(self, session_id: str, key: str, value: any):
        if session_id in self.sessions:
            self.sessions[session_id]["context"][key] = value

    def get_context(self, session_id: str) -> dict:
        return self.sessions.get(session_id, {}).get("context", {})

    def add_history(self, session_id: str, entry: str):
        if session_id in self.sessions:
            self.sessions[session_id]["history"].append(entry)
