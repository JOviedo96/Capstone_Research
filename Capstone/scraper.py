import pandas as pd
from app_store_web_scraper import AppStoreEntry
from google_play_scraper import Sort, reviews_all

competitors = [
    {"name": "webmd", "apple_id": 295076329, "google_id": "com.webmd.android"},
    {"name": "mychart", "apple_id": 382952264, "google_id": "epic.mychart.android"},
    {"name": "ada", "apple_id": 1099986434, "google_id": "com.ada.app"},
    {"name": "mayoclinic", "apple_id": 523220194, "google_id": "com.mayoclinic.patient"},
    {"name": "goodrx", "apple_id": 485357017, "google_id": "com.goodrx"},
    {"name": "zocdoc", "apple_id": 391062219, "google_id": "com.zocdoc.android"},
    {"name": "applehealth", "apple_id": 1242545199, "google_id": None},
    {"name": "redfin", "apple_id": 327962480, "google_id": "com.redfin.android"},
    {"name": "creditkarma", "apple_id": 519817714, "google_id": "com.creditkarma.mobile"},
    {"name": "loseit", "apple_id": 297368629, "google_id": "com.fitnow.loseit"},
]

reviews_by_competitor = {}

for comp in competitors:
    print(f"Scraping reviews for {comp['name']}...")

    #Apple Reviews
    apple_reviews = []
    app = AppStoreEntry(comp["apple_id"], country="us")

    for review in app.reviews():
        if hasattr(review, 'content'):
            apple_reviews.append({
                "id": review.id,
                "rating": review.rating,
                "title": review.title,
                "content": review.content,
                "date": review.date,
                "source": "apple",
                "competitor": comp["name"]
            })
        else:
            print(f"Skipping a review for {comp['name']} due to missing 'content' attribute.")

    #Google Reviews
    google_reviews = []
    result = reviews_all(comp["google_id"], lang='en', country='us', sort=Sort.NEWEST)
    for r in result:
        google_reviews.append({
            "id": r.get("reviewId"),
            "rating": r.get("score"),
            "title": r.get("title", ""),
            "content": r.get("content"),
            "date": r.get("at"),
            "source": "google",
            "competitor": comp["name"]
        })

    all_reviews = apple_reviews + google_reviews
    reviews_by_competitor[comp["name"]] = pd.DataFrame(all_reviews)

df_all = pd.concat(reviews_by_competitor.values(), ignore_index=True)
df_all.to_csv("competitor_reviews.csv", index=False)

print("Scraping complete. Reviews saved to competitor_reviews.csv")