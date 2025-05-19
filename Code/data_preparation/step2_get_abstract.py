from SPARQLWrapper import SPARQLWrapper, JSON
import os
import time
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_abstract_from_dbpedia(url):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    # sparql.setRequestMethod("GET")  # Ensure using GET method
    sparql.addCustomHttpHeader("User-Agent", "Mozilla/5.0 (compatible; MyBot/0.1; +http://example.com/bot)")

    resource = "<" + url + ">"

    # query = """
    # SELECT ?abstract 
    # WHERE {
    #     """ + resource + """ dbo:abstract ?abstract .
    #     FILTER(lang(?abstract) = "en")
    # }
    # """
    query = f"""
    SELECT ?abstract 
    WHERE {{
        {resource} dbo:abstract ?abstract .
        FILTER(lang(?abstract) = "en")
    }}
    """
    
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    # sparql.setTimeout(10)
    
    # results = sparql.query().convert()
    try:
        results=sparql.queryAndConvert()
        

        abstracts = results["results"]["bindings"]
        if abstracts:
            return abstracts[0]["abstract"]["value"]
        else:
            return None
    except:
        print(url+"error!!")

if __name__ == "__main__":
    # url = "http://dbpedia.org/resource/Madison,_Wisconsin"
    with open("data_for_tx/city_links_tx.txt","r") as readfile:
        for url in readfile:
            url=url.strip()
            abstract = get_abstract_from_dbpedia(url)
            if(abstract==None):
                abstract="none"
            with open("data_for_tx/text_description_tx.txt", "a") as outfile:
                outfile.write(abstract+"\n")
