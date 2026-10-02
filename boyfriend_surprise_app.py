import streamlit as st

st.set_page_config(
    page_title="For My Bebu ❤️",
    page_icon="💌",
    layout="centered"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at top left, #fff8fb 0%, transparent 35%),
        radial-gradient(circle at bottom right, #ffe1ea 0%, transparent 40%),
        linear-gradient(135deg, #fff5f8, #ffeaf0);
}

.block-container {
    max-width: 760px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.title {
    font-family: 'DM Serif Display', serif;
    text-align: center;
    color: #b83f61;
    font-size: 48px;
    line-height: 1.15;
}

.subtitle {
    text-align: center;
    color: #79515e;
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    margin-bottom: 25px;
}

.card {
    background: rgba(255,255,255,0.90);
    border: 1px solid rgba(190,70,100,0.10);
    border-radius: 28px;
    padding: 30px;
    margin: 22px 0;
    box-shadow: 0 12px 35px rgba(140,60,85,0.12);
}

.message {
    font-family: 'Poppins', sans-serif;
    color: #51333d;
    font-size: 16px;
    line-height: 1.9;
    text-align: center;
}

.quote {
    font-family: 'DM Serif Display', serif;
    color: #b83f61;
    font-size: 27px;
    text-align: center;
    line-height: 1.45;
}

.big {
    text-align: center;
    font-size: 70px;
}

.small {
    text-align: center;
    color: #9a6b78;
    font-family: 'Poppins', sans-serif;
    font-size: 13px;
}

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 18px;
    padding: 13px 18px;
    background: #d95d7d;
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    font-weight: 600;
    box-shadow: 0 7px 18px rgba(180,65,95,0.18);
}

.stButton > button:hover {
    background: #bd4869;
    color: white;
}

img {
    border-radius: 24px !important;
}

.footer {
    text-align: center;
    color: #a46d7b;
    font-family: 'Poppins', sans-serif;
    margin-top: 28px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- STATE --------------------
if "page" not in st.session_state:
    st.session_state.page = 1

def go_next():
    st.session_state.page += 1

def restart():
    st.session_state.page = 1

# -------------------- PAGE 1 --------------------
if st.session_state.page == 1:
    st.markdown('<div class="big">💌</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">A Little Surprise For You</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">For my favourite person — Shaurya ❤️</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="quote">"Okay Bebu... don't judge my coding skills yet." 😂</div>
        <br>
        <div class="message">
            I made this little corner of the internet just for you.
            <br><br>
            It has some of our memories, a few things I don't say
            enough, and obviously... a little bit of my drama.
            <br><br>
            So go on. Open it. ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 Open My Surprise"):
        go_next()
        st.rerun()

# -------------------- PAGE 2 --------------------
elif st.session_state.page == 2:
    st.markdown('<div class="title">Us. ❤️</div>', unsafe_allow_html=True)
    st.image("photo1.jpg", use_container_width=True)

    st.markdown("""
    <div class="card">
        <div class="message">
            I think one of my favourite things about us is that
            we never really feel like just a couple.
            <br><br>
            You're my boyfriend, obviously... but you're also my friend.
            And honestly, that part means so much to me.
            <br><br>
            From completely random conversations to the most
            unnecessary fights, somehow you have become such
            a huge part of my everyday life.
            <br><br>
            And I wouldn't have it any other way. ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🌷 There's more..."):
        go_next()
        st.rerun()

# -------------------- PAGE 3 --------------------
elif st.session_state.page == 3:
    st.markdown('<div class="title">A Little Throwback 🥹</div>', unsafe_allow_html=True)
    st.image("photo2.jpg", use_container_width=True)

    st.markdown("""
    <div class="card">
        <div class="message">
            Somewhere between all our conversations and all our
            stupid little moments, you became my person.
            <br><br>
            And when I look at pictures like this, I don't just see
            a photo. I see one more memory that I get to keep.
            <br><br>
            I hope we keep collecting these forever —
            the pretty memories and the completely chaotic ones too. 😂❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🎀 Next memory"):
        go_next()
        st.rerun()

# -------------------- PAGE 4 --------------------
elif st.session_state.page == 4:
    st.markdown('<div class="title">One Of My Favourites ❤️</div>', unsafe_allow_html=True)
    st.image("photo3.jpg", use_container_width=True)

    st.markdown("""
    <div class="card">
        <div class="message">
            Look at us. 😂
            <br><br>
            Two people who can fight over the smallest things,
            annoy each other for no reason, and still somehow
            not be able to stay without talking.
            <br><br>
            That's probably one of the most "us" things ever.
            <br><br>
            And honestly? I love it.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("👀 One more"):
        go_next()
        st.rerun()

# -------------------- PAGE 5 --------------------
elif st.session_state.page == 5:
    st.markdown('<div class="title">This One... 🫶</div>', unsafe_allow_html=True)
    st.image("photo4.jpg", use_container_width=True)

    st.markdown("""
    <div class="card">
        <div class="message">
            I hope you know that I notice the little things.
            <br><br>
            The way you care, the way you make me laugh,
            the way you somehow manage to tolerate all my
            moods and nakhre... 😂
            <br><br>
            You have given me so many moments that I genuinely
            want to keep with me for a very, very long time.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💗 Keep going"):
        go_next()
        st.rerun()

# -------------------- PAGE 6 --------------------
elif st.session_state.page == 6:
    st.markdown('<div class="title">Okay, Important Question 👀</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="big">🥹❤️</div>
        <div class="message">
            Do you know how special you are to me?
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES ❤️"):
            st.session_state.answer = "yes"
            go_next()
            st.rerun()

    with col2:
        if st.button("NO 😭"):
            st.session_state.answer = "no"
            go_next()
            st.rerun()

# -------------------- PAGE 7 --------------------
elif st.session_state.page == 7:
    answer = st.session_state.get("answer", "yes")

    st.markdown('<div class="title">Hmmmm... 😂</div>', unsafe_allow_html=True)

    if answer == "yes":
        st.markdown("""
        <div class="card">
            <div class="big">🥹❤️</div>
            <div class="message">
                Good. Because I really hope you know that.
                <br><br>
                You're not just someone I love.
                You're someone I genuinely enjoy being myself with.
                <br><br>
                And that is a very special thing.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card">
            <div class="big">😭</div>
            <div class="message">
                EXCUSE ME?!
                <br><br>
                Wrong answer, Bebu. Please reconsider your decision. 😂
                <br><br>
                Obviously you are special to me.
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("💌 I have one last thing to say"):
        go_next()
        st.rerun()

# -------------------- PAGE 8 --------------------
elif st.session_state.page == 8:
    st.markdown('<div class="title">And Finally... ❤️</div>', unsafe_allow_html=True)
    st.image("photo5.jpg", use_container_width=True)

    st.markdown("""
    <div class="card">
        <div class="message">
            Dear Bebu,
            <br><br>
            I don't think I can fit everything I feel into one
            little website, but I can at least try.
            <br><br>
            Thank you for being there through the good days,
            the annoying days, the random fights, the jokes,
            the conversations that make absolutely no sense,
            and all the tiny moments in between.
            <br><br>
            I love that before anything else, we are friends.
            That's something I never want to lose.
            <br><br>
            We have already made so many memories together,
            and I hope this is only the beginning of many more.
            <br><br>
            So here's your tiny reminder:
            <br><br>
            <b>You are loved. You are important. And you are
            ridiculously lucky to have a girlfriend who made
            an entire website for you. 😂❤️</b>
            <br><br>
            Okay fine, maybe I'm the lucky one too.
            <br><br>
            Always your annoying person,
            <br>
            <b>Priyal ❤️</b>
        </div>
    </div>

    <div class="footer">
        Made with love, memories, and slightly questionable coding skills. 💌
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🔄 Start Again"):
        restart()
        st.rerun()
