import os
import json
import time

# --- CONFIGURATION ---
BASE_DIR = "docs" # GitHub Pages usually serves from root or /docs. We'll use docs.
API_VERSION = "v1"
ROOT_PATH = os.path.join(BASE_DIR, API_VERSION)

# --- HELPER: ENVELOPE WRAPPER ---
def create_response(data, status=200):
    return {
        "meta": {
            "status": status,
            "requestId": f"req-static-{int(time.time())}",
            "serverTime": int(time.time() * 1000)
        },
        "data": data,
        "errors": []
    }

# --- DATA DEFINITIONS (HAPPY PATH) ---

# 2. Authentication (Mocked responses)
auth_login_data = {
    "accessToken": "eyJhGci_mock_access_token_header.payload.signature",
    "refreshToken": "ref_873_mock_refresh_token",
    "expiresInMs": 900000,
    "user": {
        "id": "u-001",
        "name": "Gatekeeper Admin",
        "avatarUrl": "https://ui-avatars.com/api/?name=Gatekeeper+Admin&background=0D8ABC&color=fff"
    }
}

auth_refresh_data = {
    "accessToken": "eyJhGci_new_mock_token...",
    "refreshToken": "ref_999_new_mock_refresh...",
    "expiresInMs": 900000
}

# 3. Home & News
home_feed_data = {
    "greeting": "Good Morning",
    "categories": [
        { "id": "cat-1", "label": "Finance", "iconKey": "finance" },
        { "id": "cat-2", "label": "HR", "iconKey": "users" },
        { "id": "cat-3", "label": "Tech", "iconKey": "cpu" }
    ],
    "featuredNews": [
        {
            "id": "news-101",
            "title": "Q3 Quarterly Results Exceed Expectations",
            "thumbnailUrl": "https://placehold.co/600x400/000000/FFF?text=Quarterly+Results",
            "contentUrl": "https://helix.dev/news/101",
            "publishedAt": "2023-10-27T10:00:00Z"
        }
    ],
    "latestNews": [
        {
            "id": "news-102",
            "title": "New Remote Work Policy",
            "excerpt": "Please review the updated guidelines for WFH arrangements effective next month.",
            "thumbnailUrl": "https://placehold.co/100x100/2ecc71/FFF?text=Policy",
            "publishedAt": "2023-10-26T09:00:00Z",
            "isBookmarked": False
        },
        {
            "id": "news-103",
            "title": "Server Maintenance Schedule",
            "excerpt": "Downtime expected this Sunday from 2 AM to 4 AM.",
            "thumbnailUrl": "https://placehold.co/100x100/e74c3c/FFF?text=Maint",
            "publishedAt": "2023-10-25T14:00:00Z",
            "isBookmarked": True
        }
    ]
}

news_detail_102 = {
    "id": "news-102",
    "title": "New Remote Work Policy",
    "content": "<h1>Remote Work Update</h1><p>We are shifting to a hybrid model. Employees are expected to be in the office 2 days a week.</p><ul><li>Tuesday</li><li>Thursday</li></ul>",
    "author": "HR Department",
    "readTimeMinutes": 5
}

# 4. Community
community_posts = {
    "items": [
        {
            "id": "post-555",
            "author": { "name": "John Doe", "avatarUrl": "https://ui-avatars.com/api/?name=John+Doe" },
            "content": "Just launched the new feature! Check it out on staging.",
            "createdAt": "2023-10-27T11:00:00Z",
            "likesCount": 42,
            "commentsCount": 5
        },
        {
            "id": "post-554",
            "author": { "name": "Sarah Smith", "avatarUrl": "https://ui-avatars.com/api/?name=Sarah+Smith" },
            "content": "Has anyone seen the updated API docs? They look clean.",
            "createdAt": "2023-10-27T09:30:00Z",
            "likesCount": 12,
            "commentsCount": 2
        }
    ],
    "nextPage": 2
}

chat_rooms = [
    {
        "id": "room-a1",
        "name": "General Engineering",
        "lastMessage": {
            "content": "Deploying now...",
            "senderName": "Alice",
            "timestamp": "2023-10-27T12:05:00Z"
        },
        "unreadCount": 3
    },
    {
        "id": "room-b2",
        "name": "Lunch Plans",
        "lastMessage": {
            "content": "Pizza looks good.",
            "senderName": "Bob",
            "timestamp": "2023-10-27T11:45:00Z"
        },
        "unreadCount": 0
    }
]

# 5. Notifications
notifications = {
    "items": [
        {
            "id": "notif-999",
            "title": "Salary Credited",
            "body": "Your October salary has been processed.",
            "type": "finance",
            "isRead": False,
            "createdAt": "2023-10-25T08:00:00Z"
        },
        {
            "id": "notif-998",
            "title": "New Comment",
            "body": "Alice commented on your post.",
            "type": "community",
            "isRead": True,
            "createdAt": "2023-10-24T15:20:00Z"
        }
    ]
}

qr_verify_response = {
    "isValid": True,
    "action": "check_in_success",
    "message": "Welcome to HQ, Gatekeeper Admin."
}

# 6. User Profile
user_profile = {
    "id": "u-001",
    "name": "Gatekeeper Admin",
    "email": "admin@helix.dev",
    "department": "Engineering",
    "avatarUrl": "https://ui-avatars.com/api/?name=Gatekeeper+Admin&background=0D8ABC&color=fff"
}


# --- MAPPING PATHS TO DATA ---
# Key: URL Path (relative to v1), Value: Data Object
endpoints = {
    # Auth (Mocked via GET for file access)
    "auth/login": auth_login_data,
    "auth/token/refresh": auth_refresh_data,
    "auth/logout": True, 
    
    # Home & News
    "feed/home": home_feed_data,
    "news/news-102": news_detail_102,
    
    # Community
    "community/posts": community_posts,
    "community/chat/rooms": chat_rooms,
    
    # Notifications
    "notifications": notifications,
    "notifications/device": {"status": "registered (mock)"}, # Mock POST response
    "qr/verify": qr_verify_response, # Mock POST response
    
    # User
    "users/me": user_profile
}

# --- GENERATOR LOGIC ---

def generate_api():
    print(f"🚀 Generating Helix Mobile API ({API_VERSION})...")
    
    if os.path.exists(BASE_DIR):
        import shutil
        shutil.rmtree(BASE_DIR)
    
    for path, data in endpoints.items():
        # Create full directory path
        full_dir = os.path.join(ROOT_PATH, path)
        os.makedirs(full_dir, exist_ok=True)
        
        # Wrap data in envelope
        response_payload = create_response(data)
        
        # Write index.json
        file_path = os.path.join(full_dir, "index.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(response_payload, f, indent=2)
            
        print(f"✅ Created: {file_path}")

    # Create a simple index.html at root to prevent 404 on base URL
    with open(os.path.join(BASE_DIR, "index.html"), "w") as f:
        f.write("<h1>Helix Mobile API is Live</h1><p>Endpoint: /v1/...</p>")

    print("\n🎉 Generation Complete. folder './docs' is ready for GitHub Pages.")

if __name__ == "__main__":
    generate_api()