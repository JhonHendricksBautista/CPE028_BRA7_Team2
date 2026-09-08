import streamlit as st
from pathlib import Path
import base64
from api_request import fetch_my_ip, fetch_target_ip
import asyncio

#Experimental UI streamlit

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="IP Address Information",
    layout="wide"
)


# --------------------------------------------------
# IMAGE FUNCTION
# --------------------------------------------------

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# --------------------------------------------------
# IMAGE PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

GLOBE_PATH = BASE_DIR / "assets" / "Globe.png"
HOUSE_PATH = BASE_DIR  / "assets" / "House.png"
SEARCH_PATH = BASE_DIR  / "assets" / "Search.png"
LOCATION_PATH = BASE_DIR  / "assets" / "Location.png"
INFORMATION_PATH = BASE_DIR / "assets" / "Information.png"
CONNECTION_PATH = BASE_DIR  / "assets" / "Connection.png"



# --------------------------------------------------
# LOAD IMAGES
# --------------------------------------------------

globe_icon = get_image_base64(GLOBE_PATH)
house_icon = get_image_base64(HOUSE_PATH)
search_icon = get_image_base64(SEARCH_PATH)
location_icon = get_image_base64(LOCATION_PATH)
information_icon = get_image_base64(INFORMATION_PATH)
connection_icon = get_image_base64(CONNECTION_PATH)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

:root {
    --background: #1F2937;
    --sidebar: #24262F;
    --card: #161b22;
    --card-border: #404040;
    --primary: #2563EB;
    --primary-hover: #1D4ED8;
    --light_green: #90EE90;
    --white: #FFFFFF;
    --text-dark: #FFFFFF;
    --text-secondary: #FFFFFF;
    --text-muted: #B8C0CC;
}

.stApp {
    background-color: var(--background);
}

.main-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 32px;
    font-weight: 700;
    color: var(--text-dark);
}

.title-icon {
    width: 32px;
    height: 32px;
    object-fit: contain;
}

.subtitle {
    color: var(--text-secondary);
    font-size: 16px;
}

.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 28px;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 10px;
    color: var(--text-dark);
}

.section-icon {
    width: 28px;
    height: 28px;
    object-fit: contain;
}

section[data-testid="stSidebar"] {
    background-color: var(--sidebar);
}

.sidebar-title {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 15px;
    color: var(--white);
}

.sidebar-icon {
    width: 30px;
    height: 30px;
    object-fit: contain;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #E5E7EB !important;
}

.search-button-container {
    height: 28px;
}

.ip-card {
    background-color: var(--card);
    border: 1px solid var(--card-border);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

.ip-label {
    color: var(--text-muted);
    font-size: 14px;
}

.ip-value {
    color: var(--light_green);
    font-size: 24px;
    font-weight: 600;
}

.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
    color: var(--text-dark);
}

.stApp p,
.stApp label {
    color: var(--text-dark);
}

.stTextInput input {
    background-color: #161b22;
    color: #FFFFFF;
    border: 1px solid #FFFFFF;
    border-radius: 8px;
}

.stTextInput input::placeholder {
    color: #6B7280;
}

.stButton button {
    background-color: var(--primary);
    color: var(--white);
    border: 1px solid var(--primary);
    border-radius: 8px;
    font-weight: 600;
}

.stButton button:hover {
    background-color: var(--primary-hover);
    color: var(--white);
}

