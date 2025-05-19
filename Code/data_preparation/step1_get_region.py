from SPARQLWrapper import SPARQLWrapper, JSON

def get_us_administrative_regions_links():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dbr: <http://dbpedia.org/resource/>

        SELECT DISTINCT ?city WHERE {
            ?city a dbo:City ; 
                dbo:subdivision dbr:California.
        }

    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    region_links = [result['city']['value'] for result in results['results']['bindings']]
    return region_links

if __name__ == "__main__":
    links = get_us_administrative_regions_links()
    with open("data_for_california/city_links_ca.txt", "w") as file:
        for link in links:
            file.write(link + "\n")