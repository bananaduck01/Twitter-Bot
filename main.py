import config
import google.generativeai as genai
import time

# EDITABLE PROMPT
PROMPT = "Write an inspiring tweet about @shellyelpro, specifically mentioning that user. No user directions, no hashtags, include emojis. THE RESPONSE MUST BE EXACTLY 250 CHARACTERS. NO EXCEPTIONS."

def main():
    try:
        # Configure Gemini
        genai.configure(api_key=config.gemini_api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")

        print(f"Generating tweet with prompt: '{PROMPT}'...")
        
        response = model.generate_content(PROMPT)
        tweet_text = response.text.strip()

        # Ensure tweet is within length (basic check)
        if len(tweet_text) > 280:
             tweet_text = tweet_text[:277] + "..."

        print(f"Drafted Tweet: {tweet_text}")
        
        print("Posting to Twitter...")
        response = config.client.create_tweet(text=tweet_text)
        print(f"Tweeted successfully! ID: {response.data['id']}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
