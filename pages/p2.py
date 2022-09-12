import streamlit as st
from fire_state import create_store, get_state, set_state, get_store

slot = "main"
create_store(slot, [
    ("state1", 0),
])

slot2 = "p2"
create_store(slot2, [
    ("slider", 0),
    ("arquivos", None),
    ('fileup', False),
])

'''if 'arquivo' not in st.session_state:
    st.session_state['arquivo'] = None
'''
def fetch(atrib=False):
    set_state(slot2, ("slider", st.session_state['key1']))
    if get_state(slot2, 'fileup') == False or atrib == True:
        set_state(slot2, ('arquivos', st.session_state['arquivo']))
        set_state(slot2, ('fileup', True))
    #set_state(slot2, ('arquivos', st.session_state['arquivo']))

if get_state(slot2, 'fileup') is True:
    set_state(slot2, ('arquivos', st.session_state['arquivo']))

st.slider("+1", 1, 10, on_change=fetch, key='key1', value=get_state(slot2, "slider"))
st.file_uploader('arquivos', on_change=fetch, key='arquivo')
st.session_state['arquivo']
get_state(slot2, 'arquivos')
if st.session_state['arquivo'] is not get_state(slot2, 'arquivos'):
    fetch(atrib=True)


st.text(f"Value: {get_state(slot2, 'slider')}")
st.text(f"Value: {get_state(slot, 'state1')}")
st.text(f"Value: {get_state(slot2, 'arquivos')}")
