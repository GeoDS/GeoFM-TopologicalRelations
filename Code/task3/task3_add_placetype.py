from collections import defaultdict
import openai
import csv

import sys

if len(sys.argv) < 2:
    print("Usage: python script.py filename")
    sys.exit(1)

filename = sys.argv[1]
# filename = "3_answer_object_place_type_3.csv"
headers = ["relation_predicate", "subject_place_type","object_place_type", "Response","actual_relation"]

client = openai.OpenAI(api_key='')
def run(place_type_subject,place_type_object,relation_predicate,relation):
    response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": """
                    The given seven PREDICATES: contains, is within, touches, crosses, disjoint, overlaps, equals. 
                    Given a sentence that include a vernacular spatial relation term: please give the corresponding PREDICATES. 
                    - Indicate spatial relation from A to B only.
                    - The vernacular spatial relation term should consider its typical meanings of the terms and the general geographical relationship it represent. Also pay attention to any other context that you can get from the sentence. 
                    - MAKE SURE the [PREDICATE] satisfies the the dimension requirements defined by DE-9IM and OGC given Geometry Type A and Geometry Type B.
                    - MAKE SURE that the output includes all plausible predicates and excludes any that are impossible or irrelevant in the given context. 
                    OUTPUT FORMAT: 
                        Analysis: Provide a detailed, professional, and coherent examination of the spatial relation from A to B.
                        Answer: A [PREDICATE1/PREDICATE2...] B. For example: A [overlaps/is within] B
