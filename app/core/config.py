import os

class settings:
    def get_database_url():
        if os.getenv("ENVIRONMENT","local") == "test":
            return "sqlite:///./test.db"
        else:
            return "postgresql://postgres:421203@localhost:5432/ai_pairprogramming"