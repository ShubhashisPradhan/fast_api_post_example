import streamlit as st
import requests

# ==========================
# Config
# ==========================
API_URL = "http://127.0.0.1:8000/search"  # FastAPI endpoint

st.set_page_config(page_title="Partner Search API Tester", layout="centered")
st.title("🔍 Partner Search API Tester")

# ==========================
# Input Form
# ==========================
with st.form("search_form"):
    st.subheader("Enter Search Parameters")

    request_id = st.text_input("Request ID", value="REQ12345")
    company_name = st.text_input("Company Name", value="Sample Company")
    address = st.text_input("Address", value="123 Main St, City")
    country = st.text_input("Country Code", value="USA")
    search_database = st.text_input("Search Database", value="db1")

    submitted = st.form_submit_button("Search")

# ==========================
# Submit & Display Results
# ==========================
if submitted:
    payload = {
        "request_id": request_id,
        "company_name": company_name,
        "address": address,
        "country": country,
        "search_database": search_database,
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()

            st.success("✅ Response received successfully!")
            st.json(data)  # Pretty print full JSON

            # Optional: Display matches in table form
            if data.get("top_5_matches"):
                st.subheader("Top Matches")
                for idx, match in enumerate(data["top_5_matches"], start=1):
                    st.markdown(f"### Match {idx}")
                    st.write(f"**Partner Code:** {match['partner_code']}")
                    st.write(f"**Company Name:** {match['company_name']}")
                    st.write(f"**Address:** {match['address']}")
                    st.write(f"**Country:** {match['country']}")
                    st.write(f"**State:** {match['state']}")
                    st.write(f"**Postal:** {match['postal']}")
                    st.write(f"**Search DB:** {match['search_db']}")
                    st.write(f"**Match Score:** {match['match_score']}")
                    st.markdown("---")
            else:
                st.warning("No matches found.")
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 Request failed: {e}")
