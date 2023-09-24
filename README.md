# Django Blog Application

This is a Django-based Blog Application that allows you to create, publish, and manage blog posts. Users can read and comment on posts, and you can also share posts via email.

## Features

- User-friendly admin panel for managing posts and comments.
- Tagging system for categorizing posts.
- RSS feed for the latest blog posts.
- Text-based search functionality.
- Share posts via email.
- Comment on blog posts.
- Similar post recommendations based on tags.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the project dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python manage.py migrate

5. Create a superuser account to access the admin panel:
python manage.py createsuperuser

6. Start the development server:
python manage.py runserver

7. Access the admin panel at http://localhost:8000/admin/ and start creating posts.

## Usage
- To view the blog posts, visit http://localhost:8000/.
- You can filter posts by tags using URLs like http://localhost:8000/tag/<tag-slug>/.

## RSS Feed
- You can subscribe to the RSS feed to receive updates on new blog posts. Use the following URL:
- http://localhost:8000/feed/

## Text-Based Search
The application provides a text-based search feature. Use the search bar on the homepage to search for specific keywords in the blog posts.

## Sharing Posts via Email
You can share a post via email by clicking on the "Share via Email" button on a post's detail page. Fill in the required information, and the post will be shared with the recipient.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow the guidelines in CONTRIBUTING.md.

