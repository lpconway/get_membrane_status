# get_membrane_status
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