"""},
                {"role": "user", "content": """given the sentence: A {} B and A is {}, B is {}.""".format(relation_predicate,place_type_subject,place_type_object)}
            ],
            temperature=0.1
    )
    # with open("3_answer_object_place_type_2.txt","a") as outputfile:
    #     line="""relation_predicate:{},object_place_type:{}, response:{}""".format(relation_predicate,place_type_object,response.choices[0].message.content)
    #     outputfile.writelines(line)
    #     outputfile.writelines("\n")



    line = [relation_predicate, place_type_subject,place_type_object, response.choices[0].message.content,relation]
    with open(filename, "a", newline="") as outputfile: 
        csvwriter = csv.writer(outputfile)
        if outputfile.tell() == 0:
            csvwriter.writerow(headers)
        csvwriter.writerow(line)

# descrption_list=[['along the border/touches', 'county'],
# ['along the border/is within', 'county'],
# ['along/crosses', 'water'],
# ['along/touches', 'water'],
# ['bordering/overlaps', 'municipality'],
# ['bordering/touches', 'municipality'], ['bordering/touches', 'county'], ['bordering/touches', 'city'],
# ['county seat of/overlaps', 'county'],
# ['county seat of/is within', 'county'],
# ['is a certain direction from/disjoint', 'city'], ['is a certain direction from/disjoint', 'island'], ['is a certain direction from/disjoint', 'amenity'], ['is a certain direction from/disjoint', 'municipality'],
# ['is a certain direction from/touches', 'village'], ['is a certain direction from/touches', 'city'], ['is a certain direction from/touches', 'municipality'],
# ['is is home to/contains', 'amenity'], ['is is home to/contains', 'building'], ['is is home to/contains', 'commercial'], ['is is home to/contains', 'man_made'], ['is is home to/contains', 'park'], ['is is home to/contains', 'quarter'], ['is is home to/contains', 'tourism'],
# ['is is home to/disjoint', 'aeroway'], ['is is home to/disjoint', 'amenity'], ['is is home to/disjoint', 'building'], ['is is home to/disjoint', 'commercial'], ['is is home to/disjoint', 'industrial'], ['is is home to/disjoint', 'office'], ['is is home to/disjoint', 'retail'],
# ['is is home to/overlaps', 'amenity'], ['is is home to/overlaps', 'commercial'], ['is is home to/overlaps', 'shop'], ['is is home to/overlaps', 'water'],
# ['in/overlaps', 'county'],
# ['in/touches', 'municipality'],
# ['in/is within', 'county'], ['in/is within', 'historic'],
# ['located in/touches', 'municipality'],
# ['located in/is within', 'county'],
# ['is mostly in/overlaps', 'county'], ['is mostly in/overlaps', 'municipality'],
# ['is mostly in/touches', 'municipality'],
# ['near/disjoint', 'leisure'],
# ['near/touches', 'water'],
# ['is partly in/overlaps', 'county'], ['is partly in/overlaps', 'island'], ['is partly in/overlaps', 'municipality'],
# ['is partly in/touches', 'municipality'],
# ['situated on/crosses', 'water'],
# ['situated on/overlaps', 'water'],
# ['situated on/touches', 'water'],
# ['straddling/crosses', 'water'],
# ['straddling/overlaps', 'county'],
# ['surrounded by/overlaps', 'municipality'],
# ['surrounded by/touches', 'municipality'], ['surrounded by/touches', 'village'],
# ['surrounding/disjoint', 'city'],
# ['surrounding/overlaps', 'city']]


# descrption_list=[['highway','city','is located on'],
# ['lake','city','is located on'],
# ['river','city','is located on'],
# ['river','county','is located on'],
# ['city','village','is located on'],
# ['city','military','is located on'],
# ['city','county','is to the south of'],
# ['city','city','is to the south of'],
# ['municipality','city','is to the south of'],
# ['water','city','is to the south of'],
# ['national_park','county','is to the south of'],
# ['national_park','national_park','is to the south of'],
# ['college','city','is to the south of'],
# ['locality','city','is to the south of'],
# ['city','village','is to the south of'],
# ['county','county','is to the south of'],
# ['county','city','is to the south of'],
# ['amenity','city','is home to'],
# ['building','city','is home to'],
# ['commercial','city','is home to'],
# ['man_made','city','is home to'],
# ['park','city','is home to'],
# ['quarter','city','is home to'],
# ['tourism','city','is home to'],
# ['neighbourhood','city','is home to'],
# ['leisure','city','is home to'],
# ['aeroway','city','is home to'],
# ['shop','city','is home to'],
# ['water','city','is home to'],
# ['county','city','is mostly in'],
# ['municipality','city','is mostly in'],
# ['county','city','is partly in'],
# ['island','city','is partly in'],
# ['municipality','city','is partly in'],
# ['halmet','tourism','is within'],
# ['county','city','is within'],
# ['municipality','city','is within'],
# ['city','city','is within'],
# ['city','amenity','is within'],
# ['city','city','surrounds'],
# ['moutain range','city','surrounds'],
# ['municipality','city','surrounds']]

descrption_list=[
['borders','1','touches','place_type','city/city'],
['borders','1','touches','place_type','city/municipality'],
['connect C and','1','crosses','place_type','industrial/city'],
['extend into','1','overlaps','place_type','city/county'],
['is adjacent to','1','touches','place_type','city/municipality'],
['is between C and','1','touches','place_type','town/town'],
['is bordered by','1','touches','place_type','town/city'],
['is bounded by','1','touches','place_type','city/city'],
['is home to','1','contains','place_type','city/amenity'],
['is in','1','within','place_type','village/county'],
['is located in','1','within','place_type','city/state'],
['is located in','1','within','place_type','town/county'],
['is located in','1','within','place_type','village/county'],
['is partly in','1','overlaps','place_type','city/county'],
['is surrounded by','1','touches','place_type','city/city'],
['is surrounded by','1','touches','place_type','town/city'],
['is within','1','touches','place_type','city/municipality']]

for description_word in descrption_list:
    place_type_subject = description_word[4].split('/')[0]
    place_type_object = description_word[4].split('/')[1]
    relation_predicate = description_word[0]
    relation=description_word[2]
    run(place_type_subject,place_type_object,relation_predicate,relation)
    print(description_word)





