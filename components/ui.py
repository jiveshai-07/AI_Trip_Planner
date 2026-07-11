import streamlit as st


def load_ui():

    st.markdown("""
<style>

:root{
  --primary:#0F766E;
  --primary-dark:#0B5D57;
  --primary-light:#14B8A6;

  --bg:#F8FAFC;
  --surface:#FFFFFF;

  --border:#E2E8F0;

  --text-main:#0F172A;
  --text-muted:#64748B;

  --shadow-sm:0 4px 10px rgba(15,23,42,.05);
  --shadow-md:0 10px 25px rgba(15,23,42,.08);
  --shadow-lg:0 20px 40px rgba(15,118,110,.15);

  --radius:18px;
}

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

section[data-testid="stSidebar"]{
display:none;
}

[data-testid="stSidebarNav"]{
display:none;
}

.stApp{
background:var(--bg);
font-family:'Segoe UI',sans-serif;
color:var(--text-main);
}

.block-container{
max-width:1400px;
padding-top:24px;
padding-bottom:40px;
padding-left:4%;
padding-right:4%;
}

h1{
font-size:2.4rem !important;
font-weight:800 !important;
color:var(--text-main);
margin-bottom:10px;
}

h2,h3,h4{
font-weight:700 !important;
color:var(--text-main);
}

p{
color:var(--text-main);
}

.stButton > button{
width:100%;
height:52px;

background:var(--surface);
color:var(--text-main);

border:1.5px solid var(--border);
border-radius:14px;

font-size:15px;
font-weight:600;

transition:all .25s ease;

box-shadow:var(--shadow-sm);
}

.stButton>button{
width:100%;
height:50px;
border-radius:14px;
font-weight:600;
transition:all .25s ease;
}

.stButton>button:hover{
transform:translateY(-4px) scale(1.02);
box-shadow:0 15px 30px rgba(0,0,0,.12);
}

.stDownloadButton > button{
width:100%;
height:52px;

background:var(--surface);
color:var(--text-main);

border:1.5px solid var(--border);
border-radius:14px;

font-size:15px;
font-weight:600;

transition:all .25s ease;

box-shadow:var(--shadow-sm);
}

.stDownloadButton > button:hover{
background:var(--primary);
color:white;
border-color:var(--primary);

transform:translateY(-3px);

box-shadow:var(--shadow-lg);
}
div[data-testid="stMetric"]{
transition:.25s;
border-radius:16px;
}

div[data-testid="stMetric"]:hover{
transform:translateY(-5px);
box-shadow:0 15px 35px rgba(0,0,0,.08);
}
div[data-testid="stExpander"]{
transition:.25s;
}

div[data-testid="stExpander"]:hover{
transform:translateY(-2px);
}                

div[data-testid="stMetric"]{
background:var(--surface);

padding:20px;

border-radius:var(--radius);

border:1px solid var(--border);

box-shadow:var(--shadow-md);

min-height:130px;

transition:.25s ease;
}

div[data-testid="stMetric"]:hover{
transform:translateY(-5px);
box-shadow:var(--shadow-lg);
}

div[data-testid="stExpander"]{
border-radius:16px !important;
border:1px solid var(--border) !important;
overflow:hidden;
}

div[data-testid="stExpander"] details{
border-radius:16px;
}

input,
textarea{
border-radius:14px !important;
border:1.5px solid var(--border) !important;
}

.stTextInput input{
height:50px;
}

.stNumberInput input{
height:50px;
}

.stSelectbox div[data-baseweb="select"]{
border-radius:14px;
}

.hero-card{
background:linear-gradient(
135deg,
#0F766E,
#14B8A6
);

padding:32px;

border-radius:22px;

color:white;

margin-bottom:25px;

box-shadow:var(--shadow-lg);
}

.hero-title{
font-size:34px;
font-weight:800;
margin-bottom:10px;
}

.hero-subtitle{
font-size:16px;
opacity:.95;
}

.quick-card{
background:white;

border:1px solid var(--border);

border-radius:18px;

padding:24px;

min-height:170px;

box-shadow:var(--shadow-md);

transition:.25s ease;
}

.quick-card:hover{
transform:translateY(-5px);
box-shadow:var(--shadow-lg);
}

.footer{
text-align:center;

padding:30px 0;

margin-top:40px;

color:var(--text-muted);

border-top:1px solid var(--border);

font-size:14px;
}
@media (max-width:900px){

.block-container{
padding-left:18px;
padding-right:18px;
}

.hero-card{
padding:24px;
}

.hero-title{
font-size:34px;
}

.hero-subtitle{
font-size:17px;
}

.quick-card{
margin-bottom:15px;
}

.stButton>button{
height:48px;
}

}
</style>
""", unsafe_allow_html=True)


def footer():
    st.markdown("""
<div class="footer">
🧭 AI Trip Planner v1.0 • Built by Jivesh Mishra
</div>
""", unsafe_allow_html=True)
