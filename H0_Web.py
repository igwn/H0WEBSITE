"""
Script for website 

Luis Miguel Galvis E
"""

#Libraries
from pathlib import Path
import streamlit as st
from PIL import Image
from H0live import *
from numpy import where,array
import json

###########################################
#Session status
if 'object' not in st.session_state:
    st.session_state.object = None


sb = st.sidebar

st.title('$H_0$ estimator')

#add columns for subtitle and LOGO.
col1, col2 = st.columns([7, 2])

with col1:
    st.subheader('An estimator for the Hubble Constant based on gravitational wave multi-messenger observations')

with col2:
    image = Image.open('LVK_rainbow_dark.png')
    st.image(image)

sb.header("Adjust the assumptions that are used when estimating the Hubble constant")

csvfile='bright_sirens.csv'
jsonfile='bright-sirens.json'


# Helper function to read the content of a file
def read_file(filepath):
    return Path(filepath).read_text()


#Function to read the csv file and get the events
def list_events_old(csv_file):
    ev1=pd.read_csv(csv_file,sep=",",engine='python')
    return ev1.columns[1:].values.tolist()

class list_events:
    def __init__(self,jsonfile):
        jsonin=json.load(open(jsonfile))
        self.evlist={}
        for gwev in jsonin:
            gwname=jsonin[gwev]['display_name']
            self.evlist[gwname]={}
            self.evlist[gwname]['counterpart']=[]
            self.evlist[gwname]['column']=[]
            for emev in jsonin[gwev]['Counterparts']:
                emname=jsonin[gwev]['Counterparts'][emev]['display_name']
                self.evlist[gwname]['counterpart'].append(emname)
                self.evlist[gwname]['column'].append(jsonin[gwev]['Counterparts'][emev]['column_name'])
        return
    
    def list(self):
        return self.evlist
    def getcolumn(self,gwev,emev):
        print(gwev,emev,self.evlist[gwev]['counterpart'])
        print(np.argwhere(self.evlist[gwev]['counterpart']==emev))
        return self.evlist[gwev]['column'][np.where(np.array(self.evlist[gwev]['counterpart'])==emev)[0][0]]

ev_list = list_events(jsonfile)
dictionary=ev_list.list()
print(dictionary)

#To create the lists to be used
Events=[]
Events_in_checbox=[]
Counterpart_in_selectbox=[]

#To create the sidebar form
with sb.form("My form"):
#To select the events and their counterparts
    st.subheader("Events and counterparts")
    st.markdown("""**Gravitational wave events:** Gravitational wave events are named starting with the prefix GW, while observations that trigger an event alert but have not (yet) been published are named starting with the prefix S.""")
    st.markdown("""**Electromagnetic counterparts:** Electromagnetic counterpart associations to a gravitational wave event will be labelled as "potential" until confirmed in an LVK publication.""")
    st.markdown("""**Select the GW events you want to include, and its EM counterpart:**""")
    for key in dictionary:
        if Events_in_checbox==[] and Counterpart_in_selectbox==[]:
            Events_in_checbox.append(st.checkbox(key,True))
            Events.append(key)
            Counterpart_in_selectbox.append(st.selectbox("Counterpart ",dictionary[key]['counterpart'],key=key,label_visibility="collapsed"))
        else:
            Events_in_checbox.append(st.checkbox(key))
            Events.append(key)
            Counterpart_in_selectbox.append(st.selectbox("Counterpart ",dictionary[key]['counterpart'],key=key,label_visibility="collapsed"))
    
 
#To select the desired prior
    #st.markdown("""Select the prior you want to use for the $H_0$ estimation:""")
    prior_list=['uniform', 'log']
    choice = st.selectbox("**Prior**",prior_list) 

#To select additional H0 estimates and the plot of Individual event likelihoods 
    st.subheader("Additional options")
    planck_checkbox = st.checkbox('Planck H0 estimate',help='Planck Collaboration. *Planck 2018 results VI. Cosmological parameters*. **A&A** 641, A6 (2020). [https://doi.org/10.1051/0004-6361/201833910](https://doi.org/10.1051/0004-6361/201833910)')
    sh0es_checkbox = st.checkbox('SH0ES H0 estimate',help='Riess, A. G., Casertano, S., Yuan, W., Macri, L. M., and Scolnic, D. *Large Magellanic Cloud Cepheid Standards Provide a 1% Foundation for the Determination of the Hubble Constant and Stronger Evidence for Physics beyond ΛCDM*. **The Astrophysical Journal** 876, no. 1 (2019). [https://doi.org/10.3847/1538-4357/ab1422](https://doi.org/10.3847/1538-4357/ab1422)')
    indivual_likelihoods_checkbox = st.checkbox('Individual event likelihoods')
    add_options_choice=[planck_checkbox,sh0es_checkbox,indivual_likelihoods_checkbox]
    


#To create the list of events and their counterparts chosen
    choice_list1=[]
    for i in range(len(Events_in_checbox)):
        if Events_in_checbox[i]==True:
            choice_list1.append(ev_list.getcolumn(Events[i],str(Counterpart_in_selectbox[i])))
            # choice_list1.append(str(Events[i])+"_"+str(Counterpart_in_selectbox[i]))


     
    #To calculate the H0    
    Calculated = st.form_submit_button("Calculate")   

#When no event is selected
if choice_list1==[]:
    if  Calculated or not Calculated:
        st.header(":red[Please select an event and its counterpart!]")

    

#Default values starting the program
else:
    choice_list2=[]

    if not Calculated and st.session_state.object is None:
        # choice_list2.append(str(Events[0])+"_"+str(dictionary[Events[0]][0]))
        choice_list2.append(ev_list.getcolumn(Events[0],str(Counterpart_in_selectbox[0])))
        h0live_output=H0live(choice_list2, choice,planck=add_options_choice[0],riess=add_options_choice[1],likelihood_plot=add_options_choice[2],data_download=True,likelihood_fname=csvfile)
        csv = h0live_output.H0data_download.to_csv(index=False)
                
        sb.download_button(
        "Download data",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv')  
#If events are selected
    if Calculated:
        st.session_state.object=H0live(choice_list1, choice,planck=add_options_choice[0],riess=add_options_choice[1],likelihood_plot=add_options_choice[2],data_download=True,likelihood_fname=csvfile)
        csv = st.session_state.object.H0data_download.to_csv(index=False)
        a=sb.download_button(
        "Download data",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv')     
        
#To work outside of form without disappearing the image
    if not Calculated and st.session_state.object is not None:
        h0live_output=H0live(choice_list1, choice,planck=add_options_choice[0],riess=add_options_choice[1],likelihood_plot=add_options_choice[2],data_download=True,likelihood_fname=csvfile)
        csv = h0live_output.H0data_download.to_csv(index=False)
        b=sb.download_button(
        "Download data",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv')  

# Display the content of Description.md
description = read_file("Description.md")
st.markdown(description)
