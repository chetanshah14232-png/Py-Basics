import sqlite3
from datetime import datetime

# 1. Database Connection
db = sqlite3.connect('my_growth_tracker.db')
cursor = db.cursor()

# 2. Table Creation (Added UNIQUE to date to prevent duplicates)
cursor.execute('''
  CREATE TABLE IF NOT EXISTS daily_logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT UNIQUE, 
    pushups INTEGER,
    protein_intake TEXT,
    finance_learning TEXT
  )
''')

# 3. Data Entry
today_date = datetime.now().strftime("%d-%m-%Y")
pushups = 15
protein = "Banana & Chickpeace"
finance = "Learned about Freelancing on Upwork"

# 'INSERT OR REPLACE' use karne se ek date ki do entries nahi hongi
cursor.execute('''
  INSERT OR REPLACE INTO daily_logs(date, pushups, protein_intake, finance_learning)
  VALUES(?,?,?,?)
''', (today_date, pushups, protein, finance))

db.commit()
print("✅ Data Successfully synced to your transformation log!")

# 4. View Progress Function
def view_progress():
    date_to_search = input("\nWhich date's data do you wanna see? (DD-MM-YYYY): ")
    
    # Connection reuse kar rahe hain jo upar open hai
    cursor.execute("SELECT * FROM daily_logs WHERE date = ?", (date_to_search,))
    result = cursor.fetchone()

    if result:
        print("\n" + "🚀" + "=" *25)
        print(f"Date             : {result[1]}")
        print(f"Push-ups         : {result[2]}")
        print(f"Diet             : {result[3]}")
        print(f"Finance Learning : {result[4]}")
        print("=" *26)
    else:
        print(f"\n⚠️ Sorry, no records found for {date_to_search}")

# Function Call
view_progress()

#update entry
def update_entry():
    search_date = input("\nWhich date's data do you wanna update? (DD-MM-YYYY) : ")
    new_pushups = int(input("Write correct push-ups counts : "))

    conn = sqlite3.connect('my_growth_tracker.db')
    cursor = conn.cursor()

    #update query
    cursor.execute('''
        UPDATE daily_logs
        SET pushups = ?
        WHERE date = ?
''',(new_pushups,search_date))

    conn.commit()
    print(f"The data for date {search_date} has been updated")

    conn.close()

# Sab kaam khatam hone ke baad connection band karein
db.close()
