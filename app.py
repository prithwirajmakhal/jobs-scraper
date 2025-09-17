from flask import Flask, request, jsonify
from jobspy import scrape_jobs
from flask_cors import CORS
SUPPORTED_SITES = ['bayt', 'bdjobs', 'glassdoor',
                   'google', 'indeed', 'linkedin', 'naukri']

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'status': 'success', 'message': 'All is well'}), 200


@app.route('/scrape-jobs')
def scrape_linkedin_jobs():
    try:
        # Get parameters from request URL
        site_name = [site.strip().lower() for site in request.args.get(
            'site_name', 'linkedin').split(',')]
        if not all(site for site in site_name):
            raise ValueError("Invalid site_name: cannot be empty")
        if not all(site in SUPPORTED_SITES for site in site_name):
            raise ValueError(
                f"Invalid site_name: must be one of {', '.join(SUPPORTED_SITES)}")

        search_term = request.args.get('search_term', 'software engineer')
        if not search_term.strip():
            raise ValueError("Search term cannot be empty")

        location = request.args.get('location', 'San Francisco, CA')
        if not location.strip():
            raise ValueError("Location cannot be empty")

        try:
            results_wanted = int(request.args.get('results_wanted', 20))
            if results_wanted <= 0:
                raise ValueError("Results wanted must be greater than 0")
        except ValueError:
            raise ValueError(
                "Invalid results_wanted: must be a positive integer")

        try:
            hours_old = int(request.args.get('hours_old', 72))
            if hours_old <= 0:
                raise ValueError("Hours old must be greater than 0")
        except ValueError:
            raise ValueError("Invalid hours_old: must be a positive integer")

        country = request.args.get('country', 'USA')
        if not country.strip():
            raise ValueError("Country cannot be empty")

        fetch_description = request.args.get(
            'fetch_description', 'true').lower() == 'true'

        google_search_term = request.args.get(
            'google_search_term',
            f"{search_term} jobs near {location} since yesterday"
        )

        # Scrape jobs with provided parameters
        jobs = scrape_jobs(
            site_name=site_name,
            search_term=search_term,
            google_search_term=google_search_term,
            location=location,
            results_wanted=results_wanted,
            hours_old=hours_old,
            country_indeed=country,
            linkedin_fetch_description=fetch_description
        )

        # Convert DataFrame to dictionary for JSON response
        jobs_dict = jobs.to_dict(orient='records')
        return jsonify({
            'status': 'success',
            'jobs': jobs_dict
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True)
