# LinkedIn Job Scraper API

A Flask-based REST API that scrapes job listings from multiple job sites including LinkedIn, Indeed, Google Jobs, and more.

## Supported Job Sites
- LinkedIn
- Indeed
- Google Jobs
- Glassdoor
- Bayt
- BDJobs
- Naukri

## API Endpoints

### Health Check
```
GET /
```
Returns a status check to verify the API is running.

### Scrape Jobs
```
GET /scrape-jobs
```

#### Query Parameters
- `site_name` (string): Comma-separated list of job sites (default: linkedin)
- `search_term` (string): Job title or keywords (default: software engineer)
- `location` (string): Job location (default: San Francisco, CA)
- `results_wanted` (int): Number of results to return (default: 20)
- `hours_old` (int): Maximum age of job postings in hours (default: 72)
- `country` (string): Country code for Indeed search (default: USA)
- `fetch_description` (boolean): Whether to fetch full job descriptions (default: true)
- `google_search_term` (string): Custom search term for Google Jobs

## Setup and Installation

1. Clone the repository
2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
1. Run the application:
```bash
python app.py
```

## Example Usage
```
GET /scrape-jobs?site_name=linkedin,indeed&search_term=python developer&location=New York
```

## Error Handling
The API returns appropriate error messages for invalid parameters with a 400 status code.

## Notes
- Rate limiting may apply based on job site policies
- Some sites may require authentication
- Results are returned in JSON format