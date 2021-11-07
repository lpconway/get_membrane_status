# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:08:12 2020

@author: Louis
"""
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request

def get_membrane_status(uniprot_accession, verbose=False, uniprot_path=None):
    """
    Checks whether a protein has one or more transmembrane domains, as
    annotated by UniProt

    Parameters
    ----------
    uniprot_accession : string
        Accession code of the protein in question.
    verbose : bool, optional
        Prints the current protein being checked. May be useful when looping
        over many proteins. The default is False.
    uniprot_path : string/None, optional
        A path in which UniProt xml files can be found. The default is None,
        and uses the UniProt website.

    Returns
    -------
    A bool denoting whether or not the given protein has one or more
    transmembrane domains, as annotated by UniProt

    """
    if verbose:
        print(uniprot_accession)
    try:
        if type(uniprot_path) == str:
            f = open(uniprot_path+uniprot_accession+'.xml', 'r')
            soup = BeautifulSoup(f, 'xml')
        if uniprot_path == None:
                url = 'https://www.uniprot.org/uniprot/'+uniprot_accession+'.xml'
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req) as f:
                   response = f.read()
                soup = BeautifulSoup(response, 'xml')
    except:
        print(uniprot_accession + ' not found')
        return(None)
    if soup.find(attrs={"type": "transmembrane region"}):
        return(True)
    else:
        return(False)