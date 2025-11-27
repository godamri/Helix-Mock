Helix Mobile API - Static Host

This repository contains a generated Static API for the Helix Mobile application.

⚠️ Important Limitations

Since this is hosted on GitHub Pages (Static Hosting):

Read-Only: Real POST, PUT, DELETE requests will return 405 Method Not Allowed.

Mocking Write Ops: "Write" endpoints (like /auth/login or /community/posts creation) are implemented as static JSON files. You must perform a GET request to retrieve the "Happy Path" success response during development.

URL Structure: GitHub Pages works best with directories.

Contract: GET /v1/feed/home

Actual URL: https://<user>.github.io/<repo>/v1/feed/home/index.json
(Note: Some clients handle trailing slashes automatically, but explicitly adding /index.json is the safest way to fetch the file).

How to Deploy

1. Generate the Data

Run the included Python script to build the docs folder.

python mock_api_generator.py


2. Push to GitHub

Create a new repository on GitHub.

Push this code (including the generated docs folder).

git init
git add .
git commit -m "Initial API deploy"
git branch -M main
git remote add origin [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
git push -u origin main


3. Enable GitHub Pages

Go to your repository Settings > Pages.

Under Build and deployment > Source, select Deploy from a branch.

Under Branch, select main and the folder /docs (this is why the script outputs to docs).

Click Save.

4. Test It

Your API Base URL will be:
https://<your-username>.github.io/<your-repo-name>/v1

Example:
https://<your-username>.github.io/<your-repo-name>/v1/feed/home/index.json