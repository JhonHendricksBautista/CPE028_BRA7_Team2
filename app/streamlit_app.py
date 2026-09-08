import streamlit as st
from pathlib import Path
import base64

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

/* -----------------------------------------------
   MAIN TITLE
------------------------------------------------ */

.main-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 32px;
    font-weight: 700;
}

.title-icon {
    width: 32px;
    height: 32px;
    object-fit: contain;
}


/* -----------------------------------------------
   SUBTITLE
------------------------------------------------ */

.subtitle {
    color: #8b949e;
    font-size: 16px;
}


/* -----------------------------------------------
   SECTION HEADER
------------------------------------------------ */

.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 28px;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 10px;
}

.section-icon {
    width: 28px;
    height: 28px;
    object-fit: contain;
}


/* -----------------------------------------------
   SIDEBAR TITLE
------------------------------------------------ */

.sidebar-title {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 15px;
}

.sidebar-icon {
    width: 24px;
    height: 24px;
    object-fit: contain;
}

.search-button-container {
    height: 28px;
}


/* -----------------------------------------------
   IP CARD
------------------------------------------------ */

.ip-card {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

.ip-label {
    color: #8b949e;
    font-size: 14px;
}

.ip-value {
    font-size: 24px;
    font-weight: 600;
}


/* -----------------------------------------------
   SECTION TITLE
------------------------------------------------ */

.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
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
            """
            <div class="ip-card">
                <div class="ip-label">IPv4 Address</div>
                <div class="ip-value">—</div>
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

        st.write("**ISP**")
        st.write("—")

        st.write("**ASN**")
        st.write("—")

        st.write("**Country**")
        st.write("—")

    with col2:

        st.write("**Country Code**")
        st.write("—")

        st.write("**Region**")
        st.write("—")

        st.write("**City**")
        st.write("—")


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
        st.write("—")

        st.write("**Longitude**")
        st.write("—")

    with col2:

        st.write("**Timezone**")
        st.write("—")

        st.write("**Postal Code**")
        st.write("—")


    # ----------------------------------------------
    # REFRESH
    # ----------------------------------------------

    st.divider()

    if st.button(
        "Refresh Information",
        use_container_width=False
    ):

        # API function will be implemented here
        pass

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

            # ------------------------------------------
            # API FUNCTION WILL BE IMPLEMENTED HERE
            # ------------------------------------------

            # data = fetch_target_ip(ip_address)


            # ------------------------------------------
            # IP INFORMATION
            # ------------------------------------------

            st.markdown(
                '<div class="section-title">IP Information</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write("**IP Address:** —")
                st.write("**Type:** —")

            with col2:

                st.write("**Country:** —")
                st.write("**Country Code:** —")


            # ------------------------------------------
            # NETWORK INFORMATION
            # ------------------------------------------

            st.markdown(
                '<div class="section-title">Network Information</div>',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write("**ISP:** —")
                st.write("**ASN:** —")

            with col2:

                st.write("**Region:** —")
                st.write("**City:** —")


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

                st.write("**Latitude:** —")
                st.write("**Longitude:** —")

            with col2:

                st.write("**Timezone:** —")
                st.write("**Postal Code:** —")