import numpy as np
import pandas as pd
import streamlit as st

from fire_state import create_store, get_store, get_state, set_state, form_update

slot = "main"
key1 = create_store(slot, [
    ("state1", 0),
])

slot2 = "p2"
create_store(slot2, [
    ("slider", 0),
    ("arquivos", None),
    ('fileup', False),
])

def fetch():
    prev = get_state(slot, "state1")
    set_state(slot, ("state1", prev + 1))

if get_state(slot2, 'fileup') is True:
    set_state(slot2, ('arquivos', st.session_state['arquivo']))

st.button("+1", on_click=fetch)
st.text(f"Value: {get_state(slot, 'state1')}")
st.text(f"Value: {get_state(slot2, 'fileup')}")
st.text(f"Value: {get_state(slot2, 'arquivos')}")