import streamlit as st

def main():
    # Set up page layout
    st.set_page_config(page_title="Cornell Mediator", layout="wide")

    # Add custom styles
    st.markdown("""
        <style>
            .big-font {
                font-size:20px !important;
            }
        </style>
        """, unsafe_allow_html=True)

    # Main container
    with st.container():
        # Record Button
        if st.button('Record'):
            st.write('Recording...')

        # Response Text
        st.markdown("<p class='big-font'>Let's dive in the essence of authentic Indian Masala chai, a desi way to brighten your mood</p>", unsafe_allow_html=True)

        # Mood Container
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("client/images/point-image.png", caption="Point Image")
        with col2:
            st.markdown("<p class='big-font'>Had a bad day? Trying to stay calm?</p>", unsafe_allow_html=True)
            st.image("client/images/point-image-2.png.png")
        with col3:
            st.markdown("<p class='big-font'>Pissed off by the landlord? And don’t know what to say?</p>", unsafe_allow_html=True)
            st.image("client/images/point-image-3.png.png")

        # Generate Response Button
        if st.button('Generate Response'):
            st.write('Generating Response...')

        # User and Brand Info
        st.image("user-circle.png", caption="Akshay Iyer")
        st.markdown("<p class='big-font'><span>Cornell</span> Mediator</p>", unsafe_allow_html=True)

    # Banner Content
    # st.image("banner-content-container.png")

if __name__ == "__main__":
    main()