hr {
    border-color: #AAAAAA;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    f"""
    <div class="main-title">
        <img src="data:image/png;base64,{information_icon}" class="title-icon">
        <span>IP Address Information</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Network Location & IP Lookup Tool</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown(
    f"""
    <div class="sidebar-title">
        <img src="data:image/png;base64,{globe_icon}" class="sidebar-icon">
        <span>IP Address Tool</span>
    </div>
    """,
    unsafe_allow_html=True
)


selection = st.sidebar.radio(
    "Select an option",
    [
        "My IP",
        "Search IP"
    ]
)


# ==================================================
# MY IP
# ==================================================

if selection == "My IP":

    # ----------------------------------------------
    # PAGE HEADER
    # ----------------------------------------------


    # get the API data and store in use state variable
    if 'my_ip_data' not in st.session_state:
        try:
            st.session_state.my_ip_data = asyncio.run(fetch_my_ip())

        except Exception as e:
            st.error(f"Unable to fetch IP information: {e}")
            st.stop()


    # get the json data
    data = st.session_state.my_ip_data

    # EXTRACT THE IP
    ipv4 = data.get('ip','Not Found')

    # ------EXTRACT THE DATA upper part
    currency = data.get('currency','N/A')
    country_code = data.get('country','N/A')
    country_name = data.get('country_name','N/A')
    ASN = data.get('asn','N/A')
    region = data.get('region','N/A')
    city = data.get('city','N/A')

    # ------- EXTRACT THE DATA lower part
    latitude = data.get('latitude','N/A')
    longitude = data.get('longitude', 'N/A')
    timezone = data.get('timezone', 'N/A')
    postal = data.get('postal','N/A')

    st.markdown(
        f"""
        <div class="section-header">
            <img src="data:image/png;base64,{house_icon}" class="section-icon">
            <span>My IP</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "View your current IP address information."
    )


    # ----------------------------------------------
    # IP ADDRESS
    # ----------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="ip-card">
                <div class="ip-label">IPv4 Address</div>
                <div class="ip-value">{ipv4}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="ip-card">
                <div class="ip-label">IPv6 Address</div>
                <div class="ip-value">—</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ----------------------------------------------
    # NETWORK INFORMATION
    # ----------------------------------------------

    st.markdown(
    f"""
    <div class="section-header">
        <img src="data:image/png;base64,{connection_icon}" class="section-icon">
        <span>Network Information</span>
    </div>
    """,
    unsafe_allow_html=True
)

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Currency**")
        st.write(f"{currency}")

        st.write("**ASN**")
        st.write(f"{ASN}")

        st.write("**Country**")
        st.write(f"{country_name}")

    with col2:

        st.write("**Country Code**")
        st.write(f"{country_code}")

        st.write("**Region**")
        st.write(f"{region}")

        st.write("**City**")
        st.write(f"{city}")


    # ----------------------------------------------
    # LOCATION INFORMATION
    # ----------------------------------------------

    st.markdown(
        f"""
        <div class="section-header">
            <img src="data:image/png;base64,{location_icon}" class="section-icon">
            <span>Location Information</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Latitude**")
        st.write(f"{latitude}")

        st.write("**Longitude**")
        st.write(f"{longitude}")

    with col2:

        st.write("**Timezone**")
        st.write(f"{timezone}")

        st.write("**Postal Code**")
        st.write(f"{postal}")


    # ----------------------------------------------
    # REFRESH
    # ----------------------------------------------

    st.divider()

    if st.button(
        "Refresh Information",
        use_container_width=False
    ):

        # API function will be implemented here
        try:
            st.session_state.my_ip_data = asyncio.run(fetch_my_ip())
            st.rerun()
        
        except Exception as e:
            st.error(f"Unable to fetch IP information: {e}")
            st.stop()

    st.caption("Ready")
        #STATUS OF API / UPDATE DATE / POSSIBLE IMPLEMENTATION

# ==================================================
# SEARCH IP
# ==================================================

elif selection == "Search IP":

    # ----------------------------------------------
    # PAGE HEADER
    # ----------------------------------------------

    st.markdown(
        f"""
        <div class="section-header">
            <img src="data:image/png;base64,{search_icon}" class="section-icon">
            <span>Search IP</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Search information of IP address."
    )


    # ----------------------------------------------
    # SEARCH BOX
    # ----------------------------------------------

    col1, col2 = st.columns([4, 1])

    with col1:

        ip_address = st.text_input(
            "IP Address",
            placeholder="Search for an IP address"
        )

    with col2:

        st.markdown(
            "<div style='height: 28px;'></div>",
            unsafe_allow_html=True
        )

        search_button = st.button(
            "Search",
            use_container_width=True
        )


    # ==================================================
    # SEARCH RESULT
    # ==================================================

    # IMPORTANT:
    # This is OUTSIDE col1 and col2

    if search_button:

        if not ip_address:

            st.warning("Please enter an IP address.")

        else:
            try:
                st.session_state.target_ip_data = asyncio.run(fetch_target_ip(ip_address))

            except Exception as e:
                st.error(f"Unable to fetch IP information: {e}")
                st.stop()

            fetched_ip_data = st.session_state.target_ip_data

            # ------------------------------------------
            # API FUNCTION WILL BE IMPLEMENTED HERE
            # ------------------------------------------

            # data = fetch_target_ip(ip_address)


            # ------------------------------------------
            # IP INFORMATION
            # ------------------------------------------

            # Extract IP information
            ip_add = fetched_ip_data.get('ip','N/A')
            ip_type = fetched_ip_data.get('version','N/A')
            country = fetched_ip_data.get('country_name','N/A')
            country_code = fetched_ip_data.get('country_code','N/A')

            # Extract Network Information
            currency = fetched_ip_data.get('currency','N/A')
            ASN = fetched_ip_data.get('asn','N/A')
            region = fetched_ip_data.get('region','N/A')
            city = fetched_ip_data.get('city','N/A')
        
            # Extract Location information
            latitude = fetched_ip_data.get('latitude','N/A')
            longitude = fetched_ip_data.get('longitude','N/A')
            timezone = fetched_ip_data.get('timezone','N/A')
            postal = fetched_ip_data.get('postal','N/A')

            st.markdown(f"""
    <div class="section-header">
        <img src="data:image/png;base64,{information_icon}" class="section-icon">
        <span>Network Information</span>
    </div>  """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"**IP Address:** {ip_add}")
                st.write(f"**Type:** {ip_type}")

            with col2:

                st.write(f"**Country:** {country}")
                st.write(f"**Country Code:** {country_code}")


            # ------------------------------------------
            # NETWORK INFORMATION
            # ------------------------------------------

            st.markdown(
                '<div class="section-title">Network Information</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"**Currency:** {currency}")
                st.write(f"**ASN:** {ASN}")

            with col2:

                st.write(f"**Region:** {region}")
                st.write(f"**City:** {city}")


            # ------------------------------------------
            # LOCATION INFORMATION
            # ------------------------------------------

            st.markdown(
                f"""
                <div class="section-header">
                    <img src="data:image/png;base64,{location_icon}" class="section-icon">
                    <span>Location Information</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"**Latitude:** {latitude}")
                st.write(f"**Longitude:** {longitude}")

            with col2:

                st.write(f"**Timezone:** {timezone}")
                st.write(f"**Postal Code:** {postal}")