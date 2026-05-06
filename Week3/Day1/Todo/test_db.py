import psycopg2

try:
    conn = psycopg2.connect(
        "postgresql://neondb_owner:npg_ht2DX3nKCYJH@ep-silent-wave-amaptmlk-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    # This alone string contains host, server, dbname, credentials, port
    )

    cur = conn.cursor()

    cur.execute("SELECT version();")
    print("Connected successfully!")
    print(cur.fetchone())

    conn.close()

except Exception as e:
    print("Error:", e)