from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:Shiva2004@localhost:5432/ai_recommendation"

engine = create_engine(DB_URL)

def test_connection():
    try:
        conn = engine.connect()
        print("✅ Database connected successfully!")
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)


if __name__ == "__main__":
    test_connection()
