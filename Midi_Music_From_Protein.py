### This code utilizes the pyknon library by Pedro Kroger,
### along with lessons learned from his book
### "Music for Geeks and Nerds".

#!/usr/bin/env python

# Music imports
from __future__ import division
import collections
import itertools
from random import choice
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq, Rest
# For creating simple GUI
from tkinter import *
# For opening urls
from urllib.request import urlopen
# For changing directories
import os



# Define amino acid to music function (aa_to_music)
def aa_to_music():

    # Get cwd of python script.
    os.chdir(os.path.dirname(sys.argv[0]))

    # Generate dictionary
    # for amino acid -> number conversion
    aa_notes = {'A':0, 'R':1, 'N':2, 'D':3, 'B':4, 'C':5, 'Q':6, 'E':7, 'Z':8,
     'G':9, 'H':10, 'I':11, 'L':12, 'K':13, 'M':14, 'F':15, 'P':16, 'S':17, 'T':18, 'W':19, 'Y':20, 'V':21}

    # Test that url is in protein_url_entry
    print ("Protein URL: ", protein_url_entry.get())

    # Extract just amino acid sequence from url
    # url = "http://www.uniprot.org/uniprot/P37288.fasta"
    url = protein_url_entry.get()
    response = urlopen(url)
    raw_fasta = response.read().decode("utf-8", "ignore")

    # Split on lines, define sequence and sequence name
    raw_fasta = raw_fasta.split('\n')
    sequence_name = raw_fasta[0]
    sequence_name = sequence_name.split('|')[1]
    sequence = raw_fasta[1:]
    sequence = ''.join(sequence)

    # Define empty note list to fill with integers.
    # Define empty Music list to fill with notes later.
    NoteList = []
    Music = []

    # Fill NoteList with integers, depending on amino acid
    for aa in sequence:
        NoteList.append(aa_notes[aa])

    # Print NoteList, confirm there are integers
    print(NoteList)

    # Generate Music list of notes
    for x in NoteList:
        Music.append(Note(x))

    print(Music)

    seq1 = NoteSeq(Music)

    midi = Midi()
    midi.seq_notes(seq1)
    print (midi)
    midi.write(sequence_name + ".mid")



#####
##### TKINTER PORTION OF CODE, CREATE BASIC GUI
#####

# Define master, title of tkinter program
master = Tk(className=" Music From Protein Sequence")

# Write out descriptive label for program
Label(master, text="This program converts protein sequences into musical midi files.  \n\
Input a uniprot.org fasta file URL. A midi file of the sequence will be generated.\n\
(Example: http://www.uniprot.org/uniprot/P37288.fasta)").grid(columnspan=3)

# Label to left of protein_url_entry
Label(master, text="Sequence uniprot.org URL: ").grid(row=1, column=0)

# Define protein_url_entry, define position in gui
protein_url_entry = Entry(master)
protein_url_entry.grid(row=1, column=1, columnspan=2)

# Create quite button and function execution button
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W+E+N+S, pady=4)
Button(master, text='Generate MIDI file', command=aa_to_music).grid(row=3, column=1, sticky=W+E+N+S, pady=4)

mainloop( )
