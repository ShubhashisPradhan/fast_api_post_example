📑 Partner Search API Prototype – Documentation

Repository: fast_api_post_example

Author: Shubhashis Pradhan
Tech Stack: FastAPI (Backend) • Pydantic (Validation) • Streamlit (Frontend UI for testing)

1. 🔍 Objective

This project demonstrates a prototype implementation of a Partner Search API.
The API accepts company search details (company name, address, country, etc.), validates the input, and returns top 5 best-matched companies with metadata such as partner code, state, postal code, and a normalized match score.

The prototype is built for demonstration and testing purposes (no database integration yet).

2. ⚙️ Implementation Details
Backend (FastAPI)

Framework: FastAPI

Endpoint: /search (POST)

Request Model: RequestBody

request_id: Unique ID to track a transaction

company_name: Company name to search

address: Full address string

country: Country code (e.g., USA, GBR)

search_database: Placeholder string (default: "abcd")

Response Model: ResponseBody

request_id: Echo of input request ID

top_5_matches: Array of MatchOutCome objects

Validation:

request_id → Must be non-empty

match_score → Normalized between 0.0 and 1.0

top_5_matches → Automatically sorted in descending order by match_score and limited to 5 results

Error Handling:

Returns structured HTTP 500 error with details if processing fails

Frontend (Streamlit UI)

Simple form-based client to send requests to /search

Fields include: request_id, company_name, address, country, and search_database

Displays:

Raw JSON response

Human-friendly formatted results (each match displayed with key details)

Allows interactive testing of different inputs

3. 📡 API Usage
Endpoint
POST /search

Request Example
{
  "request_id": "REQ12345",
  "company_name": "Sample Company",
  "address": "123 Main St, City",
  "country": "USA",
  "search_database": "db1"
}

Response Example
{
  "request_id": "REQ12345",
  "top_5_matches": [
    {
      "partner_code": "PART001",
      "company_name": "Sample Company Inc",
      "address": "123 Main St, City, State",
      "country": "USA",
      "state": "CA",
      "postal": "12345",
      "search_db": "db1",
      "match_score": 0.95
    }
  ]
}

4. 🧪 Test Cases & Results

Positive Test: Valid company input → Returns one or more matches (see /images/test_result_1.png)

Empty Request ID: Rejected with validation error (see /images/test_result_2.png)

Invalid Match Score (>1): Blocked by validation rules (see /images/test_result_3.png)

More than 5 Matches: Automatically truncated and sorted by score (see /images/test_result_4.png)

All test result screenshots are available in the images/ folder of the repo.

5. 🚀 How to Run
Backend
# Install dependencies
pip install fastapi uvicorn

# Run FastAPI app
uvicorn app:app --reload --port 8000

Frontend
# Install dependency
pip install streamlit requests

# Run UI
streamlit run search_ui.py


Access Streamlit UI at: http://localhost:8501


FastApi page :
URL endpoint for local machine: API_URL = "http://127.0.0.1:8000/search"
<img width="1818" height="955" alt="image" src="https://github.com/user-attachments/assets/c449f875-7c82-40ea-94b4-2c82c6051d3e" />

