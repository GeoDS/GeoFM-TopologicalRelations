import pandas as pd
import osmnx as ox
from shapely import wkt
import csv

def main():
    # csv_file = 'data_for_tx/placename_and_relation_tx_final_only_placename.txt'
    csv_file = 'data_for_tx/placename_and_relation_tx_final copy.csv'
    output_file = 'data_for_tx/wkt_result_tx_error.txt'
    
    # with open(csv_file,'r') as readfile:
    #     entities=readfile.readline()
    # entities_list=entities.split('","')
    # df = pd.read_csv(csv_file)

    entities=[]
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
    
        for row in reader:
            if len(row) == 2:
                entities.append(row[0])
                entities.append(row[1])
    
    # if '1' not in df.columns or '3' not in df.columns:
    #     print("CSV file must contain columns '2' and '4'")
    #     return

    with open(output_file, 'w') as f:
        for entity in entities: #for each row
                query = entity
                try:
                    print(query)
                    results = ox.geocode_to_gdf(query)
                    print(results)
                    if not results.empty:
                        results['wkt'] = results['geometry'].apply(lambda x: wkt.dumps(x))
                        f.write(f"\n{query}\n") 
                        for w in results['wkt']:
                            f.write(f"{w}\n")
                    else:
                        f.write(f"\n{query}\nNo results found.\n")
                except Exception as e:
                    f.write(f"\n{query}\nFailed to geocode. Error: {str(e)}\n")

if __name__ == "__main__":
    main()
